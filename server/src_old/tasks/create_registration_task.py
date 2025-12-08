from src.engines.federal_revenue_api_engine.federal_revenue_api_engine import FederalRevenueApiEngine
from src.engines.database_engine.database_engine import DatabaseEngine
from src.engines.log_engine import LogEngine
from src.engines.date_engine import DateEngine
from src.engines.registrations_docs_engine import RegistrationsDocsEngine
from src.engines.wsgi_engine.wsgi_session_manager_engine import WsgiSessionManagerEngine
from src.engines.cli_session_manager_engine import CliSessionManagerEngine

from dataclasses import dataclass
from werkzeug.datastructures import FileStorage

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

@dataclass
class RegistrationData:
    
    cnpj: str
    seller: str
    email: str
    cpf: str
    cpf_person: str
    tax_regime: str
    client_type: str
    suggested_limit: float
    article_association_doc: FileStorage
    bank_doc: FileStorage | None

class CreateRegistrationTask:
    
    def __init__(self,
        federal_revenue_api_engine: FederalRevenueApiEngine,
        database_engine: DatabaseEngine,
        log_engine: LogEngine,
        date_engine: DateEngine,
        registrations_docs_engine: RegistrationsDocsEngine,
        session_manager_engine: WsgiSessionManagerEngine | CliSessionManagerEngine,
        need_authentication: bool
    ) -> None:
        self.federal_revenue_api_engine = federal_revenue_api_engine
        self.database_engine = database_engine
        self.log_engine = log_engine
        self.date_engine = date_engine
        self.registrations_docs_engine = registrations_docs_engine
        self.session_manager_engine = session_manager_engine
        self.need_authentication = need_authentication
    
    def _verify_data(self, registration_data: RegistrationData) -> Response | None:
        registration_data.cnpj = "".join(number for number in registration_data.cnpj if number.isdigit())
        if len(registration_data.cnpj) != 14:
            return Response(success=False, message="❌ CNPJ inválido.", data=[])
        registration_data.cpf = "".join(number for number in registration_data.cpf if number.isdigit())
        if len(registration_data.cpf) != 11:
            return Response(success=False, message="❌ CPF inválido.", data=[])
        if not "@" in registration_data.email or not "." in registration_data.email:
            return Response(success=False, message="❌ E-mail inválido.", data=[])
        if registration_data.tax_regime not in ["SIMPLES", "CUMULATIVO", "NÃO CUMULATIVO"]:
            return Response(success=False, message="❌ Regime tributário deve ser: SIMPLES, CUMULATIVO ou NÃO CUMULATIVO.", data=[])
        if registration_data.client_type not in ["REVENDA", "MINHA EMPRESA"]:
            return Response(success=False, message="❌ Tipo do cliente deve ser REVENDA ou MINHA EMPRESA.", data=[])
    
    def _sanitize(self, registration_data: RegistrationData) -> RegistrationData:
        registration_data.seller = registration_data.seller.upper()
        registration_data.email = registration_data.email.lower()
        registration_data.cpf_person = registration_data.cpf_person.upper()
        return registration_data
    
    def main(self,
        cnpj: str,
        seller: str,
        email: str,
        cpf: str,
        cpf_person: str,
        tax_regime: str,
        client_type: str,
        suggested_limit: float,
        article_association_doc: FileStorage,
        bank_doc: FileStorage | None,
    ) -> Response:
        try:
            if self.need_authentication:
                if not self.session_manager_engine.is_user_in_session():
                    return Response(success=False, message="❌ Necessário fazer login.", data=[])
                if not self.session_manager_engine.have_user_module_access("zRegRpa"):
                    return Response(success=False, message="❌ Sem acesso.", data=[])
            registration_exists = self.database_engine.registrations_client.read(cnpj)
            if registration_exists:
                return Response(success=False, message="❌ Tentativa de inclusão de cadastro já existente ({new_registration.cnpj}).", data=[])
            federal_revenue_data = self.federal_revenue_api_engine.get_data(cnpj)
            registration_data = RegistrationData(
                cnpj=cnpj,
                email=email,
                tax_regime=tax_regime,
                client_type=client_type,
                suggested_limit=suggested_limit,
                seller=seller,
                cpf=cpf,
                cpf_person=cpf_person,
                article_association_doc=article_association_doc,
                bank_doc=bank_doc
            )
            response = self._verify_data(registration_data)
            if response:
                return response
            registration_data = self._sanitize(registration_data)
            self.database_engine.registrations_client.create(
                cnpj=registration_data.cnpj,
                opening=federal_revenue_data.opening,
                company_name=federal_revenue_data.company_name,
                trade_name=federal_revenue_data.trade_name,
                legal_nature=federal_revenue_data.legal_nature,
                legal_nature_id=federal_revenue_data.legal_nature_id,
                registration_status=federal_revenue_data.registration_status,
                street=federal_revenue_data.street,
                number=federal_revenue_data.number,
                complement=federal_revenue_data.complement,
                neighborhood=federal_revenue_data.neighborhood,
                pac=federal_revenue_data.pac,
                city=federal_revenue_data.city,
                state=federal_revenue_data.state,
                fone=federal_revenue_data.fone,
                email=registration_data.email,
                tax_regime=registration_data.tax_regime,
                comission_receipt=federal_revenue_data.comission_receipt,
                status="Cadastrar",
                registration_date_hour="-",
                charge_date_hour="-",
                federal_revenue_consult_date=self.date_engine.get_today_str(),
                doc_resent=False,
                client_type=registration_data.client_type,
                suggested_limit=registration_data.suggested_limit,
                seller=registration_data.seller,
                cpf=registration_data.cpf,
                cpf_person=registration_data.cpf_person
            )
            for ncea in federal_revenue_data.ncea:
                self.database_engine.nceas_client.create(
                    cnpj=registration_data.cnpj,
                    ncea=ncea["code"],
                    description=ncea["description"]
                )
            for state_registration in federal_revenue_data.state_registrations:
                self.database_engine.state_registrations_client.create(
                    cnpj=registration_data.cnpj,
                    state_registration=state_registration["state_registration"],
                    status=state_registration["status"]
                )
            for suframa_registration in federal_revenue_data.suframa_registrations:
                self.database_engine.suframa_registrations_client.create(
                    cnpj=registration_data.cnpj,
                    suframa_registration=suframa_registration["suframa_registration"],
                    status=suframa_registration["status"]
                )
            doc_list = [registration_data.article_association_doc]
            if registration_data.bank_doc:
                doc_list.append(registration_data.bank_doc)
            self.registrations_docs_engine.save_docs(cnpj=registration_data.cnpj, docs=doc_list)
            self.log_engine.write_text(f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Novo cadastro incluído com sucesso ({registration_data.cnpj}).")
            return Response(success=True, message=f"✅ Novo cadastro incluído com sucesso ({registration_data.cnpj}).", data=[])
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (CreateRegistrationTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao incluir novo cadastro. Contate o administrador.")
