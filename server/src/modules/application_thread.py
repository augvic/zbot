from threading import Thread

from typing import Callable

class ApplicationThread(Thread):
    
    def init(self, target: Callable[..., object], *args, **kwargs) -> None:
        try:
            super().__init__(target=target, *args, **kwargs)
        except Exception as error:
            raise Exception(f"Error in (ApplicationThread) module in (init) method: {error}")
