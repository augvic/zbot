from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from src.modules.sqla_serializer import SqlaSerializer

from .models import Response

class Module:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        session_manager: SessionManager,
        log_system: LogSystem,
        serializer: SqlaSerializer
    ) -> None:
        self.database_handler = database_handler
        self.session_manager = session_manager
        self.log_system = log_system
        self.serializer = serializer
    
    def create(self, module: str, description: str) -> Response:
        try:
            if not module:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar módulo: ❌ Preencha o módulo.")
                return Response(success=False, message="❌ Preencha o módulo.", data=[])
            if self.database_handler.modules_client.read(module):
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar módulo: ❌ Módulo ({module}) já existe.")
                return Response(success=False, message=f"❌ Módulo ({module}) já existe.", data=[])
            if description == "":
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar módulo: ❌ Preencha a descrição.")
                return Response(success=False, message="❌ Preencha a descrição.", data=[])
            self.database_handler.modules_client.create(module, description)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar módulo: ✅ Módulo ({module}) adicionado.")
            return Response(success=True, message=f"✅ Módulo ({module}) adicionado.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar módulo ({module}). ❌ Erro: {error}")
            raise Exception(f"❌ Erro interno ao criar módulo ({module}). Contate o administrador.")
    
    def delete(self, module: str) -> Response:
        try:
            module_exists = self.database_handler.modules_client.read(module)
            if module_exists == None:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar módulo: ❌ Módulo ({module}) não existe.")
                return Response(success=False, message=f"❌ Módulo ({module}) não existe.", data=[])
            if module == "zAdmin":
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar módulo: ❌ zAdmin não pode ser removido.")
                return Response(success=False, message="❌ zAdmin não pode ser removido.", data=[])
            self.database_handler.modules_client.delete(module)
            self.database_handler.permissions_client.delete_all(module)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar módulo:✅ Módulo ({module}) removido.")
            return Response(success=True, message=f"✅ Módulo ({module}) removido.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao deletar módulo ({module}). Contate o administrador.")
    
    def get_all(self) -> Response:
        try:
            modules = self.serializer.serialize_list(self.database_handler.modules_client.read_all())
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Módulos coletados.")
            return Response(success=True, message="✅ Módulos coletados.", data=modules)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao coletar lista de módulos. Contate o administrador.")
