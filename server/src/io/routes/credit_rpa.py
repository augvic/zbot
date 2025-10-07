from flask_socketio import SocketIO

class CreditRpa:
    
    def __init__(self, socketio: SocketIO) -> None:
        self.socketio = socketio
        self.socketio.on_event("start_credit_rpa", self.update_status_to_on) # type: ignore
        self.socketio.on_event("stop_credit_rpa", self.update_status_to_off) # type: ignore
    
    def update_status_to_on(self) -> None:
        self.socketio.emit("update_status", {"status": "Em processamento."}) # type: ignore
