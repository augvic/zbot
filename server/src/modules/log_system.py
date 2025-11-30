from os import path, makedirs
from datetime import datetime
import sys

class LogSystem:
    
    def __init__(self, folder: str) -> None:
        try:
            if getattr(sys, "frozen", False):
                self.base_path = path.dirname(sys.executable)
            else:
                self.base_path = path.join(path.dirname(__file__), "..", "..")
            self.log_dir = path.abspath(path.join(self.base_path, "storage", ".logs", folder))
            makedirs(self.log_dir, exist_ok=True)
        except Exception as error:
            raise Exception(f"Error in (LogSystem) module in (__init__) method: {error}")
    
    def write_text(self, text: str) -> None:
        try:
            with open(f"{self.log_dir}/{datetime.now().replace(microsecond=0).strftime("%d-%m-%Y")}.txt", "a", encoding="utf-8") as self.log:
                self.log.write(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n" + text + "\n\n")
                self.log.flush()
        except Exception as error:
            raise Exception(f"Error in (LogSystem) module in (write_text) method: {error}")
    
    def write_error(self, error: str) -> None:
        try:
            with open(f"{self.log_dir}/{datetime.now().replace(microsecond=0).strftime("%d-%m-%Y")}_errors.txt", "a", encoding="utf-8") as self.log_errors:
                self.log_errors.write(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n" + error + "\n\n")
                self.log_errors.flush()
        except Exception as exception:
            raise Exception(f"Error in (LogSystem) module in (write_error) method: {exception}.")
