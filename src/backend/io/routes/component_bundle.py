from flask import Flask, Response
from src.backend.tasks import SendComponent

class ComponentBundle:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/component-bundle/<component>", methods=["GET"])
        def get_component_bundle(component: str) -> Response:
            task = SendComponent()
            return task.execute(component)