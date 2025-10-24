from src.components.pos_fr_api.api import PositivoFederalRevenueApi
from src.components.database_clients.clients.registrations_client import RegistrationsClient
from src.components.database_clients.clients.nceas_client import NceasClient
from src.components.database_clients.clients.state_registrations_client import StateRegistrationsClient
from src.components.database_clients.clients.suframa_registrations_client import SuframaRegistrationsClient
from src.components.log_system import LogSystem
from src.components.date_utility import DateUtility
from src.components.registrations_docs_handler import RegistrationsDocsHandler
from src.components.session_manager import SessionManager

from .models import Response

from src.io.models import NewRegistration

class IncludeNewRegistration:
    
    def __init__(self) -> None:
        self.federal_revenue_api = PositivoFederalRevenueApi()
        self.registrations_client = RegistrationsClient("prd")
        self.state_registrations_client = StateRegistrationsClient("prd")
        self.suframa_registrations_client = SuframaRegistrationsClient("prd")
        self.nceas_client = NceasClient("prd")
        self.log_system = LogSystem("include_new_registration")
        self.date_utility = DateUtility()
        self.docs_handler = RegistrationsDocsHandler()
        self.session_manager = SessionManager()
    
    def execute(self, new_registration: NewRegistration) -> Response:
        try:
            federal_revenue_data = self.federal_revenue_api.get_data(new_registration.cnpj)
            registration_exists = self.registrations_client.read(new_registration.cnpj)
            if registration_exists:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Tentativa de inclusão de cadastro já existente: {new_registration.cnpj}.")
                return Response(success=False, message="❌ Tentativa de inclusão de cadastro já existente: {new_registration.cnpj}.")    
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
                registration_date_hour=None,
                charge_date_hour=None,
                federal_revenue_consult_date=self.date_utility.get_today(),
                doc_resent=None,
                client_type=new_registration.client_type,
                suggested_limit=new_registration.suggested_limit,
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
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n✅ Novo cadastro incluído com sucesso: {new_registration.cnpj}.")
            return Response(success=True, message=f"✅ Novo cadastro incluído com sucesso: {new_registration.cnpj}.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Erro:\n{error}")
            raise Exception("❌ Erro interno ao incluir novo cadastro. Contate o administrador.")
