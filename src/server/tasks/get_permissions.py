from src.server.infrastructure.drivers.databases.production.clients import PermissionsClient
from src.server.infrastructure.drivers.databases import Serializer
from src.server.infrastructure.managers import SessionManager

class GetPermissions:
    
    def _setup(self) -> None:
        self.permissions_client = PermissionsClient()
        self.session_manager = SessionManager()
        self.serializer = Serializer()
    
    def execute(self, user: str) -> dict | str:
        self._setup()
        if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access("zAdmin"):
            return "Sem autorização.", 401
        permissions = self.permissions_client.read(user)
        permissions_serialized = self.serializer.serialize_list(permissions)
        return permissions_serialized
