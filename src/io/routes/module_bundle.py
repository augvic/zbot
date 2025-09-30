from flask import Flask, Response
from src.tasks import SendModule

class ModuleBundle:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/module-bundle/<module>", methods=["GET"])
        def get_module_bundle(module) -> Response:
            task = SendModule()
            return task.execute(module)
