from threading import Thread
from time import sleep

class CreditRpa:
    
    def _setup(self) -> None:
        self.thread = Thread(target=self.loop)
    
    def execute(self) -> None:
        self._setup()
        pass
    
    def loop(self) -> None:
        print("Em execução.")
        sleep(3)