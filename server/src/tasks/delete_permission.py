from src.components.database_clients.clients.users_client import UsersClient
from src.components.database_clients.clients.permissions_client import PermissionsClient
from src.components.session_manager import SessionManager
from datetime import datetime

class DeletePermission:
    
    def __init__(self) -> None:
        self.users_client = UsersClient("prd")
        self.permissions_client = PermissionsClient("prd")
        self.session_manager = SessionManager()
    
    def execute(self, user: str, permission: str) -> dict[str, str | bool]:
        try:
            permission_exists = self.users_client.read(user)
            if permission_exists == None:
                return {"success": False, "message": f"Permissão ({permission}) não existe."}
            if user == "72776" and permission == "zAdmin":
                return {"success": False, "message": "Permissão zAdmin do criador não pode ser removida."}
            self.permissions_client.delete_from_user(user, permission)
            return {"success": True, "message": f"Permissão ({permission}) removida."}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": f"Erro ao deletar permissão ({permission})."}
