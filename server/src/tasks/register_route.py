from src.modules.wsgi_application import WsgiApplication
from typing import Callable

class RegisterRoute:
    
    def __init__(self,
        wsgi_application: WsgiApplication
    ) -> None:
        self.wsgi_application = wsgi_application
    
    def main(self, endpoint: str, methods: list[str], function: Callable) -> None:
        try:
            self.wsgi_application.app.route(endpoint, methods=methods)(function)
        except Exception as error:
            raise Exception(f"Error in (RegisterRoute) task in (main) method: {error}.")
