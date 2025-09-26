from src.infrastructure.drivers.databases.production.clients import UsersClient, PermissionsClient
from src.infrastructure.file_systems import SessionManager

class DeletePermission:
    
    def _setup(self) -> None:
        self.users_client = UsersClient()
        self.permissions_client = PermissionsClient()
        self.session_manager = SessionManager()
    
    def execute(self, user: str, module: str) -> dict | str:
        self._setup()
        if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access("zAdmin"):
            return "Sem autorização.", 401
        user_exists = self.users_client.read(user)
        if not user_exists:
            return {"success": False, "message": "Usuário não existe."}
        self.permissions_client.delete(user, module)
        return {"success": True, "message": "Permissão removida."}
