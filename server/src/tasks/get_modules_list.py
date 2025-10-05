from src.infrastructure.databases.production.clients.modules_client import ModulesClient
from src.infrastructure.serializers.sqla_serializer import SqlaSerializer
from src.infrastructure.session_manager import SessionManager
from datetime import datetime

class GetModulesList:
    
    def _setup(self) -> None:
        self.modules_client = ModulesClient()
        self.session_manager = SessionManager()
        self.serializer = SqlaSerializer()
    
    def execute(self) -> dict[str, str | bool | list[dict[str, str]]]:
        self._setup()
        try:
            modules = self.modules_client.read()
            modules_serialized = self.serializer.serialize_list(modules)
            return {"success": True, "modules_list": modules_serialized}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": "Erro ao coletar lista de módulos."}
