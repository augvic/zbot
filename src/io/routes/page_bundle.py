from flask import Flask, Response
from src.tasks import SendPage

class PageBundle:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/page-bundle/<page>", methods=["GET"])
        def get_page_bundle(page: str) -> Response:
            task = SendPage()
            return task.execute(page)