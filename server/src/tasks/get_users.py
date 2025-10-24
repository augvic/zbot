from src.components.database_clients.clients.users_client import UsersClient
from src.components.sqla_serializer import SqlaSerializer
from src.components.session_manager import SessionManager
from datetime import datetime

class GetUsers:
    
    def __init__(self) -> None:
        self.users_client = UsersClient("prd")
        self.session_manager = SessionManager()
        self.serializer = SqlaSerializer()
    
    def execute(self, user: str) -> dict[str, str | bool | dict[str, str] | list[dict[str, str]]]:
        try:
            if user == "all":
                users = self.users_client.read_all()    
            else:
                users = self.users_client.read(user)
            if isinstance(users, list):
                users_serialized = self.serializer.serialize_list(users)
            else:
                users_serialized = self.serializer.serialize(users)
            return {"success": True, "users": users_serialized}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": "Erro ao coletar usuários."}
