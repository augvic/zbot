from src.components.infra.database_clients.clients.modules_client import ModulesClient
from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class CreateModule:
    
    def __init__(self) -> None:
        self.modules_client = ModulesClient("prd")
        self.session_manager = SessionManager()
        self.log_system = LogSystem("admin/modules/create_module")
    
    def execute(self, module: str, description: str) -> Response:
        try:
            if not module:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}) ao criar módulo: ❌ Preencha o módulo.")
                return Response(success=False, message="❌ Preencha o módulo.")
            if self.modules_client.read(module):
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}) ao criar módulo: ❌ Módulo ({module}) já existe.")
                return Response(success=False, message=f"❌ Módulo ({module}) já existe.")
            if description == "":
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}) ao criar módulo: ❌ Preencha a descrição.")
                return Response(success=False, message="❌ Preencha a descrição.")
            self.modules_client.create(module, description)
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}) ao criar módulo: ✅ Módulo ({module}) adicionado.")
            return Response(success=True, message=f"✅ Módulo ({module}) adicionado.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário ({self.session_manager.get_from_session("user")}) ao criar módulo ({module}). ❌ Erro: {error}.")
            raise Exception(f"❌ Erro interno ao criar módulo ({module}). Contate o administrador.")
