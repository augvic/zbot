from threading import Thread
from time import sleep
from typing import TYPE_CHECKING
from src.infrastructure.log_system import LogSystem
from datetime import datetime

if TYPE_CHECKING:
    from io.routes.regrpa_websocket import RegRpaWebsocket

class RunRegistrationsRpa:
    
    def _setup(self, rpa_websocket: "RegRpaWebsocket") -> None:
        self.day = datetime.now().date()
        self.rpa_websocket = rpa_websocket
        self.thread = Thread(target=self.loop)
        self.log_system = LogSystem("registrations_rpa", self.rpa_websocket.socketio, self.rpa_websocket.memory)
    
    def execute(self, rpa_websocket: "RegRpaWebsocket") -> None:
        self._setup(rpa_websocket)
        self.thread.start()
        self.rpa_websocket.socketio.emit("regrpa_notification", {"success": True, "message": "RPA iniciado."}) # type: ignore
        self.rpa_websocket.socketio.emit("regrpa_status", {"status": "Em processamento."}) # type: ignore
        self.rpa_websocket.is_running = True
    
    def loop(self) -> None:
        try:
            while True:
                if self.day != datetime.now().date():
                    self.rpa_websocket.memory.clear()
                    self.day = datetime.now().date()
                if self.rpa_websocket.stop == True:
                    self.rpa_websocket.socketio.emit("regrpa_notification", {"success": True, "message": "RPA desligado."}) # type: ignore
                    self.rpa_websocket.socketio.emit("regrpa_status", {"status": "Desligado."}) # type: ignore
                    self.rpa_websocket.stop = False
                    self.rpa_websocket.is_running = False
                    break
                self.log_system.write("Em execução", True, "regrpa_terminal")
                sleep(2)
        except Exception as error:
            self.log_system.write(f"Erro durante execução: {error}", False, None)
            self.rpa_websocket.socketio.emit("regrpa_status", {"status": "Desligado."}) # type: ignore
            self.rpa_websocket.socketio.emit("regrpa_notification", {"success": False, "message": "Erro durante execução do RPA."}) # type: ignore
