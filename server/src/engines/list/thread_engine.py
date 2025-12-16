from threading import Thread

from typing import Callable

class ThreadEngine:
    
    def __init__(self) -> None:
        self.threads: list[Thread] = []
    
    def add_thread(self, target: Callable[..., object], *args, **kwargs) -> None:
        try:
            self.threads.append(Thread(target=target, daemon=True, *args, **kwargs))
        except Exception as error:
            raise Exception(f"❌ Error in (ThreadEngine) in (add_thread) method: {error}")
    
    def start_threads(self) -> None:
        try:
            for thread in self.threads:
                thread.start()
        except Exception as error:
            raise Exception(f"❌ Error in (ThreadEngine) in (start_threads) method: {error}")
        
    def start_single_thread(self, target: Callable[..., object], *args, **kwargs) -> None:
        try:
            thread = Thread(target=target, daemon=True, *args, **kwargs)
            thread.start()
        except Exception as error:
            raise Exception(f"❌ Error in (ThreadEngine) in (start_single_thread) method: {error}")
