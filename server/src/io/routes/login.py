from flask import request, Flask
from src.tasks.validate_login import ValidateLogin
from src.tasks.verify_if_user_is_in_session import VerifyIfUserIsInSession
from src.tasks.logout import Logout
from typing import cast

class Login:
    
    def __init__(self, app: Flask) -> None:
        self.validate_login_task = ValidateLogin()
        self.verify_if_user_is_in_session_task = VerifyIfUserIsInSession()
        self.logout_task = Logout()
        
        @app.route("/login", methods=["POST"])
        def validate_login() -> dict[str, str | bool]:
            data = cast(dict[str, str], request.json)
            return self.validate_login_task.execute(data)
        
        @app.route("/login", methods=["GET"])
        def verify_if_user_is_in_session() -> dict[str, bool]:
            isInSession = self.verify_if_user_is_in_session_task.execute()
            return {"logged_in": isInSession}
        
        @app.route("/login", methods=["DELETE"])
        def logout() -> dict[str, bool | str]:
            return self.logout_task.execute()
