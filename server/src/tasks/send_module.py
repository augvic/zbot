from src.infrastructure.storage_managers.bundle_manager import BundleManager
from src.infrastructure.session_manager import SessionManager
from flask import Response
from datetime import datetime

class SendModule:
    
    def _setup(self) -> None:
        self.bundle_sender = BundleManager()
        self.session_manager = SessionManager()
    
    def execute(self, module: str) -> Response | str:
        self._setup()
        try:
            return self.bundle_sender.send_module(module)
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return "Erro ao enviar módulo."
