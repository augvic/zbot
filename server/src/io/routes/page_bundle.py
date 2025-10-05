from flask import Blueprint, Response
from flask.views import MethodView
from src.tasks.send_page import SendPage
from src.tasks.verify_if_user_is_in_session import VerifyIfUserIsInSession

page_bundle = Blueprint("page_bundle", __name__)

class PageBundle(MethodView):
    
    def get(self, page: str) -> tuple[str, int] | Response | str:
        task1 = VerifyIfUserIsInSession()
        if page == "zindex.js":
            if not task1.execute():
                return "Necessário logar.", 401
        task2 = SendPage()
        return task2.execute(page)
        
page_bundle.add_url_rule("/page-bundle/<page>", view_func=PageBundle.as_view("page_bundle"), methods=["GET"])
