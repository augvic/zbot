from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class GetModulesTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
        self.runtime = "cli"
    
    def set_runtime(self, runtime: str) -> None:
        self.runtime = runtime
    
    def main(self) -> Response:
        try:
            if self.runtime == "cli":
                self.session_manager_engine = self.engines.cli_session_engine
            else:
                
                self.session_manager_engine = self.engines.wsgi_engine.session_manager
            modules = self.engines.serializer_engine.serialize_sqla_list(self.engines.database_engine.modules_client.read_all())
            self.engines.log_engine.write_text("tasks/get_modules_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Módulos coletados: {modules}")
            return Response(success=True, message="✅ Módulos coletados.", data=modules)
        except Exception as error:
            self.engines.log_engine.write_error("tasks/get_modules_task", f"❌ Error in (GetModulesTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao coletar lista de módulos. Contate o administrador.")
