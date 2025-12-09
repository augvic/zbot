from src.engines.list.database_engine.database_engine import DatabaseEngine
from src.engines.list.log_engine import LogEngine
from src.engines.list.registrations_docs_engine import RegistrationsDocsEngine
from src.engines.list.wsgi_engine.wsgi_session_manager_engine import WsgiSessionManagerEngine
from src.engines.list.cli_session_manager_engine import CliSessionManagerEngine
from src.engines.list.date_engine import DateEngine

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
    opening: str
    company_name: str
    trade_name: str
    legal_nature: str
    legal_nature_id: str
    registration_status: str
    street: str
    number: str
    complement: str
    neighborhood: str
    pac: str
    city: str
    state: str
    fone: str
    email: str
    tax_regime: str
    comission_receipt: str
    status: str
    client_type: str
    seller: str
    cpf: str
    cpf_person: str
    suggested_limit: float
    bank_doc: FileStorage | None
    article_association_doc: FileStorage | None

class UpdateRegistrationTask:
    
    def __init__(self,
        session_manager_engine: WsgiSessionManagerEngine | CliSessionManagerEngine,
        database_engine: DatabaseEngine,
        log_engine: LogEngine,
        registrations_docs_engine: RegistrationsDocsEngine,
        date_engine: DateEngine,
        need_authentication: bool
    ) -> None:
        self.database_engine = database_engine
        self.log_engine = log_engine
        self.registrations_docs_engine = registrations_docs_engine
        self.session_manager_engine = session_manager_engine
        self.date_engine = date_engine
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
            return Response(success=False, message="❌ Tipo do cliente deve ser: REVENDA ou MINHA EMPRESA.", data=[])
        is_date = self.date_engine.is_date(registration_data.opening)
        if not is_date:
            return Response(success=False, message="❌ Data deve ser no formato (dd/mm/aaaa).", data=[])
        if not registration_data.status in ["Cadastrar", "Aguardando Assinatura", "Erro"]:
            return Response(success=False, message="❌ Status deve ser: Cadastrar, Aguardando Assinatura ou Erro.", data=[])
    
    def _sanitize(self, registration_data: RegistrationData) -> RegistrationData:
        registration_data.company_name = registration_data.company_name.upper()
        registration_data.trade_name = registration_data.trade_name.upper()
        registration_data.legal_nature = registration_data.legal_nature.upper()
        registration_data.registration_status = registration_data.registration_status.upper()
        registration_data.street = registration_data.street.upper()
        registration_data.complement = registration_data.complement.upper()
        registration_data.neighborhood = registration_data.neighborhood.upper()
        registration_data.city = registration_data.city.upper()
        registration_data.state = registration_data.state.upper()
        registration_data.tax_regime = registration_data.tax_regime.upper()
        registration_data.client_type = registration_data.client_type.upper()
        registration_data.seller = registration_data.seller.upper()
        registration_data.email = registration_data.email.lower()
        registration_data.cpf_person = registration_data.cpf_person.upper()
        return registration_data
    
    def main(self,
        cnpj: str,
        opening: str,
        company_name: str,
        trade_name: str,
        legal_nature: str,
        legal_nature_id: str,
        registration_status: str,
        street: str,
        number: str,
        complement: str,
        neighborhood: str,
        pac: str,
        city: str,
        state: str,
        fone: str,
        email: str,
        tax_regime: str,
        comission_receipt: str,
        status: str,
        client_type: str,
        seller: str,
        cpf: str,
        cpf_person: str,
        suggested_limit: float,
        bank_doc: FileStorage | None,
        article_association_doc: FileStorage | None,
    ) -> Response:
        try:
            if self.need_authentication:
                if not self.session_manager_engine.is_user_in_session():
                    return Response(success=False, message="❌ Necessário fazer login.", data=[])
                if not self.session_manager_engine.have_user_module_access("zRegRpa"):
                    return Response(success=False, message="❌ Sem acesso.", data=[])
            registration_exists = self.database_engine.registrations_client.read(cnpj)
            if not registration_exists:
                return Response(success=False, message="❌ Cadastro não existe.", data=[])
            if registration_exists.opening == opening \
                and registration_exists.company_name == company_name \
                and registration_exists.trade_name == trade_name \
                and registration_exists.legal_nature == legal_nature \
                and registration_exists.legal_nature_id == legal_nature_id \
                and registration_exists.registration_status == registration_status \
                and registration_exists.street == street \
                and registration_exists.number == number \
                and registration_exists.complement == complement \
                and registration_exists.neighborhood == neighborhood \
                and registration_exists.pac == pac \
                and registration_exists.city == city \
                and registration_exists.state == state \
                and registration_exists.fone == fone \
                and registration_exists.email == email \
                and registration_exists.tax_regime == tax_regime \
                and registration_exists.comission_receipt == comission_receipt \
                and registration_exists.status == status \
                and registration_exists.client_type == client_type \
                and registration_exists.suggested_limit == suggested_limit \
                and registration_exists.seller == seller \
                and registration_exists.cpf == cpf \
                and registration_exists.cpf_person == cpf_person:
                    return Response(success=True, message="⚠️ Nenhum dado do cadastro modificado.", data=[])
            registration_data = RegistrationData(
                cnpj=cnpj,
                opening=opening,
                company_name=company_name,
                trade_name=trade_name,
                legal_nature=legal_nature,
                legal_nature_id=legal_nature_id,
                registration_status=registration_status,
                street=street,
                number=number,
                complement=complement,
                neighborhood=neighborhood,
                pac=pac,
                city=city,
                state=state,
                fone=fone,
                email=email,
                tax_regime=tax_regime,
                comission_receipt=comission_receipt,
                status=status,
                client_type=client_type,
                suggested_limit=suggested_limit,
                seller=seller,
                cpf=cpf,
                cpf_person=cpf_person,
                bank_doc=bank_doc,
                article_association_doc=article_association_doc
            )
            response = self._verify_data(registration_data)
            if response:
                return response
            registration_data = self._sanitize(registration_data)
            self.database_engine.registrations_client.update(
                cnpj=registration_data.cnpj,
                opening=registration_data.opening,
                company_name=registration_data.company_name,
                trade_name=registration_data.trade_name,
                legal_nature=registration_data.legal_nature,
                legal_nature_id=registration_data.legal_nature_id,
                registration_status=registration_data.registration_status,
                street=registration_data.street,
                number=registration_data.number,
                complement=registration_data.complement,
                neighborhood=registration_data.neighborhood,
                pac=registration_data.pac,
                city=registration_data.city,
                state=registration_data.state,
                fone=registration_data.fone,
                email=registration_data.email,
                tax_regime=registration_data.tax_regime,
                comission_receipt=registration_data.comission_receipt,
                status=registration_data.status,
                client_type=registration_data.client_type,
                suggested_limit=registration_data.suggested_limit,
                seller=registration_data.seller,
                cpf=registration_data.cpf,
                cpf_person=registration_data.cpf_person
            )
            doc_list = []
            if registration_data.article_association_doc:
                doc_list.append(registration_data.article_association_doc)
            if registration_data.bank_doc:
                doc_list.append(registration_data.bank_doc)
            self.registrations_docs_engine.save_docs(cnpj=registration_data.cnpj, docs=doc_list)
            self.log_engine.write_text("tasks_update_registration_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Cadastro ({registration_data.cnpj}) atualizado.")
            return Response(success=True, message="✅ Cadastro atualizado.", data=[])
        except Exception as error:
            self.log_engine.write_error("tasks_update_registration_task", f"❌ Error in (UpdateRegistrationTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao atualizar cadastro. Contate o administrador.")
