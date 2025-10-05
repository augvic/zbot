from src.infrastructure.session_manager import SessionManager

class VerifyIfHaveAccess:
    
    def _setup(self) -> None:
        self.session_manager = SessionManager()
    
    def execute(self, module: str) -> bool:
        self._setup()
        if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access(module):
            return False
        return True
