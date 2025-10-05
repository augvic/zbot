from src.infrastructure.session_manager import SessionManager

class VerifyIfLoggedIn:
    
    def _setup(self) -> None:
        self.session_manager = SessionManager()
    
    def execute(self) -> dict[str, bool]:
        self._setup()
        if self.session_manager.is_user_in_session():
            return {"logged_in": True}
        return {"logged_in": False}
