from threading import Thread
from typing import Any, Callable, Iterable, Mapping

class ApplicationThread(Thread):
    
    def __init__(self, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = [], kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
        try:
            super().__init__(group, target, name, args, kwargs, daemon=daemon)
        except Exception as error:
            raise Exception(f"Error in (ApplicationThread) component in (__init__) method: {error}.")
