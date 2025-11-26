from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from .models import Response

class GetSessionModules:
    
    def __init__(self,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.session_manager = session_manager
        self.log_system = log_system
    
    def main(self) -> Response:
        try:
            session_modules = self.session_manager.get_from_session("session_modules")
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Módulos de sessão coletados: {session_modules}.")
            return Response(success=True, message="✅ Módulos de sessão coletados.", data=session_modules)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao coletar módulos da sessão.")
