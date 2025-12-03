from src.engines.wsgi_engine.wsgi_engine import WsgiEngine
from src.engines.log_engine import LogEngine
from typing import Callable

class RegisterRouteTask:
    
    def __init__(self,
        wsgi_engine: WsgiEngine,
        log_engine: LogEngine
    ) -> None:
        self.wsgi_engine = wsgi_engine
        self.log_engine = log_engine
    
    def main(self, endpoint: str, methods: list[str], function: Callable) -> None:
        try:
            self.wsgi_engine.register_route(endpoint, methods, function)
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (RegisterRouteTask) task in (main) method: {error}")
            raise Exception(f"❌ Erro interno ao registrar rota. Contate o administrador.")
