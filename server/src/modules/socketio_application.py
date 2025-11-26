from flask_socketio import SocketIO
from .wsgi_application import WsgiApplication

class SocketIoApplication(SocketIO):
    
    def __init__(self, app: WsgiApplication):
        try:
            super().__init__(app)
        except Exception as error:
            raise Exception(f"Error in (SocketIoApplication) component in (__init__) method: {error}.")
