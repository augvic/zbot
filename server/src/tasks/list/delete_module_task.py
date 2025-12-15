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
    
    def main(self, module: str) -> Response:
        try:
            module_exists = self.engines.database_engine.modules_client.read(module)
            if module_exists == None:
                return Response(success=False, message=f"❌ Módulo ({module}) não existe.", data=[])
            if module == "zAdmin":
                return Response(success=False, message="❌ zAdmin não pode ser removido.", data=[])
            self.engines.database_engine.modules_client.delete(module)
            self.engines.database_engine.permissions_client.delete_all(module)
            return Response(success=True, message=f"✅ Módulo ({module}) removido.", data=[])
        except Exception as error:
            raise Exception(f"❌ Error in (DeleteModuleTask) in (main) method: {error}")
