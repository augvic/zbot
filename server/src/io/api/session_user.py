from src.tasks.auth.verify_if_user_is_in_session.task import VerifyIfUserIsInSession
from src.tasks.auth.get_session_user.task import GetSessionUser
from src.tasks.application.route_registry import RouteRegistryTask
from typing import Any

class SessionUser:
    
    def __init__(self,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession,
        get_session_user_task: GetSessionUser,
        route_registry_task: RouteRegistryTask
    ) -> None:
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
        self.get_session_user_task = get_session_user_task
        self.route_registry_task = route_registry_task
        
    def init(self) -> None:
        try:
            def get_session_user() -> tuple[dict[str, str | bool | Any], int]:
                try:
                    response = self.verify_if_user_is_in_session_task.execute()
                    if not response.success:
                        return {"success": False, "message": response.message}, 401
                    response = self.get_session_user_task.execute()
                    return {"success": True, "message": response.message, "data": response.data}, 200
                except Exception as error:
                    return {"success": False, "message": f"{error}"}, 500
            
            self.route_registry_task.execute("/session-user", ["GET"], get_session_user )
        except Exception as error:
            print(f"❌ Error in (SessionUser) route: {error}.")
