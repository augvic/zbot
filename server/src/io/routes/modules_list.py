from flask import Flask
from src.tasks import GetModulesList

class ModulesList:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/modules-list", methods=["GET"])
        def get_modules_list() -> dict | str:
            if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access("zAdmin"):
                return "Sem autorização.", 401
            task = GetModulesList()
            return task.execute()
