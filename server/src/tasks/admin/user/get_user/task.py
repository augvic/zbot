from src.components.infra.database_clients.clients.users_client import UsersClient
from src.components.adapter.sqla_serializer import SqlaSerializer
from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class GetUser:
    
    def __init__(self) -> None:
        self.users_client = UsersClient("prd")
        self.session_manager = SessionManager()
        self.serializer = SqlaSerializer()
        self.log_system = LogSystem("admin/user")
    
    def execute(self, user: str) -> Response:
        try:
            if user == "all":
                users = self.users_client.read_all()    
            else:
                users = self.users_client.read(user)
            if isinstance(users, list):
                users_serialized = self.serializer.serialize_list(users)
            else:
                users_serialized = [self.serializer.serialize(users)]
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}. ✅ Usuário coletado com sucesso: {users_serialized}.")
            return Response(success=True, message="✅ Usuário coletado com sucesso: {users_serialized}.", data=users_serialized)
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Erro:\n{error}")
            raise Exception("❌ Erro interno ao coletar usuários. Contate o administrador.")
