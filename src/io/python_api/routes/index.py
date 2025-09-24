from flask import Flask, Response
from src.tasks import SendIndex

class Index:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/zindex", methods=["GET"])
        def get_index() -> Response:
            task = SendIndex()
            return task.execute()