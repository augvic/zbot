from src.infrastructure.databases.production.clients.users_client import UsersClient
from src.infrastructure.serializers.sqla_serializer import SqlaSerializer
from src.io.session_manager import SessionManager
from datetime import datetime

class GetUsers:
    
    def _setup(self) -> None:
        self.users_client = UsersClient()
        self.session_manager = SessionManager()
        self.serializer = SqlaSerializer()
    
    def execute(self, user: str) -> dict[str, str | bool | dict[str, str] | list[dict[str, str]]]:
        self._setup()
        try:
            users = self.users_client.read(user)
            if isinstance(users, list):
                users_serialized = self.serializer.serialize_list(users)
            else:
                users_serialized = self.serializer.serialize(users)
            return {"success": True, "users": users_serialized}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": "Erro ao coletar usuários."}
