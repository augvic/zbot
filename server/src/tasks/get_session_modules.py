from src.infrastructure.session_manager import SessionManager
from typing import Any

class GetSessionModules:
    
    def _setup(self) -> None:
        self.session_manager = SessionManager()
    
    def execute(self) -> Any:
        self._setup()
        return self.session_manager.get_from_session("session_modules")
