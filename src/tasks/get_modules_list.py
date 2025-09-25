from src.infrastructure.drivers.databases.production.clients import ModulesClient
from src.infrastructure.drivers.databases import Serializer
from src.infrastructure.file_systems import SessionManager

class GetModulesList:
    
    def _setup(self) -> None:
        self.modules_client = ModulesClient()
        self.session_manager = SessionManager()
        self.serializer = Serializer()
    
    def execute(self) -> dict | str:
        self._setup()
        if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access("zusers"):
            return "Sem autorização.", 401
        modules = self.modules_client.read("all")
        modules_serialized = self.serializer.serialize_list(modules)
        return modules_serialized
