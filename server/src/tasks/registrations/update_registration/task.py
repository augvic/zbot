from src.components.infra.database_clients.clients.registrations_client import RegistrationsClient
from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class UpdateRegistration:
    
    def __init__(self,
        registrations_client: RegistrationsClient,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.registrations_client = registrations_client
        self.session_manager = session_manager
        self.log_system = log_system
    
    def execute(self,
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
        suggested_limit: str,
        seller: str,
        cpf: str,
        cpf_person: str
    ) -> Response:
        try:
            registration_exists = self.registrations_client.read(cnpj)
            if registration_exists == None:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Cadastro não existe.")
                return Response(success=False, message="❌ Usuário não existe.")
            if not cnpj:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o CNPJ.")
                return Response(success=False, message="❌ Preencha o CNPJ.")
            if not opening:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a data de abertura.")
                return Response(success=False, message="❌ Preencha a data de abertura.")
            if not company_name:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a razão social.")
                return Response(success=False, message="❌ Preencha a razão social.")
            if not trade_name:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o nome fantasia.")
                return Response(success=False, message="❌ Preencha o nome fantasia.")
            if not legal_nature or not legal_nature_id:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a natureza jurídica.")
                return Response(success=False, message="❌ Preencha a natureza jurídica.")
            if not registration_status:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o status.")
                return Response(success=False, message="❌ Preencha o status.")
            if not street:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a rua.")
                return Response(success=False, message="❌ Preencha a rua.")
            if not number:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o número do endereço.")
                return Response(success=False, message="❌ Preencha o número do endereço.")
            if not complement:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o complemento.")
                return Response(success=False, message="❌ Preencha o complemento.")
            if not neighborhood:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o bairro.")
                return Response(success=False, message="❌ Preencha o bairro.")
            if not pac:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o CEP.")
                return Response(success=False, message="❌ Preencha o CEP.")
            if not city:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a cidade.")
                return Response(success=False, message="❌ Preencha a cidade.")
            if not state:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o estado.")
                return Response(success=False, message="❌ Preencha o estado.")
            if not fone:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o número de telefone.")
                return Response(success=False, message="❌ Preencha o número de telefone.")
            if not email:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o e-mail.")
                return Response(success=False, message="❌ Preencha o e-mail.")
            if not tax_regime:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o regime tributário.")
                return Response(success=False, message="❌ Preencha o regime tributário.")
            if not comission_receipt:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o recebimento de comissão.")
                return Response(success=False, message="❌ Preencha o recebimento de comissão.")
            if not status:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o status.")
                return Response(success=False, message="❌ Preencha o status.")
            if not client_type:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o tipo do cliente.")
                return Response(success=False, message="❌ Preencha o tipo do cliente.")
            if not suggested_limit:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o limite sugerido.")
                return Response(success=False, message="❌ Preencha o limite sugerido.")
            if not seller:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o vendedor.")
                return Response(success=False, message="❌ Preencha o vendedor.")
            if not cpf:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o CPF.")
                return Response(success=False, message="❌ Preencha o CPF.")
            if not cpf_person:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o representante legal.")
                return Response(success=False, message="❌ Preencha o representante legal.")
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
                    self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ⚠️ Nenhum dado do cadastro ({cnpj}) modificado.")
                    return Response(success=True, message="⚠️ Nenhum dado do cadastro modificado.")
            self.registrations_client.update(
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
                cpf_person=cpf_person
            )
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ✅ Cadastro ({cnpj}) atualizado.")
            return Response(success=True, message="✅ Cadastro atualizado.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao atualizar cadastro. Contate o administrador.")
