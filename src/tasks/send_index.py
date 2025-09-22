from src.infrastructure.file_systems import BundleSender, SessionManager
from flask import Response, redirect

class SendIndex:
    
    def _setup(self) -> None:
        self.bundle_sender = BundleSender()
        self.session_manager = SessionManager()
    
    def execute(self) -> Response:
        self._setup()
        if not self.session_manager.is_user_in_session():
            return redirect("/")
        return self.bundle_sender.send_index()
