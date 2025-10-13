from flask import Flask
from src.tasks.verify_if_user_is_in_session import VerifyIfUserIsInSession
from src.tasks.get_session_user import GetSessionUser

class SessionUser:
    
    def __init__(self, app: Flask) -> None:
        
        @app.route("/session-user", methods=["GET"])
        def get_session_user() -> tuple[str, int] | list[str]:
            task1 = VerifyIfUserIsInSession()
            task2 = GetSessionUser()
            if not task1.execute():
                return "Faça login.", 401
            return task2.execute()
