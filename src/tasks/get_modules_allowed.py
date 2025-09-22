from src.infrastructure.file_systems import SessionManager

class GetModulesAllowed:
    
    def _setup(self) -> None:
        self.session_manager = SessionManager()
    
    def execute(self) -> dict:
        self._setup()
        return self.session_manager.get_from_session("modules_allowed")
