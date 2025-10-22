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
    
    def _message(self, text: str) -> None:
        self.log_system.write(text)
        self.memory.append(text)
        self.socketio.emit("regrpa_terminal", text)
    
    def memory_to_str(self) -> str:
        memory_string = ""
        for message in self.memory:
            memory_string += message + "\n"
        return memory_string
    
    def execute(self, socketio: SocketIO) -> None:
        self._setup(socketio)
        self.socketio.emit("regrpa_status", {"status": "Iniciando..."})
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
                self._message("Em execução")
                sleep(2)
        except Exception as error:
            self.log_system.write_error(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}")
            self.socketio.emit("regrpa_status", {"status": "Desligado."})
            self.socketio.emit("regrpa_notification", {"success": False, "message": "Erro durante execução do RPA."})
            self.stop = False
            self.is_running = False
