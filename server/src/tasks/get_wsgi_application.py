from src.components.wsgi_application import WsgiApplication

class GetWsgiApplication:
    
    def execute(self) -> WsgiApplication:
        return WsgiApplication()
