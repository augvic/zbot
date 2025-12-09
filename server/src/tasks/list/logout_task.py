from src.engines.list.wsgi_engine.wsgi_session_manager_engine import WsgiSessionManagerEngine
from src.engines.list.cli_session_manager_engine import CliSessionManagerEngine
from src.engines.list.log_engine import LogEngine

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str

class LogoutTask:
    
    def __init__(self,
        session_manager_engine: WsgiSessionManagerEngine | CliSessionManagerEngine,
        log_engine: LogEngine
    ) -> None:
        self.session_manager_engine = session_manager_engine
        self.log_engine = log_engine
    
    def main(self) -> Response:
        try:
            if not self.session_manager_engine.is_user_in_session():
                return Response(success=False, message="❌ Usuário não está logado.")     
            user = self.session_manager_engine.get_session_user()
            self.session_manager_engine.clear_session()
            self.log_engine.write_text("tasks/logout_task", f"👤 Usuário ({user}): ✅ Logout realizado.")
            return Response(success=True, message="✅ Logout realizado.")
        except Exception as error:
            self.log_engine.write_error("tasks/logout_task", f"❌ Error in (LogoutTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao fazer logout. Contate o administrador.")
