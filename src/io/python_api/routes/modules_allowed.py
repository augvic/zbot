from flask import Flask
from src.tasks import GetModulesAllowed

class ModulesAllowed:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/modules-allowed", methods=["GET"])
        def get_modules_allowed() -> dict:
            task = GetModulesAllowed()
            return task.execute()
