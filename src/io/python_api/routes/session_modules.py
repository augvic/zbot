from flask import Flask
from src.tasks import GetSessionModules

class ModulesAllowed:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/session-modules", methods=["GET"])
        def get_session_modules() -> dict:
            task = GetSessionModules()
            return task.execute()
