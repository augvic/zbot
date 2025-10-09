from typing import Any
from os import path, makedirs
from datetime import datetime

class LogSystem:
    
    def __init__(self, folder: str, socket: Any = None, memory: list[str] | None = None) -> None:
        log_dir = path.abspath(path.join(path.dirname(__file__), "..", "storage", ".logs", folder))
        makedirs(log_dir, exist_ok=True)
        self.log = open(f"{log_dir}/{datetime.now().replace(microsecond=0).strftime("%d-%m-%Y")}.txt", "a", encoding="utf-8")
        self.socket = None
        self.memory = None
        if socket:
            self.socket = socket
        if memory != None:
            self.memory = memory
    
    def write(self, text: str, socket_channel: str | None = None) -> None:
        self.log.write(text + "\n")
        self.log.flush()
        if socket_channel and self.socket:
            self.socket.emit(socket_channel, {"message": text})
        if self.memory != None:
            self.memory.append(text)
