from src.components.infra.database_clients.clients.registrations_client import RegistrationsClient
from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from src.components.gear.date_utility import DateUtility
from .models import Response, RegistrationData

class UpdateRegistration:
    
    def __init__(self,
        registrations_client: RegistrationsClient,
        session_manager: SessionManager,
        log_system: LogSystem,
        date_utility: DateUtility
    ) -> None:
        self.registrations_client = registrations_client
        self.session_manager = session_manager
        self.log_system = log_system
        self.date_utility = date_utility
    
    def _verify_not_nullables(self, registration_data: RegistrationData) -> Response | None:
        if not registration_data.cnpj:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o CNPJ.")
            return Response(success=False, message="❌ Preencha o CNPJ.")
        if not registration_data.opening:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a data de abertura.")
            return Response(success=False, message="❌ Preencha a data de abertura.")
        if not registration_data.company_name:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a razão social.")
            return Response(success=False, message="❌ Preencha a razão social.")
        if not registration_data.trade_name:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o nome fantasia.")
            return Response(success=False, message="❌ Preencha o nome fantasia.")
        if not registration_data.legal_nature:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a natureza jurídica.")
            return Response(success=False, message="❌ Preencha a natureza jurídica.")
        if not registration_data.legal_nature_id:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o ID da natureza jurídica.")
            return Response(success=False, message="❌ Preencha o ID da natureza jurídica.")
        if not registration_data.registration_status:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o status.")
            return Response(success=False, message="❌ Preencha o status.")
        if not registration_data.street:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a rua.")
            return Response(success=False, message="❌ Preencha a rua.")
        if not registration_data.number:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o número do endereço.")
            return Response(success=False, message="❌ Preencha o número do endereço.")
        if not registration_data.complement:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o complemento.")
            return Response(success=False, message="❌ Preencha o complemento.")
        if not registration_data.neighborhood:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o bairro.")
            return Response(success=False, message="❌ Preencha o bairro.")
        if not registration_data.pac:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o CEP.")
            return Response(success=False, message="❌ Preencha o CEP.")
        if not registration_data.city:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a cidade.")
            return Response(success=False, message="❌ Preencha a cidade.")
        if not registration_data.state:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o estado.")
            return Response(success=False, message="❌ Preencha o estado.")
        if not registration_data.fone:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o número de telefone.")
            return Response(success=False, message="❌ Preencha o número de telefone.")
        if not registration_data.email:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o e-mail.")
            return Response(success=False, message="❌ Preencha o e-mail.")
        if not registration_data.tax_regime:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o regime tributário.")
            return Response(success=False, message="❌ Preencha o regime tributário.")
        if not registration_data.comission_receipt:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o recebimento de comissão.")
            return Response(success=False, message="❌ Preencha o recebimento de comissão.")
        if not registration_data.status:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o status.")
            return Response(success=False, message="❌ Preencha o status.")
        if not registration_data.client_type:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o tipo do cliente.")
            return Response(success=False, message="❌ Preencha o tipo do cliente.")
        if not registration_data.suggested_limit:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o limite sugerido.")
            return Response(success=False, message="❌ Preencha o limite sugerido.")
        if not registration_data.seller:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o vendedor.")
            return Response(success=False, message="❌ Preencha o vendedor.")
        if not registration_data.cpf:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o CPF.")
            return Response(success=False, message="❌ Preencha o CPF.")
        if not registration_data.cpf_person:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o representante legal.")
            return Response(success=False, message="❌ Preencha o representante legal.")
    
    def _verify_types(self, registration_data: RegistrationData) -> Response | None:
        if not isinstance(registration_data.cnpj, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ CNPJ deve ser string type.")
            return Response(success=False, message="❌ CNPJ deve ser string type.")
        if not isinstance(registration_data.opening, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Data de abertura deve ser string type.")
            return Response(success=False, message="❌ Data de abertura deve ser string type.")
        if not isinstance(registration_data.company_name, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Razão social deve ser string type.")
            return Response(success=False, message="❌ Razão social deve ser string type.")
        if not isinstance(registration_data.trade_name, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Nome fantasia deve ser string type.")
            return Response(success=False, message="❌ Nome fantasia deve ser string type.")
        if not isinstance(registration_data.legal_nature, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Natureza jurídica deve ser string type.")
            return Response(success=False, message="❌ Natureza jurídica deve ser string type.")
        if not isinstance(registration_data.legal_nature_id, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ ID da natureza jurídica deve ser string type.")
            return Response(success=False, message="❌ ID da natureza jurídica deve ser string type.")
        if not isinstance(registration_data.registration_status, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Status deve ser string type.")
            return Response(success=False, message="❌ Status deve ser string type.")
        if not isinstance(registration_data.street, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Rua deve ser string type.")
            return Response(success=False, message="❌ Rua deve ser string type.")
        if not isinstance(registration_data.number, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Número do endereço deve ser string type.")
            return Response(success=False, message="❌ Número do endereço deve ser string type.")
        if not isinstance(registration_data.complement, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Complemento deve ser string type.")
            return Response(success=False, message="❌ Complemento deve ser string type.")
        if not isinstance(registration_data.neighborhood, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Bairro deve ser string type.")
            return Response(success=False, message="❌ Bairro deve ser string type.")
        if not isinstance(registration_data.pac, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ CEP deve ser string type.")
            return Response(success=False, message="❌ CEP deve ser string type.")
        if not (registration_data.city, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Cidade deve ser string type.")
            return Response(success=False, message="❌ Cidade deve ser string type.")
        if not isinstance(registration_data.state, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Estado deve ser string type.")
            return Response(success=False, message="❌ Estado deve ser string type.")
        if not isinstance(registration_data.fone, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Número de telefone deve ser string type.")
            return Response(success=False, message="❌ Número de telefone deve ser string type.")
        if not isinstance(registration_data.email, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ E-mail deve ser string type.")
            return Response(success=False, message="❌ E-mail deve ser string type.")
        if not isinstance(registration_data.tax_regime, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Regime tributário deve ser string type.")
            return Response(success=False, message="❌ Regime tributário deve ser string type.")
        if not isinstance(registration_data.comission_receipt, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Recebimento de comissão deve ser string type.")
            return Response(success=False, message="❌ Recebimento de comissão deve ser string type.")
        if not isinstance(registration_data.status, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Status deve ser string type.")
            return Response(success=False, message="❌ Status deve ser string type.")
        if not isinstance(registration_data.client_type, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Tipo do cliente deve ser string type.")
            return Response(success=False, message="❌ Tipo do cliente deve ser string type.")
        if not isinstance(registration_data.suggested_limit, float):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Limite sugerido deve ser float type.")
            return Response(success=False, message="❌ Limite sugerido deve ser float type.")
        if not isinstance(registration_data.seller, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Vendedor deve ser string type.")
            return Response(success=False, message="❌ Vendedor deve ser string type.")
        if not isinstance(registration_data.cpf, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ CPF deve ser string type.")
            return Response(success=False, message="❌ CPF deve ser string type.")
        if not isinstance(registration_data.cpf_person, str):
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Representante legal deve ser string type.")
            return Response(success=False, message="❌ Representante legal deve ser string type.")
    
    def _verify_data(self, registration_data: RegistrationData) -> Response | None:
        registration_data.cnpj = "".join(number for number in registration_data.cnpj if number.isdigit())
        if len(registration_data.cnpj) != 14:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ CNPJ ({registration_data.cnpj}) inválido.")
            return Response(success=False, message="❌ CNPJ inválido.")
        is_date = self.date_utility.is_date(registration_data.opening)
        if not is_date:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Data deve ser no formato (dd/mm/aaaa).")
            return Response(success=False, message="❌ Data deve ser no formato (dd/mm/aaaa).")
        if not registration_data.status in ["Cadastrar", "Aguardando Assinatura", "Erro"]:
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Status deve ser: Cadastrar, Aguardando Assinatura ou Erro.")
            return Response(success=False, message="❌ Status deve ser: Cadastrar, Aguardando Assinatura ou Erro.")
    
    def main(self, registration_data: RegistrationData) -> Response:
        try:
            response = self._verify_not_nullables(registration_data)
            if response:
                return response
            response = self._verify_types(registration_data)
            if response:
                return response
            registration_exists = self.registrations_client.read(registration_data.cnpj)
            if registration_exists == None:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Cadastro não existe.")
                return Response(success=False, message="❌ Usuário não existe.")
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
                    return Response(success=True, message="⚠️ Nenhum dado do cadastro modificado.")
            self.registrations_client.update(
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
            return Response(success=True, message="✅ Cadastro atualizado.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao atualizar cadastro. Contate o administrador.")
