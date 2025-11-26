from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from .models import Response

class CreateModule:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.database_handler = database_handler
        self.session_manager = session_manager
        self.log_system = log_system
    
    def main(self, module: str, description: str) -> Response:
        try:
            if not module:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar módulo: ❌ Preencha o módulo.")
                return Response(success=False, message="❌ Preencha o módulo.")
            if self.database_handler.modules_client.read(module):
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar módulo: ❌ Módulo ({module}) já existe.")
                return Response(success=False, message=f"❌ Módulo ({module}) já existe.")
            if description == "":
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar módulo: ❌ Preencha a descrição.")
                return Response(success=False, message="❌ Preencha a descrição.")
            self.modules_client.create(module, description)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar módulo: ✅ Módulo ({module}) adicionado.")
            return Response(success=True, message=f"✅ Módulo ({module}) adicionado.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar módulo ({module}). ❌ Erro: {error}.")
            raise Exception(f"❌ Erro interno ao criar módulo ({module}). Contate o administrador.")
