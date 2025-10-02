from src.infrastructure.drivers.federal_revenue_apis import PositivoFederalRevenueApi
from src.infrastructure.drivers.databases.production.clients import RegistrationsClient, SuframaRegistrationsClient, StateRegistrationsClient, NceasClient
from src.infrastructure.managers import SessionManager
from datetime import datetime
from os import path, makedirs
from shutil import copy2

class IncludeNewRegistration:
    
    def _setup(self) -> None:
        self.federal_revenue_api = PositivoFederalRevenueApi()
        self.registrations_client = RegistrationsClient()
        self.state_registrations_client = StateRegistrationsClient()
        self.suframa_registrations_client = SuframaRegistrationsClient()
        self.nceas_client = NceasClient()
        self.session_manager = SessionManager()
    
    def execute(self,
        cnpj: str,
        seller: str,
        email: str,
        cpf: str,
        cpf_person: str,
        tax_regime: str,
        article_association_dir: str,
        bank_doc_dir: str,
        suggested_limit: str,
        client_type: str
    ) -> None:
        self._setup()
        if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access("zNreg"):
            return "Sem autorização.", 401
        federal_revenue_data = self.federal_revenue_api.get_data(cnpj)
        self.registrations_client.create(
            cnpj=cnpj,
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
            email=email,
            tax_regime=tax_regime,
            comission_receipt=federal_revenue_data.comission_receipt,
            status="Cadastrar",
            registration_date_hour="",
            charge_date_hour="",
            federal_revenue_consult_date=datetime.now().strftime("%d/%m/%Y"),
            doc_resent="",
            client_type=client_type,
            suggested_limit=suggested_limit,
            seller=seller,
            cpf=cpf,
            cpf_person=cpf_person
        )
        for ncea in federal_revenue_data.ncea:
            self.nceas_client.create(
                cnpj=cnpj,
                ncea=ncea["code"],
                description=ncea["description"]
            )
        for state_registration in federal_revenue_data.state_registrations:
            self.state_registrations_client.create(
                cnpj=cnpj,
                state_registration=state_registration["state_registration"],
                status=state_registration["status"]
            )
        for suframa_registration in federal_revenue_data.suframa_registrations:
            self.suframa_registrations_client.create(
                cnpj=cnpj,
                suframa_registration=suframa_registration["suframa_registration"],
                status=suframa_registration["status"]
            )
        dir_to_create = path.abspath(path.join(path.dirname(path.abspath(__file__)), f"../storage/clients_docs/{cnpj}"))
        makedirs(dir_to_create, exist_ok=True)
        if article_association_dir:
            article_association_destination = path.join(dir_to_create, path.basename(article_association_dir))
            copy2(article_association_dir, article_association_destination)
        if bank_doc_dir:
            bank_doc_destination = path.join(dir_to_create, path.basename(bank_doc_dir))
            copy2(bank_doc_dir, bank_doc_destination)

if __name__ == "__main__":
    task = IncludeNewRegistration()
    task.execute(
        cnpj="31933143000180",
        seller="ANDRE MARQUES DE SOUSA",
        email="DIEGONEWLIFE@GMAIL.COM",
        cpf="123456789",
        cpf_person="DIEGO FERREIRA DE ARAUJO",
        tax_regime="SIMPLES",
        article_association_dir="",
        bank_doc_dir="",
        suggested_limit="15000.00",
        client_type="Revenda"
    )
