from src.engines.log_engine import LogEngine
from src.engines.wsgi_engine.wsgi_engine import WsgiEngine

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: dict[str, str]

class ProcessRequestTask:
    
    def __init__(self,
        log_engine: LogEngine,
        wsgi_engine: WsgiEngine
    ) -> None:
        self.log_engine = log_engine
        self.wsgi_engine = wsgi_engine
    
    def main(self, content_type: str, expected_data: list[str], expected_files: list[str]) -> Response:
        try:
            request_processed = self.wsgi_engine.process_request(content_type, expected_data, expected_files)
            if request_processed.success:
                return Response(success=True, message=request_processed.message, data=request_processed.data)
            else:
                return Response(success=False, message=request_processed.message, data=request_processed.data)
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (CreateModuleTask) task in (main) method: {error}")
            raise Exception(f"❌ Erro interno ao criar módulo. Contate o administrador.")
