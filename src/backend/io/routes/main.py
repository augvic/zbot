from flask import Flask
from src.backend.tasks import RenderTemplate

class Main:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> str:
        @self.app.route("/", methods=["GET"])
        def get_main() -> str:
            task = RenderTemplate()
            return task.execute("base.html")
