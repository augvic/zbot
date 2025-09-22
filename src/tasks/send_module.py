from src.infrastructure.file_systems import BundleSender, SessionManager
from flask import Response

class SendModule:
    
    def _setup(self) -> None:
        self.bundle_sender = BundleSender()
        self.session_manager = SessionManager()
    
    def execute(self, module: str) -> Response:
        self._setup()
        if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access(module):
            return "Sem autorização.", 401
        return self.bundle_sender.send_module(module)
