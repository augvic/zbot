from src.tasks.auth.validate_login.task import ValidateLogin
from src.tasks.auth.verify_if_user_is_in_session.task import VerifyIfUserIsInSession
from src.tasks.auth.logout.task import Logout
from src.tasks.application.process_request.task import ProcessRequest
from src.tasks.application.route_registry import RouteRegistryTask
from typing import cast

class Login:
    
    def __init__(self,
        validate_login_task: ValidateLogin,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession,
        logout_task: Logout,
        process_request_task: ProcessRequest,
        route_registry_task: RouteRegistryTask
    ) -> None:
        self.validate_login_task = validate_login_task
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
        self.logout_task = logout_task
        self.process_request_task = process_request_task
        self.route_registry_task = route_registry_task
    
    def init(self) -> None:
        try:
            def validate_login() -> tuple[dict[str, str | bool], int]:
                try:
                    response = self.process_request_task.execute(
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
                    response =  self.validate_login_task.execute(
                        user=cast(str, response.data.get("user")),
                        password=cast(str, response.data.get("password"))
                    )
                    if response.success:
                        return {"success": True, "message": response.message}, 200
                    else:
                        return {"success": False, "message": response.message}, 400
                except Exception as error:
                    return {"success": False, "message": f"{error}"}, 500
            
            def verify_if_user_is_in_session() -> tuple[dict[str, str | bool], int]:
                try:
                    response = self.verify_if_user_is_in_session_task.execute()
                    if response.success:
                        return {"success": True, "message": response.message}, 200
                    else:
                        return {"success": False, "message": response.message}, 401
                except Exception as error:
                    return {"success": False, "message": f"{error}"}, 500
            
            def logout() -> tuple[dict[str, str | bool], int]:
                try:
                    response = self.logout_task.execute()
                    if response.success:
                        return {"success": True, "message": response.message}, 200
                    else:
                        return {"success": True, "message": response.message}, 401
                except Exception as error:
                    return {"success": False, "message": f"{error}"}, 500
            
            self.route_registry_task.execute("/login", ["POST"], validate_login)
            self.route_registry_task.execute("/login", ["GET"], verify_if_user_is_in_session)
            self.route_registry_task.execute("/login", ["DELETE"], logout)
        except Exception as error:
            print(f"❌ Error in (Login) route: {error}.")
