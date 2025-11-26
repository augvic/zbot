from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from .models import Response

class GetSessionUser:
    
    def __init__(self,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.session_manager = session_manager
        self.log_system = log_system
    
    def main(self) -> Response:
        try:
            session_user = self.session_manager.get_from_session("user")
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Usuário de sessão coletado: {session_user}.")
            return Response(success=True, message="✅ Usuário da sessão coletado.", data=session_user)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao coletar usuário de sessão. Contate o administrador.")
