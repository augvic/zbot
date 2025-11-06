from src.components.infra.wsgi_application import WsgiApplication
from src.components.file_system.log_system import LogSystem
from typing import Callable

class RouteRegistryTask:
    
    def __init__(self,
        app_component: WsgiApplication,
        log_system: LogSystem
    ) -> None:
        self.app_component = app_component
        self.log_system = log_system
    
    def execute(self, end_point: str, methods: list[str], function: Callable) -> None:
        try:
            self.app_component.route(end_point, methods=methods)(function)
        except Exception as error:
            self.log_system.write_error(f"❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao retornar template. Contate o administrador.")
