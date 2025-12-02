from src.modules.wsgi_application.wsgi_session_manager import WsgiSessionManager
from src.modules.cli_session_manager import CliSessionManager
from src.modules.log_system import LogSystem
from src.modules.database_handler.database_handler import DatabaseHandler

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str

class Logout:
    
    def __init__(self,
        session_manager: WsgiSessionManager | CliSessionManager,
        log_system: LogSystem,
        database_handler: DatabaseHandler
    ) -> None:
        self.session_manager = session_manager
        self.log_system = log_system
        self.database_handler = database_handler
    
    def logout(self) -> Response:
        try:
            if not self.session_manager.is_user_in_session():
                self.log_system.write_text(f"👤 Usuário não identificado: ❌ Usuário não está logado.")
                return Response(success=False, message="❌ Usuário não está logado.")                
            user = self.session_manager.get_session_user()
            self.session_manager.clear_session()
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Logout realizado.")
            return Response(success=True, message="✅ Logout realizado.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário não identificado: ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao fazer logout. Contate o administrador.")
