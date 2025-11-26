from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from .models import Response

class VerifyIfHaveAccess:
    
    def __init__(self,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.session_manager = session_manager
        self.log_system = log_system
    
    def main(self, module: str) -> Response:
        try:
            if not self.session_manager.have_user_module_access(module):
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Não tem acesso ao módulo: ({module}).")
                return Response(success=False, message="❌ Sem autorização.")
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Tem acesso ao módulo: ({module}).")
            return Response(success=True, message="✅ Tem acesso.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao verificar se possui acesso. Contate o administrador.")
