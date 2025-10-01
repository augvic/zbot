from flask import Flask
from src.server.tasks import GetModulesList

class ModulesList:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/modules-list", methods=["GET"])
        def get_modules_list() -> dict | str:
            task = GetModulesList()
            return task.execute()
