from src.components.infra.pos_fr_api.component import PositivoFederalRevenueApi
from src.components.infra.database_clients.clients.registrations_client import RegistrationsClient
from src.components.infra.database_clients.clients.nceas_client import NceasClient
from src.components.infra.database_clients.clients.state_registrations_client import StateRegistrationsClient
from src.components.infra.database_clients.clients.suframa_registrations_client import SuframaRegistrationsClient
from src.components.file_system.log_system import LogSystem
from src.components.gear.date_utility import DateUtility
from src.components.file_system.registrations_docs_handler import RegistrationsDocsHandler
from src.components.infra.session_manager import SessionManager
from .models import Response, NewRegistration

class CreateRegistration:
    
    def __init__(self,
        federal_revenue_api: PositivoFederalRevenueApi,
        registrations_client: RegistrationsClient,
        state_registrations_client: StateRegistrationsClient,
        suframa_registrations_client: SuframaRegistrationsClient,
        nceas_client: NceasClient,
        log_system: LogSystem,
        date_utility: DateUtility,
        docs_handler: RegistrationsDocsHandler,
        session_manager: SessionManager
    ) -> None:
        self.federal_revenue_api = federal_revenue_api
        self.registrations_client = registrations_client
        self.state_registrations_client = state_registrations_client
        self.suframa_registrations_client = suframa_registrations_client
        self.nceas_client = nceas_client
        self.log_system = log_system
        self.date_utility = date_utility
        self.docs_handler = docs_handler
        self.session_manager = session_manager
    
    def _verify_not_nullables(self, new_registration: NewRegistration) -> Response | None:
        if not new_registration.cnpj:
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o CNPJ.")
            return Response(success=False, message="❌ Preencha o CNPJ.")
        if not new_registration.seller:
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o vendedor.")
            return Response(success=False, message="❌ Preencha o vendedor.")
        if not new_registration.email:
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o e-mail.")
            return Response(success=False, message="❌ Preencha o e-mail.")
        if not new_registration.cpf:
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o CPF.")
            return Response(success=False, message="❌ Preencha o CPF.")
        if not new_registration.cpf_person:
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o representante legal.")
            return Response(success=False, message="❌ Preencha o representante legal.")
        if not new_registration.tax_regime:
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o regime tributário.")
            return Response(success=False, message="❌ Preencha o regime tributário.")
        if not new_registration.client_type:
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o tipo do cliente.")
            return Response(success=False, message="❌ Preencha o tipo do cliente.")
        if not new_registration.article_association_doc:
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Envie o contrato social.")
            return Response(success=False, message="❌ Envie o contrato social.")
    
    def _verify_types(self, new_registration: NewRegistration) -> Response | None:
        if not isinstance(new_registration.cnpj, str):
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ CNPJ deve ser string type.")
            return Response(success=False, message="❌ CNPJ deve ser string type.")
        if not isinstance(new_registration.seller, str):
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Vendedor deve ser string type.")
            return Response(success=False, message="❌ Vendedor deve ser string type.")
        if not isinstance(new_registration.email, str):
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ E-mail deve ser string type.")
            return Response(success=False, message="❌ E-mail deve ser string type.")
        if not isinstance(new_registration.cpf, str):
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ CPF deve ser string type.")
            return Response(success=False, message="❌ CPF deve ser string type.")
        if not isinstance(new_registration.cpf_person, str):
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Representante legal deve ser string type.")
            return Response(success=False, message="❌ Representante legal deve ser string type.")
        if not isinstance(new_registration.tax_regime, str):
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Regime tributário deve ser string type.")
            return Response(success=False, message="❌ Regime tributário deve ser string type.")
        if not isinstance(new_registration.client_type, str):
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Tipo do cliente deve ser string type.")
            return Response(success=False, message="❌ Tipo do cliente deve ser string type.")
        if new_registration.suggested_limit:
            if not isinstance(new_registration.suggested_limit, float):
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Limite sugerido deve ser float type.")
                return Response(success=False, message="❌ Limite sugerido deve ser float type.")
    
    def _verify_data(self, new_registration: NewRegistration) -> Response | None:
        new_registration.cnpj = "".join(number for number in new_registration.cnpj if number.isdigit())
        if len(new_registration.cnpj) != 14:
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ CNPJ ({new_registration.cnpj}) inválido.")
            return Response(success=False, message="❌ CNPJ inválido.")
        new_registration.cpf = "".join(number for number in new_registration.cpf if number.isdigit())
        if len(new_registration.cpf) != 11:
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ CPF ({new_registration.cpf}) inválido.")
            return Response(success=False, message="❌ CPF inválido.")
        if not "@" in new_registration.email or not "." in new_registration.email:
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ E-mail inválido.")
            return Response(success=False, message="❌ E-mail inválido.")
        if new_registration.tax_regime not in ["SIMPLES", "CUMULATIVO", "NÃO CUMULATIVO"]:
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Regime tributário deve ser: SIMPLES, CUMULATIVO ou NÃO CUMULATIVO.")
            return Response(success=False, message="❌ Regime tributário deve ser: SIMPLES, CUMULATIVO ou NÃO CUMULATIVO.")
        if new_registration.client_type not in ["REVENDA", "MINHA EMPRESA"]:
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Tipo do cliente deve ser: REVENDA ou MINHA EMPRESA.")
            return Response(success=False, message="❌ Tipo do cliente deve ser: REVENDA ou MINHA EMPRESA.")
    
    def _sanitize(self, new_registration: NewRegistration) -> NewRegistration:
        new_registration.seller = new_registration.seller.upper()
        new_registration.email = new_registration.email.lower()
        new_registration.cpf_person = new_registration.cpf_person.upper()
        return new_registration
    
    def execute(self, new_registration: NewRegistration) -> Response:
        try:
            response = self._verify_not_nullables(new_registration)
            if response:
                return response
            response = self._verify_types(new_registration)
            if response:
                return response
            response = self._verify_data(new_registration)
            if response:
                return response
            new_registration = self._sanitize(new_registration)
            registration_exists = self.registrations_client.read(new_registration.cnpj)
            if registration_exists:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Tentativa de inclusão de cadastro já existente: {new_registration.cnpj}.")
                return Response(success=False, message="❌ Tentativa de inclusão de cadastro já existente ({new_registration.cnpj}).")
            federal_revenue_data = self.federal_revenue_api.get_data(new_registration.cnpj)
            self.registrations_client.create(
                cnpj=new_registration.cnpj,
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
                email=new_registration.email,
                tax_regime=new_registration.tax_regime,
                comission_receipt=federal_revenue_data.comission_receipt,
                status="Cadastrar",
                registration_date_hour="-",
                charge_date_hour="-",
                federal_revenue_consult_date=self.date_utility.get_today_str(),
                doc_resent="-",
                client_type=new_registration.client_type,
                suggested_limit=new_registration.suggested_limit if new_registration.suggested_limit else "-",
                seller=new_registration.seller,
                cpf=new_registration.cpf,
                cpf_person=new_registration.cpf_person
            )
            for ncea in federal_revenue_data.ncea:
                self.nceas_client.create(
                    cnpj=new_registration.cnpj,
                    ncea=ncea["code"],
                    description=ncea["description"]
                )
            for state_registration in federal_revenue_data.state_registrations:
                self.state_registrations_client.create(
                    cnpj=new_registration.cnpj,
                    state_registration=state_registration["state_registration"],
                    status=state_registration["status"]
                )
            for suframa_registration in federal_revenue_data.suframa_registrations:
                self.suframa_registrations_client.create(
                    cnpj=new_registration.cnpj,
                    suframa_registration=suframa_registration["suframa_registration"],
                    status=suframa_registration["status"]
                )
            doc_list = [new_registration.article_association_doc]
            if new_registration.bank_doc:
                doc_list.append(new_registration.bank_doc)
            self.docs_handler.save_docs(cnpj=new_registration.cnpj, docs=doc_list)
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}). ✅ Novo cadastro incluído com sucesso ({new_registration.cnpj}).")
            return Response(success=True, message=f"✅ Novo cadastro incluído com sucesso ({new_registration.cnpj}).")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao incluir novo cadastro. Contate o administrador.")
