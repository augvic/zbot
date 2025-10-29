from os import path, makedirs
from datetime import datetime
import sys

class LogSystem:
    
    def __init__(self, folder: str) -> None:
        if getattr(sys, "frozen", False):
            base_path = path.dirname(sys.executable)
        else:
            base_path = path.join(path.dirname(__file__), "..", "..")
        log_dir = path.abspath(path.join(base_path, "storage", ".logs", folder))
        makedirs(log_dir, exist_ok=True)
        self.log = open(f"{log_dir}/{datetime.now().replace(microsecond=0).strftime("%d-%m-%Y")}.txt", "a", encoding="utf-8")
        self.log_errors = open(f"{log_dir}/{datetime.now().replace(microsecond=0).strftime("%d-%m-%Y")}_errors.txt", "a", encoding="utf-8")
    
    def write_text(self, text: str) -> None:
        self.log.write(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n" + text + "\n\n")
        self.log.flush()
    
    def write_error(self, error: str) -> None:
        self.log_errors.write(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n" + error + "\n\n")
        self.log_errors.flush()
