from src.modules.wsgi_application import WsgiApplication

from typing import Callable

class WsgiApplicationActions:
    
    def __init__(self,
        wsgi_application: WsgiApplication
    ) -> None:
        self.wsgi_application = wsgi_application
    
    def run(self) -> None:
        try:
            self.wsgi_application.run()
        except Exception as error:
            raise Exception(f"Error in (WsgiApplicationActions) task in (run) method: {error}")
    
    def register_route(self, endpoint: str, methods: list[str], function: Callable) -> None:
        try:
            self.wsgi_application.register_route(endpoint, methods, function)
        except Exception as error:
            raise Exception(f"Error in (WsgiApplicationActions) task in (register_route) method: {error}")
