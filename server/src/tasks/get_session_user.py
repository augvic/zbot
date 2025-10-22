from src.components.session_manager import SessionManager
from typing import Any

class GetSessionUser:
    
    def __init__(self) -> None:
        self.session_manager = SessionManager()
    
    def execute(self) -> Any:
        return self.session_manager.get_from_session("user")
