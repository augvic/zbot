from flask_socketio import SocketIO
from src.tasks.run_registrations_rpa import RunRegistrationsRpa

class RegRpaWebsocket:
    
    def __init__(self, socketio: SocketIO) -> None:
        self.is_running = False
        self.stop = False
        self.memory: list[str] = []
        self.socketio = socketio
        self.socketio.on_event("regrpa_refresh", self.refresh) # type: ignore
        self.socketio.on_event("regrpa_start", self.update_status_to_on) # type: ignore
        self.socketio.on_event("regrpa_stop", self.update_status_to_off) # type: ignore
    
    def update_status_to_on(self) -> None:
        if self.is_running == True:
            self.socketio.emit("regrpa_notification", {"success": False, "message": "RPA já está em processamento."}) # type: ignore
            return
        self.socketio.emit("regrpa_status", {"status": "Iniciando..."}) # type: ignore
        task = RunRegistrationsRpa()
        task.execute(self)
    
    def update_status_to_off(self) -> None:
        if self.is_running == False:
            self.socketio.emit("regrpa_notification", {"message": "RPA já está desligado."}) # type: ignore    
            return
        self.socketio.emit("regrpa_status", {"status": "Desligando..."}) # type: ignore
        self.stop = True
    
    def refresh(self) -> None:
        if self.is_running == True:
            self.socketio.emit("regrpa_status", {"status": "Em processamento."}) # type: ignore
        else:
            self.socketio.emit("regrpa_status", {"status": "Desligado."}) # type: ignore
        memory_string = ""
        for message in self.memory:
            memory_string += message + "\n"
        self.socketio.emit("regrpa_terminal", {"message": memory_string}) # type: ignore
