from src.modules.infra.database_clients.clients.users_client import UsersClient
from src.modules.sqla_serializer import SqlaSerializer
from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from .models import Response

class GetUser:
    
    def __init__(self,
        users_client: UsersClient,
        session_manager: SessionManager,
        serializer: SqlaSerializer,
        log_system: LogSystem
    ) -> None:
        self.users_client = users_client
        self.session_manager = session_manager
        self.serializer = serializer
        self.log_system = log_system
    
    def main(self, user: str) -> Response:
        try:
            if user == "all":
                users = self.users_client.read_all()    
            else:
                users = self.users_client.read(user)
            if isinstance(users, list):
                users_serialized = self.serializer.serialize_list(users)
            elif not users:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Usuário ({user}) não existe.")
                return Response(success=False, message=f"❌ Usuário ({user}) não existe.", data=[{}])
            else:
                users_serialized = [self.serializer.serialize(users)]
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Usuário(s) coletado(s) com sucesso.")
            return Response(success=True, message="✅ Usuário(s) coletado(s) com sucesso.", data=users_serialized)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao coletar usuários. Contate o administrador.")
