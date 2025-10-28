from src.components.session_manager import SessionManager
from src.components.log_system import LogSystem
from .models import Response

class GetSessionModules:
    
    def __init__(self) -> None:
        self.session_manager = SessionManager()
        self.log_system = LogSystem("auth")
    
    def execute(self) -> Response:
        try:
            return self.session_manager.get_from_session("session_modules")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Erro:\n{error}")
            raise Exception("❌ Erro interno ao coletar módulos da sessão.")
