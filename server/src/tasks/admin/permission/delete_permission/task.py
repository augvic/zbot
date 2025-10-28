from src.components.database_clients.clients.users_client import UsersClient
from src.components.database_clients.clients.permissions_client import PermissionsClient
from src.components.session_manager import SessionManager
from src.components.log_system import LogSystem
from .models import Response

class DeletePermission:
    
    def __init__(self) -> None:
        self.users_client = UsersClient("prd")
        self.permissions_client = PermissionsClient("prd")
        self.session_manager = SessionManager()
        self.log_system = LogSystem("admin")
    
    def execute(self, user: str, permission: str) -> Response:
        try:
            permission_exists = self.users_client.read(user)
            if permission_exists == None:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao deletar permissão).\n❌ Permissão ({permission}) não existe.")
                return Response(success=False, message=f"❌ Permissão ({permission}) não existe.")
            if user == "72776" and permission == "zAdmin":
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao deletar permissão).\n❌ Permissão zAdmin do 72776 não pode ser removida.")
                return Response(success=False, message="❌ Permissão zAdmin do 72776 não pode ser removida.")
            self.permissions_client.delete_from_user(user, permission)
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao deletar permissão).\n✅ Permissão ({permission}) removida.")
            return Response(success=True, message=f"✅ Permissão ({permission}) removida.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao deletar permissão).\n❌ Erro:\n{error}")
            raise Exception(f"❌ Erro interno ao deletar permissão ({permission}). Contate o administrador.")
