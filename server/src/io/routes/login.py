from src.tasks.validate_login import ValidateLogin
from src.tasks.verify_if_user_is_in_session import VerifyIfUserIsInSession
from src.tasks.logout import Logout
from src.tasks.process_request import ProcessRequest
from ..models import LoginData

from flask import Flask

class Login:
    
    def __init__(self, app: Flask) -> None:
        self.validate_login_task = ValidateLogin()
        self.verify_if_user_is_in_session_task = VerifyIfUserIsInSession()
        self.logout_task = Logout()
        self.process_request_task = ProcessRequest()
        
        @app.route("/login", methods=["POST"])
        def validate_login() -> tuple[dict[str, str | bool], int] | dict[str, str | bool]:
            request_processed = self.process_request_task.execute(
                content_type="application/json",
                expected_data=[
                    "user",
                    "password"
                ],
                expected_files=[],
                not_expected_data=[],
                not_expected_files=[]
            )
            if not request_processed.success:
                return {"success": False, "message": f"Erro: {request_processed.message}"}, 415
            return self.validate_login_task.execute(
                LoginData(
                    user=request_processed.data["user"],
                    password=request_processed.data["password"]
                )
            )
        
        @app.route("/login", methods=["GET"])
        def verify_if_user_is_in_session() -> dict[str, bool]:
            isInSession = self.verify_if_user_is_in_session_task.execute()
            return {"logged_in": isInSession}
        
        @app.route("/login", methods=["DELETE"])
        def logout() -> dict[str, bool | str]:
            return self.logout_task.execute()
