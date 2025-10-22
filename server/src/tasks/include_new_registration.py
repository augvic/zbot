from src.components.pos_fr_api.api import PositivoFederalRevenueApi
from src.components.database.clients.registrations_client import RegistrationsClient
from src.components.database.clients.nceas_client import NceasClient
from src.components.database.clients.state_registrations_client import StateRegistrationsClient
from src.components.database.clients.suframa_registrations_client import SuframaRegistrationsClient
from src.components.log_system import LogSystem
from datetime import datetime
from os import path, makedirs
from werkzeug.datastructures import FileStorage
import sys

class IncludeNewRegistration:
    
    def _setup(self) -> None:
        self.federal_revenue_api = PositivoFederalRevenueApi()
        self.registrations_client = RegistrationsClient("prd")
        self.state_registrations_client = StateRegistrationsClient("prd")
        self.suframa_registrations_client = SuframaRegistrationsClient("prd")
        self.nceas_client = NceasClient("prd")
        self.log_system = LogSystem("include_new_registration")
    
    def execute(self,
        cnpj: str,
        seller: str,
        email: str,
        cpf: str,
        cpf_person: str,
        tax_regime: str,
        article_association_doc: FileStorage | None,
        client_type: str,
        suggested_limit: str = "",
        bank_doc: FileStorage | None = None,
    ) -> dict[str, str | bool]:
        self._setup()
        try:
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
            if getattr(sys, 'frozen', False):
                base_path = path.dirname(sys.executable)
            else:
                base_path = path.join(path.dirname(__file__), "..", "..")
            dir_to_create = path.abspath(path.join(base_path, "storage", ".clients_docs", cnpj))
            makedirs(dir_to_create, exist_ok=True)
            if article_association_doc:
                article_association_doc.save(f"{dir_to_create}/{article_association_doc.filename}")
            if bank_doc:
                bank_doc.save(f"{dir_to_create}/{bank_doc.filename}")
            return {"success": True, "message": "Cadastro incluído."}
        except Exception as error:
            self.log_system.write_error(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}")
            return {"success": False, "message": "Erro ao incluir cadastro."}
