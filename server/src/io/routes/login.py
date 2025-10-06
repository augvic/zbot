from flask import request, Blueprint
from flask.views import MethodView
from src.tasks.validate_login import ValidateLogin
from src.tasks.verify_if_logged_in import VerifyIfLoggedIn
from src.tasks.logout import Logout
from typing import cast

login = Blueprint("login", __name__)

class Login(MethodView):
    
    def post(self) -> dict[str, str | bool]:
        data = cast(dict[str, str], request.json)
        task = ValidateLogin()
        return task.execute(data)
    
    def get(self) -> dict[str, bool]:
        task = VerifyIfLoggedIn()
        return task.execute()
    
    def delete(self) -> dict[str, bool | str]:
        task = Logout()
        return task.execute()

login.add_url_rule("/login", view_func=Login.as_view("login"), methods=["GET", "POST", "DELETE"])
