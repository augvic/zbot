from src.infrastructure.storage_managers.bundle_manager import BundleManager
from src.io.session_manager import SessionManager
from flask import Response
from datetime import datetime

class SendPage:
    
    def _setup(self) -> None:
        self.bundle_sender = BundleManager()
        self.session_manager = SessionManager()
    
    def execute(self, page: str) -> Response | str:
        self._setup()
        try:
            return self.bundle_sender.send_page(page)
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return "Erro ao enviar página."
