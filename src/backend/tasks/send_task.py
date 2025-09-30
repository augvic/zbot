from src.backend.infrastructure.managers import BundleManager, SessionManager
from flask import Response

class SendTask:
    
    def _setup(self) -> None:
        self.bundle_sender = BundleManager()
        self.session_manager = SessionManager()
    
    def execute(self, task: str) -> Response:
        self._setup()
        return self.bundle_sender.send_task(task)
