from src.tasks.auth.verify_if_user_is_in_session.task import VerifyIfUserIsInSession
from src.tasks.auth.get_session_user.task import GetSessionUser
from typing import Any

class SessionUser:
    
    def __init__(self,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession,
        get_session_user_task: GetSessionUser
    ) -> None:
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
        self.get_session_user_task = get_session_user_task
    
    def get_session_user(self) -> tuple[dict[str, str | bool | Any], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.get_session_user_task.main()
            return {"success": True, "message": response.message, "data": response.data}, 200
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
