from threading import Thread
from time import sleep
from typing import Any

class RunCreditRpa:
    
    def _setup(self, rpa: Any) -> None:
        self.rpa = rpa
        self.thread = Thread(target=self.loop)
    
    def execute(self, rpa: Any) -> None:
        self._setup(rpa)
        self.thread.start()
        
    
    def loop(self) -> None:
        while True:
            if self.rpa.stop == True:
                self.rpa.socketio.emit("zcredrpa_notification", {"success": True, "message": "RPA desligado."}) # type: ignore
                self.rpa.socketio.emit("zcredrpa_status", {"status": "Desligado."}) # type: ignore
                self.rpa.stop = False
                self.rpa.is_running = False
                break
            self.rpa.socketio.emit("zcredrpa_terminal", {"message": "Em execução."}) # type: ignore
            sleep(3)
