from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from src.components.infra.request_manager import RequestManager
from .models import Response

class VerifyIfUserIsInSession:
    
    def __init__(self,
        session_manager: SessionManager,
        log_system: LogSystem,
        request_manager: RequestManager
    ) -> None:
        self.session_manager = session_manager
        self.log_system = log_system
        self.request_manager = request_manager
    
    def execute(self) -> Response:
        try:
            if self.session_manager.is_user_in_session():
                self.log_system.write_text(f"✅ Usuário ({self.session_manager.get_from_session("user")}) está na sessão. Endpoint: {self.request_manager.get_endpoint()}.")
                return Response(success=True, message=f"✅ Usuário: {self.session_manager.get_from_session("user")} está na sessão.")
            else:
                self.log_system.write_text(f"❌ IP de usuário ({self.request_manager.get_user_ip()}) não está na sessão. Endpoint: {self.request_manager.get_endpoint()}.")
                return Response(success=False, message=f"❌ Não está na sessão.")
        except Exception as error:
            self.log_system.write_error(f"👤 IP de usuário ({self.request_manager.get_user_ip()}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao verificar se usuário está na sessão. Contate o administrador.")
