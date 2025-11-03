from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from src.components.infra.request_manager import RequestManager
from .models import Response

class VerifyIfUserIsInSession:
    
    def __init__(self) -> None:
        self.session_manager = SessionManager()
        self.log_system = LogSystem("auth/verify_if_user_is_in_session")
        self.request_manager = RequestManager()
    
    def execute(self) -> Response:
        try:
            if self.session_manager.is_user_in_session():
                self.log_system.write_text(f"✅ Usuário ({self.session_manager.get_from_session("user")}) está na sessão. Endpoint: {self.request_manager.get_endpoint()}")
                return Response(success=True, message=f"✅ Usuário: {self.session_manager.get_from_session("user")} está na sessão.")
            else:
                self.log_system.write_text(f"❌ IP de usuário ({self.request_manager.get_user_ip()}) não está na sessão. Endpoint: {self.request_manager.get_endpoint()}")
                return Response(success=True, message=f"❌ Não está na sessão.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao verificar se usuário está na sessão. Contate o administrador.")
