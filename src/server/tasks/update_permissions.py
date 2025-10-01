from src.server.infrastructure.drivers.databases.production.clients import UsersClient, PermissionsClient
from src.server.infrastructure.managers import SessionManager

class UpdatePermissions:
    
    def _setup(self) -> None:
        self.users_client = UsersClient()
        self.permissions_client = PermissionsClient()
        self.session_manager = SessionManager()
    
    def execute(self, user: str, permissions: list) -> dict | str:
        self._setup()
        if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access("zAdmin"):
            return "Sem autorização.", 401
        user_exists = self.users_client.read(user)
        if not user_exists:
            return {"success": False, "message": "Usuário não existe."}
        current_permissions = self.permissions_client.read(user)
        current_permissions_list = []
        for current_permission in current_permissions:
            current_permissions_list.append(current_permission.module)
        for permission in permissions:
            if not permission in current_permissions_list:
                self.permissions_client.create(user, permission)
        return {"success": True, "message": "Permissões atualizadas."}
