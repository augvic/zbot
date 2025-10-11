from flask_socketio import SocketIO
from src.tasks.run_registrations_rpa import RunRegistrationsRpa
from typing import Any

class RegRpaWebsocket:
    
    def __init__(self, socketio: SocketIO) -> None:
        self.is_running = False
        self.stop = False
        self.memory: list[str] = []
        self.socketio = socketio
        self.socketio.on_event("regrpa_refresh", self.refresh)
        self.socketio.on_event("regrpa_start", self.update_status_to_on)
        self.socketio.on_event("regrpa_stop", self.update_status_to_off)
    
    def update_status_to_on(self, data: Any = None) -> None:
        if self.is_running == True:
            self.socketio.emit("regrpa_notification", {"success": False, "message": "RPA já está em processamento."})
            return
        self.socketio.emit("regrpa_status", {"status": "Iniciando..."})
        task = RunRegistrationsRpa()
        task.execute(self)
    
    def update_status_to_off(self, data: Any = None) -> None:
        if self.is_running == False:
            self.socketio.emit("regrpa_notification", {"message": "RPA já está desligado."})    
            return
        self.socketio.emit("regrpa_status", {"status": "Desligando..."})
        self.stop = True
    
    def refresh(self, data: Any = None) -> None:
        if self.is_running == True:
            self.socketio.emit("regrpa_status", {"status": "Em processamento."})
        else:
            self.socketio.emit("regrpa_status", {"status": "Desligado."})
        memory_string = ""
        for message in self.memory:
            memory_string += message + "\n"
        self.socketio.emit("regrpa_terminal", {"message": memory_string})
