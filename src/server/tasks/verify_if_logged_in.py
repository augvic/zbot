from src.server.infrastructure.managers import SessionManager

class VerifyIfLoggedIn:
    
    def _setup(self) -> None:
        self.session_manager = SessionManager()
    
    def execute(self) -> dict:
        self._setup()
        if self.session_manager.is_user_in_session():
            return {"logged_in": True}
        return {"logged_in": False}
