from src.components.infra.database_clients.clients.registrations_client import RegistrationsClient
from src.components.adapter.sqla_serializer import SqlaSerializer
from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class GetRegistration:
    
    def __init__(self,
        registrations_client: RegistrationsClient,
        session_manager: SessionManager,
        serializer: SqlaSerializer,
        log_system: LogSystem
    ) -> None:
        self.registrations_client = registrations_client
        self.session_manager = session_manager
        self.serializer = serializer
        self.log_system = log_system
    
    def execute(self, cnpj: str) -> Response:
        try:
            if cnpj == "all":
                registrations = self.registrations_client.read_all()    
            else:
                registrations = self.registrations_client.read(cnpj)
            if isinstance(registrations, list):
                registrations_serialized = self.serializer.serialize_list(registrations)
            elif not registrations:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Cadastro ({cnpj}) não existe.")
                return Response(success=False, message=f"❌ Cadastro ({cnpj}) não existe.", data=[{}])
            else:
                registrations_serialized = [self.serializer.serialize(registrations)]
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ✅ Cadastro(s) coletado(s) com sucesso.")
            return Response(success=True, message="✅ Cadastro(s) coletado(s) com sucesso.", data=registrations_serialized)
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao coletar cadastros. Contate o administrador.")
