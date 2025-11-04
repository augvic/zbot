from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class VerifyIfHaveAccess:
    
    def __init__(self) -> None:
        self.session_manager = SessionManager()
        self.log_system = LogSystem("auth/verify_if_have_access")
    
    def execute(self, module: str) -> Response:
        try:
            if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access(module):
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Não tem acesso ao módulo: ({module}).")
                return Response(success=False, message="❌ Não tem acesso.")
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ✅ Tem acesso ao módulo: ({module}).")
            return Response(success=True, message="✅ Tem acesso.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao verificar se possui acesso. Contate o administrador.")
