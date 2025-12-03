from src.engines.database_engine.database_engine import DatabaseEngine
from src.engines.log_engine import LogEngine
from src.engines.serializer_engine import SerializerEngine
from src.engines.wsgi_engine.wsgi_session_manager_engine import WsgiSessionManagerEngine
from src.engines.cli_session_manager_engine import CliSessionManagerEngine

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class GetModulesTask:
    
    def __init__(self,
        database_engine: DatabaseEngine,
        log_engine: LogEngine,
        serializer_engine: SerializerEngine,
        session_manager_engine: WsgiSessionManagerEngine | CliSessionManagerEngine,
        need_authentication: bool
    ) -> None:
        self.database_engine = database_engine
        self.log_engine = log_engine
        self.serializer_engine = serializer_engine
        self.session_manager_engine = session_manager_engine
        self.need_authentication = need_authentication
    
    def main(self) -> Response:
        try:
            if self.need_authentication:
                if not self.session_manager_engine.is_user_in_session():
                    return Response(success=False, message="❌ Necessário fazer login.", data=[])
                if not self.session_manager_engine.have_user_module_access("zAdmin"):
                    return Response(success=False, message="❌ Sem acesso.", data=[])
            modules = self.serializer_engine.serialize_sqla_list(self.database_engine.modules_client.read_all())
            self.log_engine.write_text(f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Módulos coletados: {modules}")
            return Response(success=True, message="✅ Módulos coletados.", data=modules)
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (GetModulesTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao coletar lista de módulos. Contate o administrador.")
