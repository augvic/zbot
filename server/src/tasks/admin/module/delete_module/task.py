from src.components.database_clients.clients.modules_client import ModulesClient
from src.components.database_clients.clients.permissions_client import PermissionsClient
from src.components.session_manager import SessionManager
from src.components.log_system import LogSystem
from .models import Response

class DeleteModule:
    
    def __init__(self) -> None:
        self.modules_client = ModulesClient("prd")
        self.permisssions_client = PermissionsClient("prd")
        self.session_manager = SessionManager()
        self.log_system = LogSystem("admin")
    
    def execute(self, module: str) -> Response:
        try:
            module_exists = self.modules_client.read(module)
            if module_exists == None:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao deletar módulo).\n❌ Módulo ({module}) não existe.")
                return Response(success=False, message=f"❌ Módulo ({module}) não existe.")
            if module == "zAdmin":
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao deletar módulo).\n❌ zAdmin não pode ser removido.")
                return Response(success=False, message="❌ zAdmin não pode ser removido.")
            self.modules_client.delete(module)
            self.permisssions_client.delete_all(module)
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao deletar módulo).\n✅ Módulo ({module}) removido.")
            return Response(success=True, message=f"✅ Módulo ({module}) removido.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Erro:\n{error}")
            raise Exception("❌ Erro interno ao deletar módulo ({module}). Contate o administrador.")
