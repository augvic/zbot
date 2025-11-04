from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class GetSessionModules:
    
    def __init__(self) -> None:
        self.session_manager = SessionManager()
        self.log_system = LogSystem("auth/get_session_modules")
    
    def execute(self) -> Response:
        try:
            session_modules = self.session_manager.get_from_session("session_modules")
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ✅ Módulos de sessão coletados: {session_modules}.")
            return Response(success=True, message="✅ Módulos de sessão coletados.", data=session_modules)
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao coletar módulos da sessão.")
