from threading import Thread
from flask_socketio import SocketIO
from time import sleep
from src.components.log_system import LogSystem
from datetime import datetime

class RunRegistrationsRpa:
    
    def _setup(self, socketio: SocketIO) -> None:
        self.is_running = False
        self.stop = False
        self.memory: list[str] = []
        self.day = datetime.now().date()
        self.socketio = socketio
        self.thread = Thread(target=self.loop)
        self.log_system = LogSystem("registrations_rpa")
    
    def execute(self, socketio: SocketIO) -> None:
        self._setup(socketio)
        self.thread.start()
        self.socketio.emit("regrpa_notification", {"success": True, "message": "RPA iniciado."})
        self.socketio.emit("regrpa_status", {"status": "Em processamento."})
        self.is_running = True
    
    def loop(self) -> None:
        try:
            while True:
                if self.day != datetime.now().date():
                    self.memory.clear()
                    self.day = datetime.now().date()
                if self.stop == True:
                    self.socketio.emit("regrpa_notification", {"success": True, "message": "RPA desligado."})
                    self.socketio.emit("regrpa_status", {"status": "Desligado."})
                    self.stop = False
                    self.is_running = False
                    break
                self.log_system.write("Em execução")
                sleep(2)
        except Exception as error:
            self.log_system.write(f"Erro durante execução: {error}")
            self.socketio.emit("regrpa_status", {"status": "Desligado."})
            self.socketio.emit("regrpa_notification", {"success": False, "message": "Erro durante execução do RPA."})
            self.stop = False
            self.is_running = False
