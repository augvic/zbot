from flask import Blueprint
from flask.views import MethodView
from src.tasks.verify_if_user_is_in_session import VerifyIfUserIsInSession
from src.tasks.get_session_user import GetSessionUser

session_user = Blueprint("session_user", __name__)

class SessionUser(MethodView):
    
    def get(self) -> tuple[str, int] | list[str]:
        task1 = VerifyIfUserIsInSession()
        task2 = GetSessionUser()
        if not task1.execute():
            return "Faça login.", 401
        return task2.execute()

session_user.add_url_rule("/session-user", view_func=SessionUser.as_view("session_user"), methods=["GET"])
