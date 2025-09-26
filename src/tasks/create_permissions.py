from src.infrastructure.drivers.databases.production.clients import UsersClient, PermissionsClient
from src.infrastructure.file_systems import SessionManager

class CreatePermissions:
    
    def _setup(self) -> None:
        self.users_client = UsersClient()
        self.permissions_client = PermissionsClient()
        self.session_manager = SessionManager()
    
    def execute(self, user: str, permissions: list) -> dict | str:
        self._setup()
        if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access("zAdmin"):
            return "Sem autorização.", 401
        user = self.users_client.read(user)
        if not user:
            return {"success": False, "message": "Usuário não existe."}
        for permission in permissions:
            self.permissions_client.create(user, permission)
        return {"success": True, "message": "Permissões criadas."}
