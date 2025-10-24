from src.components.database_clients.clients.modules_client import ModulesClient
from src.components.session_manager import SessionManager
from datetime import datetime

class CreateModule:
    
    def __init__(self) -> None:
        self.modules_client = ModulesClient("prd")
        self.session_manager = SessionManager()
    
    def execute(self, data: dict[str, str]) -> dict[str, str | bool]:
        try:
            if data["module"] == "":
                return {"success": False, "message": "Preencha o módulo."}
            if self.modules_client.read(data["module"]):
                return {"success": False, "message": f"Módulo ({data["module"]}) já existe."}
            if data["description"] == "":
                return {"success": False, "message": "Preencha a descrição."}
            self.modules_client.create(data["module"], data["description"])
            return {"success": True, "message": f"Módulo ({data["module"]}) adicionado."}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": f"Erro ao criar módulo ({data["module"]})."}
