from src.components.infra.database_clients.clients.modules_client import ModulesClient
from src.components.infra.database_clients.clients.permissions_client import PermissionsClient
from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class DeleteModule:
    
    def __init__(self,
        modules_client: ModulesClient,
        permisssions_client: PermissionsClient,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.modules_client = modules_client
        self.permisssions_client = permisssions_client
        self.session_manager = session_manager
        self.log_system = log_system
    
    def main(self, module: str) -> Response:
        try:
            module_exists = self.modules_client.read(module)
            if module_exists == None:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar módulo: ❌ Módulo ({module}) não existe.")
                return Response(success=False, message=f"❌ Módulo ({module}) não existe.")
            if module == "zAdmin":
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar módulo: ❌ zAdmin não pode ser removido.")
                return Response(success=False, message="❌ zAdmin não pode ser removido.")
            self.modules_client.delete(module)
            self.permisssions_client.delete_all(module)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar módulo:✅ Módulo ({module}) removido.")
            return Response(success=True, message=f"✅ Módulo ({module}) removido.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao deletar módulo ({module}). Contate o administrador.")
