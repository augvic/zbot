from src.tasks.auth.verify_if_user_is_in_session.task import VerifyIfUserIsInSession
from src.tasks.auth.get_session_modules.task import GetSessionModules
from src.tasks.application.route_registry import RouteRegistryTask

class SessionModules:
    
    def __init__(self,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession,
        get_session_modules_task: GetSessionModules,
        route_registry_task: RouteRegistryTask
    ) -> None:
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
        self.get_session_modules_task = get_session_modules_task
        self.route_registry_task = route_registry_task
        
    def init(self) -> None:
        try:
            def get_session_modules() -> tuple[dict[str, str | bool | list[str]], int]:
                try:
                    response = self.verify_if_user_is_in_session_task.execute()
                    if not response.success:
                        return {"success": False, "message": response.message}, 401
                    response = self.get_session_modules_task.execute()
                    return {"success": True, "message": response.message, "data": response.data}, 200
                except Exception as error:
                    return {"success": False, "message": f"{error}"}, 500
            
            self.route_registry_task.execute("/session-modules", ["GET"], get_session_modules)
        except Exception as error:
            print(f"❌ Error in (SessionModules) route: {error}.")