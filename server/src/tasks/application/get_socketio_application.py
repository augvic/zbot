from src.components.socketio_application import SocketIoApplication
from src.components.wsgi_application import WsgiApplication

class GetSocketIoApplication:
    
    def execute(self, app: WsgiApplication) -> SocketIoApplication:
        return SocketIoApplication(app)
