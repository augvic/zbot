from flask import request, Blueprint
from flask.views import MethodView
from src.tasks import ValidateLogin, VerifyIfLoggedIn

login = Blueprint("login", __name__)

class Login(MethodView):
    
    def post(self) -> dict[str, str]:
        data = request.json
        task = ValidateLogin()
        return task.execute(data)
    
    def get(self) -> dict[str, str]:
        task = VerifyIfLoggedIn()
        return task.execute()

login.add_url_rule("/login", view_func=Login.as_view("login"), methods=["GET", "POST"])
