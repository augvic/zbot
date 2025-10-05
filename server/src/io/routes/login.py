from flask import request, Blueprint
from flask.views import MethodView
from src.tasks.validate_login import ValidateLogin
from src.tasks.verify_if_logged_in import VerifyIfLoggedIn

login = Blueprint("login", __name__)

class Login(MethodView):
    
    def post(self) -> dict[str, str]:
        data = request.json
        task = ValidateLogin()
        response = task.execute(data)
        self.session_manager.save_in_session("user", data["user"])
        self.session_manager.save_in_session("session_modules", permissions["permissions"])
    
    def get(self) -> dict[str, str]:
        task = VerifyIfLoggedIn()
        return task.execute()

login.add_url_rule("/login", view_func=Login.as_view("login"), methods=["GET", "POST"])
