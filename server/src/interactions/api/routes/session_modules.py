from src.tasks.verify_if_user_is_in_session.verify_if_user_is_in_session import VerifyIfUserIsInSession
from src.tasks.get_session_modules.get_session_modules import GetSessionModules
from src.tasks.register_route import RegisterRoute

class SessionModules:
    
    def __init__(self,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession,
        get_session_modules_task: GetSessionModules,
        register_route_task: RegisterRoute
    ) -> None:
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
        self.get_session_modules_task = get_session_modules_task
        register_route_task.main("/session-modules", ["GET"], self.get_session_modules)
    
    def get_session_modules(self) -> tuple[dict[str, str | bool | list[str]], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.get_session_modules_task.main()
            return {"success": True, "message": response.message, "data": response.data}, 200
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
