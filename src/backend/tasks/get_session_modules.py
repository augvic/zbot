from src.backend.infrastructure.managers import SessionManager

class GetSessionModules:
    
    def _setup(self) -> None:
        self.session_manager = SessionManager()
    
    def execute(self) -> dict:
        self._setup()
        if not self.session_manager.is_user_in_session():
            return "Faça login.", 401
        return self.session_manager.get_from_session("session_modules")
