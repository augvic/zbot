from os import path, makedirs
from datetime import datetime

class LogSystem:
    
    def __init__(self, folder: str) -> None:
        log_dir = path.abspath(path.join(path.dirname(__file__), "..", ".." "storage", ".logs", folder))
        makedirs(log_dir, exist_ok=True)
        self.log = open(f"{log_dir}/{datetime.now().replace(microsecond=0).strftime("%d-%m-%Y")}.txt", "a", encoding="utf-8")
    
    def write(self, text: str) -> None:
        self.log.write(text + "\n")
        self.log.flush()
