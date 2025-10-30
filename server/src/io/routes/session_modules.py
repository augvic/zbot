from flask import Flask
from src.tasks.auth.verify_if_user_is_in_session.task import VerifyIfUserIsInSession
from src.tasks.auth.get_session_modules.task import GetSessionModules

class SessionModules:
    
    def __init__(self, app: Flask) -> None:
        self.verify_if_user_is_in_session_task = VerifyIfUserIsInSession()
        self.get_session_modules_task = GetSessionModules()
        
        @app.route("/session-modules", methods=["GET"])
        def get_session_modules() -> tuple[str, int] | list[str]:
            if not self.verify_if_user_is_in_session_task.execute():
                return "Faça login.", 401
            return self.get_session_modules_task.execute()
