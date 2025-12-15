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
    
    def main(self, module: str, description: str) -> Response:
        try:
            if not module:
                return Response(success=False, message="❌ Preencha o módulo.", data=[])
            if self.engines.database_engine.modules_client.read(module):
                return Response(success=False, message=f"❌ Módulo ({module}) já existe.", data=[])
            if description == "":
                return Response(success=False, message="❌ Preencha a descrição.", data=[])
            self.engines.database_engine.modules_client.create(module, description)
            return Response(success=True, message=f"✅ Módulo ({module}) adicionado.", data=[])
        except Exception as error:
            raise Exception(f"❌ Error in (CreateModuleTask) in (main) method: {error}")
