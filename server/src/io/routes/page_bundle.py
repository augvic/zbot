from flask import Flask, Response
from src.tasks import SendPage

class PageBundle:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/page-bundle/<page>", methods=["GET"])
        def get_page_bundle(page: str) -> Response:
            if page == "zindex.js":
                if not self.session_manager.is_user_in_session():
                    return "Necessário logar.", 401
            task = SendPage()
            return task.execute(page)