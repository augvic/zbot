from src.engines.database_engine.database_engine import DatabaseEngine
from src.engines.log_engine import LogEngine
from src.engines.wsgi_engine.wsgi_session_manager_engine import WsgiSessionManagerEngine
from src.engines.cli_session_manager_engine import CliSessionManagerEngine

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class CreateModuleTask:
    
    def __init__(self,
        database_engine: DatabaseEngine,
        log_engine: LogEngine,
        session_manager_engine: WsgiSessionManagerEngine | CliSessionManagerEngine,
        need_authentication: bool
    ) -> None:
        self.database_engine = database_engine
        self.log_engine = log_engine
        self.session_manager_engine = session_manager_engine
        self.need_authentication = need_authentication
    
    def main(self, module: str, description: str) -> Response:
        try:
            if self.need_authentication:
                if not self.session_manager_engine.is_user_in_session():
                    return Response(success=False, message="❌ Necessário fazer login.", data=[])
                if not self.session_manager_engine.have_user_module_access("zAdmin"):
                    return Response(success=False, message="❌ Sem acesso.", data=[])
            if not module:
                return Response(success=False, message="❌ Preencha o módulo.", data=[])
            if self.database_engine.modules_client.read(module):
                return Response(success=False, message=f"❌ Módulo ({module}) já existe.", data=[])
            if description == "":
                return Response(success=False, message="❌ Preencha a descrição.", data=[])
            self.database_engine.modules_client.create(module, description)
            self.log_engine.write_text(f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Módulo ({module}) adicionado.")
            return Response(success=True, message=f"✅ Módulo ({module}) adicionado.", data=[])
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (CreateModuleTask) task in (main) method: {error}")
            raise Exception(f"❌ Erro interno ao criar módulo. Contate o administrador.")
