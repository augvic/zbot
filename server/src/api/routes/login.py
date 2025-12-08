from src.tasks.login_task import LoginTask
from src.tasks.logout_task import LogoutTask
from src.tasks.process_request_task import ProcessRequestTask
from src.tasks.verify_if_user_is_in_session_task import VerifyIfUserIsInSessionTask

from typing import cast

class LoginRoute:
    
    def __init__(self,
        login_task: LoginTask,
        logout_task: LogoutTask,
        process_request_task: ProcessRequestTask,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSessionTask
    ) -> None:
        self.login_task = login_task
        self.logout_task = logout_task
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
        self.process_request_task = process_request_task
        wsgi_engine.register_route("/login", ["POST"], self.validate_login)
        wsgi_engine.register_route("/login", ["GET"], self.verify_if_user_is_in_session)
        wsgi_engine.register_route("/login", ["DELETE"], self.logout)
    
    def validate_login(self) -> tuple[dict[str, str | bool], int]:
        try:
            response = self.process_request_task.main(
                content_type="application/json",
                expected_data=[
                    "user",
                    "password"
                ],
                expected_files=[]
            )
            if not response.success:
                return {"success": False, "message": response.message}, 400
            response =  self.login_task.main(
                user=cast(str, response.data.get("user")),
                password=cast(str, response.data.get("password"))
            )
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def verify_if_user_is_in_session(self) -> tuple[dict[str, str | bool], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 401
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def logout(self) -> tuple[dict[str, str | bool], int]:
        try:
            response = self.logout_task.main()
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 401
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
