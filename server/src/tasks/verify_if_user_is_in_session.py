from src.infrastructure.session_manager import SessionManager

class VerifyIfUserIsInSession:
    
    def _setup(self) -> None:
        self.session_manager = SessionManager()
    
    def execute(self) -> bool:
        self._setup()
        return self.session_manager.is_user_in_session()
