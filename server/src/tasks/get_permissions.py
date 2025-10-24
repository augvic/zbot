from src.components.database_clients.clients.permissions_client import PermissionsClient
from src.components.sqla_serializer import SqlaSerializer
from src.components.session_manager import SessionManager
from datetime import datetime

class GetPermissions:
    
    def __init__(self) -> None:
        self.permissions_client = PermissionsClient("prd")
        self.session_manager = SessionManager()
        self.serializer = SqlaSerializer()
    
    def execute(self, user: str) -> dict[str, str | bool | list[dict[str, str]]]:
        try:
            permissions = self.permissions_client.read_all_from_user(user)
            permissions_serialized = self.serializer.serialize_list(permissions)
            return {"success": True, "permissions": permissions_serialized}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": "Erro ao coletar permissões."}
