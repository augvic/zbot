from src.components.logic.request_processor.component import RequestProcessor
from src.components.file_system.log_system import LogSystem
from src.components.infra.session_manager import SessionManager
from src.components.infra.request_manager import RequestManager
from .models import Response
from typing import cast

class ProcessRequest:
    
    def __init__(self) -> None:
        self.request_processor = RequestProcessor()
        self.log_system = LogSystem("application/process_request")
        self.session_manager = SessionManager()
        self.request_manager = RequestManager()
    
    def execute(self, content_type: str, expected_data: list[str], expected_files: list[str], optional_data: list[str], optional_files: list[str]) -> Response:
        try:
            user = self.session_manager.get_from_session("user")
        except:
            request_dict = cast(dict, self.request_manager.get_request().json)
            user = cast(str, request_dict["user"])
        try:
            request_processed = self.request_processor.process(content_type, expected_data, expected_files, optional_data, optional_files)
            if request_processed.success:
                self.log_system.write_text(f"👤 Por usuário ({user}): ✅ Requisição bem sucedida: {request_processed.message}")
                return Response(success=True, message=f"✅ Requisição bem sucedida: {request_processed.message}", data=request_processed.data, files=request_processed.files)
            else:
                self.log_system.write_text(f"👤 Por usuário ({user}): ❌ Requisição inválida: {request_processed.message}")
                return Response(success=False, message=f"❌ Requisição inválida: {request_processed.message}", data={}, files={})
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário ({user}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao processar requisição. Contate o administrador.")
