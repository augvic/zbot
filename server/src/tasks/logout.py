from src.infrastructure.session_manager import SessionManager

class Logout:
    
    def _setup(self) -> None:
        self.session_manager = SessionManager()
    
    def execute(self) -> dict[str, str | bool]:
        self._setup()
        self.session_manager.clear_session()
        return {"success": True, "message": "Logout realizado."}
