from src.components.infra.database_clients.clients.users_client import UsersClient
from src.components.infra.database_clients.clients.permissions_client import PermissionsClient
from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class DeletePermission:
    
    def __init__(self,
        users_client: UsersClient,
        permissions_client: PermissionsClient,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.users_client = users_client
        self.permissions_client = permissions_client
        self.session_manager = session_manager
        self.log_system = log_system
    
    def main(self, user: str, permission: str) -> Response:
        try:
            permission_exists = self.users_client.read(user)
            if permission_exists == None:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar permissão: ❌ Permissão ({permission}) não existe.")
                return Response(success=False, message=f"❌ Permissão ({permission}) não existe.")
            if user == "72776" and permission == "zAdmin":
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar permissão: ❌ Permissão zAdmin do 72776 não pode ser removida.")
                return Response(success=False, message="❌ Permissão zAdmin do 72776 não pode ser removida.")
            self.permissions_client.delete_from_user(user, permission)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar permissão: ✅ Permissão ({permission}) removida.")
            return Response(success=True, message=f"✅ Permissão ({permission}) removida.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar permissão: ❌ Erro: {error}.")
            raise Exception(f"❌ Erro interno ao deletar permissão ({permission}). Contate o administrador.")
