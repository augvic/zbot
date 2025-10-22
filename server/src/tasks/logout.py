from src.components.session_manager import SessionManager

class Logout:
    
    def __init__(self) -> None:
        self.session_manager = SessionManager()
    
    def execute(self) -> dict[str, str | bool]:
        self.session_manager.clear_session()
        return {"success": True, "message": "Logout realizado."}
