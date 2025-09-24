from src.infrastructure.drivers.databases.production.clients import UsersClient
from src.infrastructure.drivers.databases import Serializer
from src.infrastructure.file_systems import SessionManager

class GetAllUsers:
    
    def _setup(self) -> None:
        self.users_client = UsersClient()
        self.session_manager = SessionManager()
        self.serializer = Serializer()
    
    def execute(self, user: str) -> dict | str:
        self._setup()
        if self.session_manager.have_user_module_access("zusers"):
            users = self.users_client.read(user)
            users_dict = self.serializer.serialize_list(users)
            return users_dict
        else:
            return "Sem autorização", 401
