from threading import Thread
from typing import Callable

class ApplicationThread(Thread):
    
    def start(self, target: Callable[..., object], *args, **kwargs) -> None:
        try:
            super().__init__(target=target, args=args, kwargs=kwargs)
        except Exception as error:
            raise Exception(f"Error in (ApplicationThread) component in (__init__) method: {error}.")
