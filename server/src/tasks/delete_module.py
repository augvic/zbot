from src.components.database_clients.clients.modules_client import ModulesClient
from src.components.database_clients.clients.permissions_client import PermissionsClient
from src.components.session_manager import SessionManager
from datetime import datetime

class DeleteModule:
    
    def __init__(self) -> None:
        self.modules_client = ModulesClient("prd")
        self.permisssions_client = PermissionsClient("prd")
        self.session_manager = SessionManager()
    
    def execute(self, module: str) -> dict[str, str | bool]:
        try:
            module_exists = self.modules_client.read(module)
            if module_exists == None:
                return {"success": False, "message": f"Módulo ({module}) não existe."}
            if module == "zAdmin":
                return {"success": False, "message": "zAdmin não pode ser removido."}
            self.modules_client.delete(module)
            self.permisssions_client.delete_all(module)
            return {"success": True, "message": f"Módulo ({module}) removido."}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": f"Erro ao deletar módulo ({module})."}
