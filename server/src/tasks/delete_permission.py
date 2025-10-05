from src.infrastructure.databases.production.clients.users_client import UsersClient
from src.infrastructure.databases.production.clients.permissions_client import PermissionsClient
from src.io.session_manager import SessionManager
from datetime import datetime

class DeletePermission:
    
    def _setup(self) -> None:
        self.users_client = UsersClient()
        self.permissions_client = PermissionsClient()
        self.session_manager = SessionManager()
    
    def execute(self, user: str, permission: str) -> dict[str, str | bool]:
        self._setup()
        try:
            user_exists = self.users_client.read(user)
            if not user_exists:
                return {"success": False, "message": "Usuário não existe."}
            self.permissions_client.delete(user, permission)
            return {"success": True, "message": "Permissões removidas."}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": "Erro ao deletar permissão."}
