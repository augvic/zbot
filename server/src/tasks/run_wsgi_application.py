from src.modules.wsgi_application import WsgiApplication

class RunWsgiApplication:
    
    def __init__(self,
        wsgi_application: WsgiApplication
    ) -> None:
        self.wsgi_application = wsgi_application
    
    def main(self) -> None:
        self.wsgi_application.socketio.run(self.wsgi_application.app, host="127.0.0.1", debug=True)
