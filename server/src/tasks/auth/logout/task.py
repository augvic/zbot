from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class Logout:
    
    def __init__(self) -> None:
        self.session_manager = SessionManager()
        self.log_system = LogSystem("auth/logout")
    
    def execute(self) -> Response:
        try:
            self.session_manager.clear_session()
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ✅ Logout realizado.")
            return Response(success=True, message="✅ Logout realizado.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao fazer logout. Contate o administrador.")
