from threading import Thread
from time import sleep
from typing import TYPE_CHECKING
from src.infrastructure.log_system import LogSystem
from datetime import datetime

if TYPE_CHECKING:
    from io.routes.regrpa_websocket import RegRpaWebsocket

class RunRegistrationsRpa:
    
    def _setup(self, rpa: "RegRpaWebsocket") -> None:
        self.day = datetime.now().date()
        self.rpa = rpa
        self.thread = Thread(target=self.loop)
        self.log_system = LogSystem("registrations_rpa", self.rpa.socketio, self.rpa.memory)
    
    def execute(self, rpa: "RegRpaWebsocket") -> None:
        self._setup(rpa)
        try:
            self.thread.start()
            self.rpa.socketio.emit("regrpa_notification", {"success": True, "message": "RPA iniciado."}) # type: ignore
            self.rpa.socketio.emit("regrpa_status", {"status": "Em processamento."}) # type: ignore
            self.rpa.is_running = True
        except:
            self.rpa.socketio.emit("regrpa_status", {"status": "Desligado."}) # type: ignore
            self.rpa.socketio.emit("regrpa_notification", {"success": False, "message": "Erro ao iniciar RPA."}) # type: ignore
    
    def loop(self) -> None:
        while True:
            if self.day != datetime.now().date():
                self.rpa.memory.clear()
                self.day = datetime.now().date()
            if self.rpa.stop == True:
                self.rpa.socketio.emit("regrpa_notification", {"success": True, "message": "RPA desligado."}) # type: ignore
                self.rpa.socketio.emit("regrpa_status", {"status": "Desligado."}) # type: ignore
                self.rpa.stop = False
                self.rpa.is_running = False
                break
            self.log_system.write("Em execução", "regrpa_terminal")
            sleep(2)
