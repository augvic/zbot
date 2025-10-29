from src.components.infra.socketio_application import SocketIoApplication
from src.components.infra.wsgi_application import WsgiApplication

class GetSocketIoApplication:
    
    def execute(self, app: WsgiApplication) -> SocketIoApplication:
        return SocketIoApplication(app)
