from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class CreateModuleTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
        self.runtime = "cli"
    
    def set_runtime(self, runtime: str) -> None:
        self.runtime = runtime
    
    def main(self, module: str, description: str) -> Response:
        try:
            if self.runtime == "cli":
                self.session_manager_engine = self.engines.cli_session_engine
            else:
                self.session_manager_engine = self.engines.wsgi_engine.session_manager
            if not module:
                return Response(success=False, message="❌ Preencha o módulo.", data=[])
            if self.engines.database_engine.modules_client.read(module):
                return Response(success=False, message=f"❌ Módulo ({module}) já existe.", data=[])
            if description == "":
                return Response(success=False, message="❌ Preencha a descrição.", data=[])
            self.engines.database_engine.modules_client.create(module, description)
            self.engines.log_engine.write_text("tasks/create_module_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Módulo ({module}) adicionado.")
            return Response(success=True, message=f"✅ Módulo ({module}) adicionado.", data=[])
        except Exception as error:
            self.engines.log_engine.write_error("tasks/create_module_task", f"❌ Error in (CreateModuleTask) task in (main) method: {error}")
            raise Exception(f"❌ Erro interno ao criar módulo. Contate o administrador.")
