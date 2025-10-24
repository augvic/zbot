from src.components.request_processor import RequestProcessor
from src.components.log_system import LogSystem
from src.components.session_manager import SessionManager
from src.components.request_manager import RequestManager

from .models import Response

from typing import cast

class ProcessRequest:
    
    def __init__(self) -> None:
        self.request_processor = RequestProcessor()
        self.log_system = LogSystem("process_request")
        self.session_manager = SessionManager()
        self.request_manager = RequestManager()
    
    def execute(self, content_type: str, expected_data: list[str], expected_files: list[str], optional: list[str]) -> Response:
        try:
            user = self.session_manager.get_from_session("user")
        except:
            request_dict = cast(dict, self.request_manager.get_request().json)
            user = cast(str, request_dict["user"])
        try:
            request_processed = self.request_processor.process(content_type, expected_data, expected_files, optional)
            if request_processed.success:
                self.log_system.write_text(f"👤 Por usuário: {user}.\n✅ Requisição bem sucedida:\n{request_processed.message}")
                return Response(success=True, message=f"✅ Requisição bem sucedida:\n{request_processed.message}", data=request_processed.data, files=request_processed.files)
            else:
                self.log_system.write_text(f"👤 Por usuário: {user}.\n❌ Requisição inválida: {request_processed.message}")
                return Response(success=False, message=f"❌ Requisição inválida: {request_processed.message}")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {user}.\n❌ Erro:\n{error}")
            raise Exception("❌ Erro interno ao processar requisição. Contate o administrador.")
