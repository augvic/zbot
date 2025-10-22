from src.components.database.clients.users_client import UsersClient
from src.components.database.clients.permissions_client import PermissionsClient
from src.components.session_manager import SessionManager
from datetime import datetime

class CreatePermission:
    
    def __init__(self) -> None:
        self.users_client = UsersClient("prd")
        self.permissions_client = PermissionsClient("prd")
        self.session_manager = SessionManager()
    
    def execute(self, user: str, permission: str) -> dict[str, str | bool]:
        try:
            user_exists = self.users_client.read(user)
            if not user_exists:
                return {"success": False, "message": "Usuário não existe."}
            self.permissions_client.create(user, permission)
            return {"success": True, "message": f"Permissão ({permission}) adicionada."}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": f"Error ao adicionar permissão ({permission})."}
