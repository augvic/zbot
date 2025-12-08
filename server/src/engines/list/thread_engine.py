from threading import Thread

from typing import Callable

class ThreadEngine:
    
    def __init__(self) -> None:
        self.threads: list[Thread] = []
    
    def add_thread(self, target: Callable[..., object], *args, **kwargs) -> None:
        try:
            self.threads.append(Thread(target=target, *args, **kwargs))
        except Exception as error:
            raise Exception(f"❌ Error in (ThreadEngine) engine in (add_thread) method: {error}")
    
    def start_threads(self) -> None:
        try:
            for thread in self.threads:
                thread.start()
        except Exception as error:
            raise Exception(f"❌ Error in (ThreadEngine) engine in (start_threads) method: {error}")
        
    def start_single_thread(self, target: Callable[..., object], *args, **kwargs) -> None:
        try:
            thread = Thread(target=target, *args, **kwargs)
            thread.start()
        except Exception as error:
            raise Exception(f"❌ Error in (ThreadEngine) engine in (start_single_thread) method: {error}")
