from src.tasks.auth.validate_login.task import ValidateLogin
from src.tasks.auth.verify_if_user_is_in_session.task import VerifyIfUserIsInSession
from src.tasks.auth.logout.task import Logout
from src.tasks.application.process_request.process_request import ProcessRequest
from ..models import LoginData
from src.components.infra.wsgi_application import WsgiApplication
from typing import cast

class Login:
    
    def __init__(self, app: WsgiApplication) -> None:
        self.validate_login_task = ValidateLogin()
        self.verify_if_user_is_in_session_task = VerifyIfUserIsInSession()
        self.logout_task = Logout()
        self.process_request_task = ProcessRequest()
        
        @app.route("/login", methods=["POST"])
        def validate_login() -> tuple[dict[str, str | bool], int] | dict[str, str | bool]:
            try:
                response = self.process_request_task.execute(
                    content_type="application/json",
                    expected_data=[
                        "user",
                        "password"
                    ],
                    expected_files=[],
                    optional=[]
                )
                if not response.success:
                    return {"success": False, "message": f"Erro: {response.message}"}, 415
                response =  self.validate_login_task.execute(
                    LoginData(
                        user=cast(str, response.data.get("user")),
                        password=cast(str, response.data.get("password"))
                    )
                )
                return {"success": True, "message": "Logado com sucesso."}
            except Exception as error:
                return {"success": False, "message": f"{error}"}
        
        @app.route("/login", methods=["GET"])
        def verify_if_user_is_in_session() -> dict[str, bool | str]:
            try:
                response = self.verify_if_user_is_in_session_task.execute()
                if response.success:
                    return {"success": True, "message": True}
                else:
                    return {"success": False, "message": response.message}
            except Exception as error:
                return {"success": False, "message": f"{error}"}
        
        @app.route("/login", methods=["DELETE"])
        def logout() -> dict[str, bool | str]:
            try:
                response = self.logout_task.execute()
                if response.success:
                    return {"success": True, "message": response.message}
                else:
                    return {"success": False, "message": response.message}
            except Exception as error:
                return {"success": False, "message": f"{error}"}
