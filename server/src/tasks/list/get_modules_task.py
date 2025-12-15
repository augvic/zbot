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
    
    def main(self) -> Response:
        try:
            modules = self.engines.serializer_engine.serialize_sqla_list(self.engines.database_engine.modules_client.read_all())
            return Response(success=True, message="✅ Módulos coletados.", data=modules)
        except Exception as error:
            raise Exception(f"❌ Error in (GetModulesTask) in (main) method: {error}")
