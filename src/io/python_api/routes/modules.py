from flask import Flask, Response
from src.tasks import SendModule

class Modules:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/modules/<path:module>", methods=["GET"])
        def get_modules(module) -> Response:
            task = SendModule()
            return task.execute(module)
