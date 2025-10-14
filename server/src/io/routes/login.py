from flask import request, Flask
from src.tasks.validate_login import ValidateLogin
from src.tasks.verify_if_user_is_in_session import VerifyIfUserIsInSession
from src.tasks.logout import Logout
from typing import cast

class Login:
    
    def __init__(self, app: Flask) -> None:
        
        @app.route("/login", methods=["POST"])
        def validate_login() -> dict[str, str | bool]:
            data = cast(dict[str, str], request.json)
            task = ValidateLogin()
            return task.execute(data)
        
        @app.route("/login", methods=["GET"])
        def verify_if_user_is_in_session() -> dict[str, bool]:
            task = VerifyIfUserIsInSession()
            isInSession = task.execute()
            return {"logged_in": isInSession}
        
        @app.route("/login", methods=["DELETE"])
        def logout() -> dict[str, bool | str]:
            task = Logout()
            return task.execute()
