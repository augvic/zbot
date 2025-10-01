from src.server.infrastructure.drivers.databases.production.clients import UsersClient
from src.server.infrastructure.drivers.databases import Serializer
from src.server.infrastructure.managers import SessionManager

class GetUsers:
    
    def _setup(self) -> None:
        self.users_client = UsersClient()
        self.session_manager = SessionManager()
        self.serializer = Serializer()
    
    def execute(self, user: str) -> dict | str:
        self._setup()
        if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access("zAdmin"):
            return "Sem autorização.", 401
        users = self.users_client.read(user)
        if isinstance(users, list):
            users_serialized = self.serializer.serialize_list(users)
        else:
            users_serialized = self.serializer.serialize(users)
        return users_serialized
