from flask import Flask, Response
from src.tasks.send_page import SendPage
from src.tasks.verify_if_user_is_in_session import VerifyIfUserIsInSession

class PageBundle:
    
    def __init__(self, app: Flask) -> None:
        
        @app.route("/page-bundle/<page>", methods=["GET"])
        def send_page(page: str) -> tuple[str, int] | Response | str:
            task1 = VerifyIfUserIsInSession()
            if page == "zindex.js":
                if not task1.execute():
                    return "Necessário logar.", 401
            task2 = SendPage()
            return task2.execute(page)
