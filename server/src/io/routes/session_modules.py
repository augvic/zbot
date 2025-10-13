from flask import Flask
from src.tasks.verify_if_user_is_in_session import VerifyIfUserIsInSession
from src.tasks.get_session_modules import GetSessionModules

class SessionModules:
    
    def __init__(self, app: Flask) -> None:
        
        @app.route("/session-modules", methods=["GET"])
        def get_session_modules() -> tuple[str, int] | list[str]:
            task1 = VerifyIfUserIsInSession()
            task2 = GetSessionModules()
            if not task1.execute():
                return "Faça login.", 401
            return task2.execute()
