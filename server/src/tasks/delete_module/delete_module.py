from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from .models import Response

class DeleteModule:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.database_handler = database_handler
        self.session_manager = session_manager
        self.log_system = log_system
    
    def main(self, module: str) -> Response:
        try:
            module_exists = self.database_handler.modules_client.read(module)
            if module_exists == None:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar módulo: ❌ Módulo ({module}) não existe.")
                return Response(success=False, message=f"❌ Módulo ({module}) não existe.")
            if module == "zAdmin":
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar módulo: ❌ zAdmin não pode ser removido.")
                return Response(success=False, message="❌ zAdmin não pode ser removido.")
            self.database_handler.modules_client.delete(module)
            self.database_handler.permissions_client.delete_all(module)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar módulo:✅ Módulo ({module}) removido.")
            return Response(success=True, message=f"✅ Módulo ({module}) removido.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao deletar módulo ({module}). Contate o administrador.")
