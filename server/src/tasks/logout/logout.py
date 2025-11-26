from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from src.modules.request_manager import RequestManager
from .models import Response

class Logout:
    
    def __init__(self,
        session_manager: SessionManager,
        log_system: LogSystem,
        request_manager: RequestManager
    ) -> None:
        self.session_manager = session_manager
        self.log_system = log_system
        self.request_manager = request_manager
    
    def main(self) -> Response:
        try:
            user = self.session_manager.get_from_session("user")
            self.session_manager.clear_session()
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Logout realizado.")
            return Response(success=True, message="✅ Logout realizado.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.request_manager.get_user_ip()}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao fazer logout. Contate o administrador.")
