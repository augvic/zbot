from flask import Blueprint
from flask.views import MethodView
from src.tasks.verify_if_user_is_in_session import VerifyIfUserIsInSession
from src.tasks.get_session_modules import GetSessionModules

session_modules = Blueprint("session_modules", __name__)

class SessionModules(MethodView):
    
    def get(self) -> tuple[str, int] | list[str]:
        task1 = VerifyIfUserIsInSession()
        task2 = GetSessionModules()
        if not task1.execute():
            return "Faça login.", 401
        return task2.execute()

session_modules.add_url_rule("/session-modules", view_func=SessionModules.as_view("session-modules"), methods=["GET"])
