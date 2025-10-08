from flask_socketio import SocketIO
from src.tasks.run_credit_rpa import RunCreditRpa

class ZcredrpaWebsocket:
    
    def __init__(self, socketio: SocketIO) -> None:
        self.is_running = False
        self.stop = False
        self.memory = ""
        self.socketio = socketio
        self.socketio.on_event("zcredrpa_refresh", self.refresh) # type: ignore
        self.socketio.on_event("zcredrpa_start", self.update_status_to_on) # type: ignore
        self.socketio.on_event("zcredrpa_stop", self.update_status_to_off) # type: ignore
    
    def update_status_to_on(self) -> None:
        if self.is_running == True:
            self.socketio.emit("zcredrpa_notification", {"success": False, "message": "RPA já está em processamento."}) # type: ignore
            return
        self.socketio.emit("zcredrpa_status", {"status": "Iniciando..."}) # type: ignore
        task = RunCreditRpa()
        task.execute(self)
    
    def update_status_to_off(self) -> None:
        if self.is_running == False:
            self.socketio.emit("zcredrpa_notification", {"message": "RPA já está desligado."}) # type: ignore    
            return
        self.socketio.emit("zcredrpa_status", {"status": "Desligando..."}) # type: ignore
        self.stop = True
    
    def refresh(self) -> None:
        if self.is_running == True:
            self.socketio.emit("zcredrpa_status", {"status": "Em processamento."}) # type: ignore
        else:
            self.socketio.emit("zcredrpa_status", {"status": "Desligado."}) # type: ignore
        self.socketio.emit("zcredrpa_terminal", {"message": self.memory}) # type: ignore
