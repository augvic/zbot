from src.infrastructure.managers import BundleManager, SessionManager
from flask import Response

class SendPage:
    
    def _setup(self) -> None:
        self.bundle_sender = BundleManager()
        self.session_manager = SessionManager()
    
    def execute(self, page: str) -> Response:
        self._setup()
        if page == "zindex.js":
            if not self.session_manager.is_user_in_session():
                return "Necessário logar.", 401
        return self.bundle_sender.send_page(page)
