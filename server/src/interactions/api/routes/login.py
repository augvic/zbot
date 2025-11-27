from src.tasks.validate_login.validate_login import ValidateLogin
from src.tasks.verify_if_user_is_in_session.verify_if_user_is_in_session import VerifyIfUserIsInSession
from src.tasks.logout.logout import Logout
from src.tasks.process_request.process_request import ProcessRequest
from src.tasks.register_route import RegisterRoute
from typing import cast

class Login:
    
    def __init__(self,
        validate_login_task: ValidateLogin,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession,
        logout_task: Logout,
        process_request_task: ProcessRequest,
        register_route_task: RegisterRoute
    ) -> None:
        self.validate_login_task = validate_login_task
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
        self.logout_task = logout_task
        self.process_request_task = process_request_task
        register_route_task.main("/login", ["POST"], self.validate_login)
        register_route_task.main("/login", ["GET"], self.verify_if_user_is_in_session)
        register_route_task.main("/login", ["DELETE"], self.logout)
    
    def validate_login(self) -> tuple[dict[str, str | bool], int]:
        try:
            response = self.process_request_task.main(
                content_type="application/json",
                expected_data=[
                    "user",
                    "password"
                ],
                expected_files=[],
                optional_data=[],
                optional_files=[]
            )
            if not response.success:
                return {"success": False, "message": response.message}, 400
            response =  self.validate_login_task.main(
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
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.logout_task.main()
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 401
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
