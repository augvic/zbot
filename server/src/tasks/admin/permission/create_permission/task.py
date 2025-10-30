from src.components.infra.database_clients.clients.users_client import UsersClient
from src.components.infra.database_clients.clients.permissions_client import PermissionsClient
from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class CreatePermission:
    
    def __init__(self) -> None:
        self.users_client = UsersClient("prd")
        self.permissions_client = PermissionsClient("prd")
        self.session_manager = SessionManager()
        self.log_system = LogSystem("admin/permission")
    
    def execute(self, user: str, permission: str) -> Response:
        try:
            user_exists = self.users_client.read(user)
            if not user_exists:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao criar permissão).\n❌ Usuário não existe.")
                return Response(success=False, message="❌ Usuário não existe.")
            self.permissions_client.create(user, permission)
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao criar permissão).\n✅ Permissão ({permission}) adicionada.")
            return Response(success=True, message=f"✅ Permissão ({permission}) adicionada.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao criar permissão).\n❌ Erro:\n{error}")
            raise Exception(f"❌ Erro interno ao adicionar permissão ({permission}). Contate o administrador.")
