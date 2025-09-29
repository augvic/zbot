from flask import Flask, Response
from src.backend.tasks import SendPage

class Pages:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/pages/<path:page>", methods=["GET"])
        def get_pages(page: str) -> Response:
            task = SendPage()
            return task.execute(page)