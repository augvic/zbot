from src.modules.positivo_federal_revenue_api.positivo_federal_revenue_api import PositivoFederalRevenueApi
from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.log_system import LogSystem
from src.modules.date_utility import DateUtility
from src.modules.registrations_docs_handler import RegistrationsDocsHandler
from src.modules.sqla_serializer import SqlaSerializer
from src.modules.session_manager import SessionManager

from .models import Response, NewRegistration, RegistrationData

class Registration:
    
    def __init__(self,
        federal_revenue_api: PositivoFederalRevenueApi,
        database_handler: DatabaseHandler,
        log_system: LogSystem,
        date_utility: DateUtility,
        docs_handler: RegistrationsDocsHandler,
        session_manager: SessionManager,
        serializer: SqlaSerializer
    ) -> None:
        self.federal_revenue_api = federal_revenue_api
        self.database_handler = database_handler
        self.log_system = log_system
        self.date_utility = date_utility
        self.docs_handler = docs_handler
        self.session_manager = session_manager
        self.serializer = serializer
    
    def _verify_not_nullables_on_create(self, new_registration: NewRegistration) -> Response | None:
        if not new_registration.cnpj:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o CNPJ.")
            return Response(success=False, message="❌ Preencha o CNPJ.", data=[])
        if not new_registration.seller:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o vendedor.")
            return Response(success=False, message="❌ Preencha o vendedor.", data=[])
        if not new_registration.email:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o e-mail.")
            return Response(success=False, message="❌ Preencha o e-mail.", data=[])
        if not new_registration.cpf:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o CPF.")
            return Response(success=False, message="❌ Preencha o CPF.", data=[])
        if not new_registration.cpf_person:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o representante legal.")
            return Response(success=False, message="❌ Preencha o representante legal.", data=[])
        if not new_registration.tax_regime:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o regime tributário.")
            return Response(success=False, message="❌ Preencha o regime tributário.", data=[])
        if not new_registration.client_type:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o tipo do cliente.")
            return Response(success=False, message="❌ Preencha o tipo do cliente.", data=[])
        if not new_registration.article_association_doc:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Envie o contrato social.")
            return Response(success=False, message="❌ Envie o contrato social.", data=[])
    
    def _verify_types_on_create(self, new_registration: NewRegistration) -> Response | None:
        if not isinstance(new_registration.cnpj, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ CNPJ deve ser string type.")
            return Response(success=False, message="❌ CNPJ deve ser string type.", data=[])
        if not isinstance(new_registration.seller, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Vendedor deve ser string type.")
            return Response(success=False, message="❌ Vendedor deve ser string type.", data=[])
        if not isinstance(new_registration.email, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ E-mail deve ser string type.")
            return Response(success=False, message="❌ E-mail deve ser string type.", data=[])
        if not isinstance(new_registration.cpf, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ CPF deve ser string type.")
            return Response(success=False, message="❌ CPF deve ser string type.", data=[])
        if not isinstance(new_registration.cpf_person, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Representante legal deve ser string type.")
            return Response(success=False, message="❌ Representante legal deve ser string type.", data=[])
        if not isinstance(new_registration.tax_regime, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Regime tributário deve ser string type.")
            return Response(success=False, message="❌ Regime tributário deve ser string type.", data=[])
        if not isinstance(new_registration.client_type, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Tipo do cliente deve ser string type.")
            return Response(success=False, message="❌ Tipo do cliente deve ser string type.", data=[])
        if new_registration.suggested_limit:
            if not isinstance(new_registration.suggested_limit, float):
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Limite sugerido deve ser float type.")
                return Response(success=False, message="❌ Limite sugerido deve ser float type.", data=[])
    
    def _verify_data_on_create(self, new_registration: NewRegistration) -> Response | None:
        new_registration.cnpj = "".join(number for number in new_registration.cnpj if number.isdigit())
        if len(new_registration.cnpj) != 14:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ CNPJ ({new_registration.cnpj}) inválido.")
            return Response(success=False, message="❌ CNPJ inválido.", data=[])
        new_registration.cpf = "".join(number for number in new_registration.cpf if number.isdigit())
        if len(new_registration.cpf) != 11:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ CPF ({new_registration.cpf}) inválido.")
            return Response(success=False, message="❌ CPF inválido.", data=[])
        if not "@" in new_registration.email or not "." in new_registration.email:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ E-mail inválido.")
            return Response(success=False, message="❌ E-mail inválido.", data=[])
        if new_registration.tax_regime not in ["SIMPLES", "CUMULATIVO", "NÃO CUMULATIVO"]:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Regime tributário deve ser: SIMPLES, CUMULATIVO ou NÃO CUMULATIVO.")
            return Response(success=False, message="❌ Regime tributário deve ser: SIMPLES, CUMULATIVO ou NÃO CUMULATIVO.", data=[])
        if new_registration.client_type not in ["REVENDA", "MINHA EMPRESA"]:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Tipo do cliente deve ser: REVENDA ou MINHA EMPRESA.")
            return Response(success=False, message="❌ Tipo do cliente deve ser: REVENDA ou MINHA EMPRESA.", data=[])
    
    def _sanitize_on_create(self, new_registration: NewRegistration) -> NewRegistration:
        new_registration.seller = new_registration.seller.upper()
        new_registration.email = new_registration.email.lower()
        new_registration.cpf_person = new_registration.cpf_person.upper()
        return new_registration

    def _verify_not_nullables_on_update(self, registration_data: RegistrationData) -> Response | None:
        if not registration_data.cnpj:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o CNPJ.")
            return Response(success=False, message="❌ Preencha o CNPJ.", data=[])
        if not registration_data.opening:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a data de abertura.")
            return Response(success=False, message="❌ Preencha a data de abertura.", data=[])
        if not registration_data.company_name:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a razão social.")
            return Response(success=False, message="❌ Preencha a razão social.", data=[])
        if not registration_data.trade_name:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o nome fantasia.")
            return Response(success=False, message="❌ Preencha o nome fantasia.", data=[])
        if not registration_data.legal_nature:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a natureza jurídica.")
            return Response(success=False, message="❌ Preencha a natureza jurídica.", data=[])
        if not registration_data.legal_nature_id:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o ID da natureza jurídica.")
            return Response(success=False, message="❌ Preencha o ID da natureza jurídica.", data=[])
        if not registration_data.registration_status:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o status.")
            return Response(success=False, message="❌ Preencha o status.", data=[])
        if not registration_data.street:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a rua.")
            return Response(success=False, message="❌ Preencha a rua.", data=[])
        if not registration_data.number:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o número do endereço.")
            return Response(success=False, message="❌ Preencha o número do endereço.", data=[])
        if not registration_data.complement:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o complemento.")
            return Response(success=False, message="❌ Preencha o complemento.", data=[])
        if not registration_data.neighborhood:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o bairro.")
            return Response(success=False, message="❌ Preencha o bairro.", data=[])
        if not registration_data.pac:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o CEP.")
            return Response(success=False, message="❌ Preencha o CEP.", data=[])
        if not registration_data.city:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a cidade.")
            return Response(success=False, message="❌ Preencha a cidade.", data=[])
        if not registration_data.state:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o estado.")
            return Response(success=False, message="❌ Preencha o estado.", data=[])
        if not registration_data.fone:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o número de telefone.")
            return Response(success=False, message="❌ Preencha o número de telefone.", data=[])
        if not registration_data.email:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o e-mail.")
            return Response(success=False, message="❌ Preencha o e-mail.", data=[])
        if not registration_data.tax_regime:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o regime tributário.")
            return Response(success=False, message="❌ Preencha o regime tributário.", data=[])
        if not registration_data.comission_receipt:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o recebimento de comissão.")
            return Response(success=False, message="❌ Preencha o recebimento de comissão.", data=[])
        if not registration_data.status:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o status.")
            return Response(success=False, message="❌ Preencha o status.", data=[])
        if not registration_data.client_type:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o tipo do cliente.")
            return Response(success=False, message="❌ Preencha o tipo do cliente.", data=[])
        if not registration_data.suggested_limit:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o limite sugerido.")
            return Response(success=False, message="❌ Preencha o limite sugerido.", data=[])
        if not registration_data.seller:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o vendedor.")
            return Response(success=False, message="❌ Preencha o vendedor.", data=[])
        if not registration_data.cpf:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o CPF.")
            return Response(success=False, message="❌ Preencha o CPF.", data=[])
        if not registration_data.cpf_person:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o representante legal.")
            return Response(success=False, message="❌ Preencha o representante legal.", data=[])
    
    def _verify_types_on_update(self, registration_data: RegistrationData) -> Response | None:
        if not isinstance(registration_data.cnpj, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ CNPJ deve ser string type.")
            return Response(success=False, message="❌ CNPJ deve ser string type.", data=[])
        if not isinstance(registration_data.opening, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Data de abertura deve ser string type.")
            return Response(success=False, message="❌ Data de abertura deve ser string type.", data=[])
        if not isinstance(registration_data.company_name, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Razão social deve ser string type.")
            return Response(success=False, message="❌ Razão social deve ser string type.", data=[])
        if not isinstance(registration_data.trade_name, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Nome fantasia deve ser string type.")
            return Response(success=False, message="❌ Nome fantasia deve ser string type.", data=[])
        if not isinstance(registration_data.legal_nature, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Natureza jurídica deve ser string type.")
            return Response(success=False, message="❌ Natureza jurídica deve ser string type.", data=[])
        if not isinstance(registration_data.legal_nature_id, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ ID da natureza jurídica deve ser string type.")
            return Response(success=False, message="❌ ID da natureza jurídica deve ser string type.", data=[])
        if not isinstance(registration_data.registration_status, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Status deve ser string type.")
            return Response(success=False, message="❌ Status deve ser string type.", data=[])
        if not isinstance(registration_data.street, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Rua deve ser string type.")
            return Response(success=False, message="❌ Rua deve ser string type.", data=[])
        if not isinstance(registration_data.number, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Número do endereço deve ser string type.")
            return Response(success=False, message="❌ Número do endereço deve ser string type.", data=[])
        if not isinstance(registration_data.complement, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Complemento deve ser string type.")
            return Response(success=False, message="❌ Complemento deve ser string type.", data=[])
        if not isinstance(registration_data.neighborhood, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Bairro deve ser string type.")
            return Response(success=False, message="❌ Bairro deve ser string type.", data=[])
        if not isinstance(registration_data.pac, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ CEP deve ser string type.")
            return Response(success=False, message="❌ CEP deve ser string type.", data=[])
        if not (registration_data.city, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Cidade deve ser string type.")
            return Response(success=False, message="❌ Cidade deve ser string type.", data=[])
        if not isinstance(registration_data.state, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Estado deve ser string type.")
            return Response(success=False, message="❌ Estado deve ser string type.", data=[])
        if not isinstance(registration_data.fone, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Número de telefone deve ser string type.")
            return Response(success=False, message="❌ Número de telefone deve ser string type.", data=[])
        if not isinstance(registration_data.email, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ E-mail deve ser string type.")
            return Response(success=False, message="❌ E-mail deve ser string type.", data=[])
        if not isinstance(registration_data.tax_regime, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Regime tributário deve ser string type.")
            return Response(success=False, message="❌ Regime tributário deve ser string type.", data=[])
        if not isinstance(registration_data.comission_receipt, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Recebimento de comissão deve ser string type.")
            return Response(success=False, message="❌ Recebimento de comissão deve ser string type.", data=[])
        if not isinstance(registration_data.status, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Status deve ser string type.")
            return Response(success=False, message="❌ Status deve ser string type.", data=[])
        if not isinstance(registration_data.client_type, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Tipo do cliente deve ser string type.")
            return Response(success=False, message="❌ Tipo do cliente deve ser string type.", data=[])
        if not isinstance(registration_data.suggested_limit, float):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Limite sugerido deve ser float type.")
            return Response(success=False, message="❌ Limite sugerido deve ser float type.", data=[])
        if not isinstance(registration_data.seller, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Vendedor deve ser string type.")
            return Response(success=False, message="❌ Vendedor deve ser string type.", data=[])
        if not isinstance(registration_data.cpf, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ CPF deve ser string type.")
            return Response(success=False, message="❌ CPF deve ser string type.", data=[])
        if not isinstance(registration_data.cpf_person, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Representante legal deve ser string type.")
            return Response(success=False, message="❌ Representante legal deve ser string type.", data=[])
    
    def _verify_data_on_update(self, registration_data: RegistrationData) -> Response | None:
        registration_data.cnpj = "".join(number for number in registration_data.cnpj if number.isdigit())
        if len(registration_data.cnpj) != 14:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ CNPJ ({registration_data.cnpj}) inválido.")
            return Response(success=False, message="❌ CNPJ inválido.", data=[])
        is_date = self.date_utility.is_date(registration_data.opening)
        if not is_date:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Data deve ser no formato (dd/mm/aaaa).")
            return Response(success=False, message="❌ Data deve ser no formato (dd/mm/aaaa).", data=[])
        if not registration_data.status in ["Cadastrar", "Aguardando Assinatura", "Erro"]:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Status deve ser: Cadastrar, Aguardando Assinatura ou Erro.")
            return Response(success=False, message="❌ Status deve ser: Cadastrar, Aguardando Assinatura ou Erro.", data=[])
    
    def create(self, new_registration: NewRegistration) -> Response:
        try:
            response = self._verify_not_nullables_on_create(new_registration)
            if response:
                return response
            response = self._verify_types_on_create(new_registration)
            if response:
                return response
            response = self._verify_data_on_create(new_registration)
            if response:
                return response
            new_registration = self._sanitize_on_create(new_registration)
            registration_exists = self.database_handler.registrations_client.read(new_registration.cnpj)
            if registration_exists:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Tentativa de inclusão de cadastro já existente ({new_registration.cnpj}).")
                return Response(success=False, message="❌ Tentativa de inclusão de cadastro já existente ({new_registration.cnpj}).", data=[])
            federal_revenue_data = self.federal_revenue_api.get_data(new_registration.cnpj)
            self.database_handler.registrations_client.create(
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
                doc_resent=False,
                client_type=new_registration.client_type,
                suggested_limit=new_registration.suggested_limit if new_registration.suggested_limit else 0.0,
                seller=new_registration.seller,
                cpf=new_registration.cpf,
                cpf_person=new_registration.cpf_person
            )
            for ncea in federal_revenue_data.ncea:
                self.database_handler.nceas_client.create(
                    cnpj=new_registration.cnpj,
                    ncea=ncea["code"],
                    description=ncea["description"]
                )
            for state_registration in federal_revenue_data.state_registrations:
                self.database_handler.state_registrations_client.create(
                    cnpj=new_registration.cnpj,
                    state_registration=state_registration["state_registration"],
                    status=state_registration["status"]
                )
            for suframa_registration in federal_revenue_data.suframa_registrations:
                self.database_handler.suframa_registrations_client.create(
                    cnpj=new_registration.cnpj,
                    suframa_registration=suframa_registration["suframa_registration"],
                    status=suframa_registration["status"]
                )
            doc_list = [new_registration.article_association_doc]
            if new_registration.bank_doc:
                doc_list.append(new_registration.bank_doc)
            self.docs_handler.save_docs(cnpj=new_registration.cnpj, docs=doc_list)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Novo cadastro incluído com sucesso ({new_registration.cnpj}).")
            return Response(success=True, message=f"✅ Novo cadastro incluído com sucesso ({new_registration.cnpj}).", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao incluir novo cadastro. Contate o administrador.")
    
    def delete(self, cnpj: str) -> Response:
        try:
            registration_exists = self.database_handler.registrations_client.read(cnpj)
            if registration_exists == None:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar cadastro: ❌ Cadastro ({cnpj}) não existe.")
                return Response(success=False, message=f"❌ Cadastro ({cnpj}) não existe.", data=[])
            self.database_handler.registrations_client.delete(cnpj)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar usuário: ✅ Cadastro ({cnpj}) removido.")
            return Response(success=True, message=f"✅ Cadastro ({cnpj}) removido.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar usuário: ❌ Erro: {error}")
            raise Exception(f"❌ Erro interno ao deletar cadastro ({cnpj}). Contate o administrador.")
    
    def get(self, cnpj: str) -> Response:
        try:
            if cnpj == "all":
                registrations = self.database_handler.registrations_client.read_all()    
            else:
                registrations = self.database_handler.registrations_client.read(cnpj)
            if isinstance(registrations, list):
                registrations_serialized = self.serializer.serialize_list(registrations)
            elif not registrations:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Cadastro ({cnpj}) não existe.")
                return Response(success=False, message=f"❌ Cadastro ({cnpj}) não existe.", data=[])
            else:
                registrations_serialized = [self.serializer.serialize(registrations)]
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Cadastro(s) coletado(s) com sucesso.")
            return Response(success=True, message="✅ Cadastro(s) coletado(s) com sucesso.", data=registrations_serialized)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao coletar cadastros. Contate o administrador.")
    
    def update(self, registration_data: RegistrationData) -> Response:
        try:
            response = self._verify_not_nullables_on_update(registration_data)
            if response:
                return response
            response = self._verify_types_on_update(registration_data)
            if response:
                return response
            response = self._verify_data_on_update(registration_data)
            if response:
                return response
            registration_exists = self.database_handler.registrations_client.read(registration_data.cnpj)
            if registration_exists == None:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Cadastro não existe.")
                return Response(success=False, message="❌ Usuário não existe.", data=[])
            if registration_exists.opening == registration_data.opening \
                and registration_exists.company_name == registration_data.company_name \
                and registration_exists.trade_name == registration_data.trade_name \
                and registration_exists.legal_nature == registration_data.legal_nature \
                and registration_exists.legal_nature_id == registration_data.legal_nature_id \
                and registration_exists.registration_status == registration_data.registration_status \
                and registration_exists.street == registration_data.street \
                and registration_exists.number == registration_data.number \
                and registration_exists.complement == registration_data.complement \
                and registration_exists.neighborhood == registration_data.neighborhood \
                and registration_exists.pac == registration_data.pac \
                and registration_exists.city == registration_data.city \
                and registration_exists.state == registration_data.state \
                and registration_exists.fone == registration_data.fone \
                and registration_exists.email == registration_data.email \
                and registration_exists.tax_regime == registration_data.tax_regime \
                and registration_exists.comission_receipt == registration_data.comission_receipt \
                and registration_exists.status == registration_data.status \
                and registration_exists.client_type == registration_data.client_type \
                and registration_exists.suggested_limit == registration_data.suggested_limit \
                and registration_exists.seller == registration_data.seller \
                and registration_exists.cpf == registration_data.cpf \
                and registration_exists.cpf_person == registration_data.cpf_person:
                    self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ⚠️ Nenhum dado do cadastro ({registration_data.cnpj}) modificado.")
                    return Response(success=True, message="⚠️ Nenhum dado do cadastro modificado.", data=[])
            self.database_handler.registrations_client.update(
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
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Cadastro ({registration_data.cnpj}) atualizado.")
            return Response(success=True, message="✅ Cadastro atualizado.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao atualizar cadastro. Contate o administrador.")
