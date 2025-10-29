from src.components.infra.session_manager import SessionManager

class VerifyIfUserIsInSession:
    
    def __init__(self) -> None:
        self.session_manager = SessionManager()
    
    def execute(self) -> bool:
        return self.session_manager.is_user_in_session()
