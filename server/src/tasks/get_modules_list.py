from src.components.database_clients.clients.modules_client import ModulesClient
from src.components.sqla_serializer import SqlaSerializer
from src.components.session_manager import SessionManager
from datetime import datetime

class GetModulesList:
    
    def __init__(self) -> None:
        self.modules_client = ModulesClient("prd")
        self.session_manager = SessionManager()
        self.serializer = SqlaSerializer()
    
    def execute(self) -> dict[str, str | bool | list[dict[str, str]]]:
        try:
            modules = self.modules_client.read_all()
            modules_serialized = self.serializer.serialize_list(modules)
            return {"success": True, "modules": modules_serialized}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": "Erro ao coletar lista de módulos."}
