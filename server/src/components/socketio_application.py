from flask_socketio import SocketIO
from .wsgi_application import WsgiApplication

class SocketIoApplication(SocketIO):
    
    def __init__(self, app: WsgiApplication):
        super().__init__(app)
