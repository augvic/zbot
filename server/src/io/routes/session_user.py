from flask import Flask
from src.tasks.auth.verify_if_user_is_in_session.task import VerifyIfUserIsInSession
from src.tasks.auth.get_session_user.task import GetSessionUser

class SessionUser:
    
    def __init__(self, app: Flask) -> None:
        self.verify_if_user_is_in_session_task = VerifyIfUserIsInSession()
        self.get_session_user_task = GetSessionUser()
        
        @app.route("/session-user", methods=["GET"])
        def get_session_user() -> tuple[str, int] | list[str]:
            if not self.verify_if_user_is_in_session_task.execute():
                return "Faça login.", 401
            return self.get_session_user_task.execute()
