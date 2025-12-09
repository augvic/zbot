from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class DeleteModuleTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
        self.runtime = "cli"
    
    def set_runtime(self, runtime: str) -> None:
        self.runtime = runtime
    
    def main(self, module: str) -> Response:
        try:
            if self.runtime == "cli":
                self.session_manager_engine = self.engines.cli_session_engine
            else:
                self.session_manager_engine = self.engines.wsgi_engine.session_manager
            module_exists = self.engines.database_engine.modules_client.read(module)
            if module_exists == None:
                return Response(success=False, message=f"❌ Módulo ({module}) não existe.", data=[])
            if module == "zAdmin":
                return Response(success=False, message="❌ zAdmin não pode ser removido.", data=[])
            self.engines.database_engine.modules_client.delete(module)
            self.engines.database_engine.permissions_client.delete_all(module)
            self.engines.log_engine.write_text("tasks/delete_module_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Módulo ({module}) removido.")
            return Response(success=True, message=f"✅ Módulo ({module}) removido.", data=[])
        except Exception as error:
            self.engines.log_engine.write_error("tasks/delete_module_task", f"❌ Error in (DeleteModuleTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao deletar módulo. Contate o administrador.")
