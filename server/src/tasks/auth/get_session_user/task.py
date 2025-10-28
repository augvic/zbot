from src.components.session_manager import SessionManager
from src.components.log_system import LogSystem
from .models import Response

class GetSessionUser:
    
    def __init__(self) -> None:
        self.session_manager = SessionManager()
        self.log_system = LogSystem("auth")
    
    def execute(self) -> Response:
        try:
            session_user = self.session_manager.get_from_session("user")
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}. ✅ Usuário de sessão coletado: {session_user}.")
            return Response(success=True, message="✅ Usuário da sessão coletado.", data=session_user)
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Erro:\n{error}")
            raise Exception("❌ Erro interno ao coletar usuário de sessão. Contate o administrador.")
