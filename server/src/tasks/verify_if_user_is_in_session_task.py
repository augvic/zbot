from src.engines.wsgi_engine.wsgi_session_manager_engine import WsgiSessionManagerEngine
from src.engines.cli_session_manager_engine import CliSessionManagerEngine
from src.engines.log_engine import LogEngine

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str


class VerifyIfUserIsInSessionTask:
    
    def __init__(self,
        session_manager_engine: WsgiSessionManagerEngine | CliSessionManagerEngine,
        log_engine: LogEngine
    ) -> None:
        self.session_manager_engine = session_manager_engine
        self.log_engine = log_engine
    
    def main(self) -> Response:
        try:
            if self.session_manager_engine.is_user_in_session():
                return Response(success=True, message=f"✅ Usuário ({self.session_manager_engine.get_session_user()}) está na sessão.")
            else:
                return Response(success=False, message=f"❌ Não está na sessão.")
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (VerifyIfUserIsInSessionTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao verificar se usuário está na sessão. Contate o administrador.")
