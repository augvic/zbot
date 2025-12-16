from typing import Any, Callable

class EventBusEngine:
    
    def __init__(self) -> None:
        self.listeners = {}
    
    def emit(self, event: str, data: Any = None) -> None:
        try:
            if event in self.listeners:
                self.listeners[event](data)
        except Exception as error:
            raise Exception(f"❌ Error in (EventBusEngine) in (emit) method: {error}")
    
    def on(self, event: str, callable: Callable) -> None:
        try:
            self.listeners[event] = callable
        except Exception as error:
            raise Exception(f"❌ Error in (EventBusEngine) in (on) method: {error}")
    
    def remove_listener(self, event: str) -> None:
        try:
            self.listeners.pop(event)
        except Exception as error:
            raise Exception(f"❌ Error in (EventBusEngine) in (remove_listener) method: {error}")
