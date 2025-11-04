from flask import request
from .models import RequestProcessed

class RequestProcessor:
    
    def process(self, content_type: str, expected_data: list[str], expected_files: list[str], optional_data: list[str], optional_files: list[str]) -> RequestProcessed:
        data_dict = {}
        files_dict = {}
        try:
            if request.content_type is None:
                return RequestProcessed(success=False, message=f"Endpoint: '{request.endpoint}'. Enviar conteúdo da requisição como: {content_type}.", data={}, files={})
            if content_type not in request.content_type:
                return RequestProcessed(success=False, message=f"Endpoint: '{request.endpoint}'. Enviar conteúdo da requisição como: {content_type}.", data={}, files={})
            if content_type == "multipart/form-data":
                data_dict = request.form.to_dict()
                missing_data = set(expected_data) - set(data_dict.keys())
                if missing_data:
                    return RequestProcessed(success=False, message=f"Endpoint: '{request.endpoint}'. Dados faltantes na requisição: '{missing_data}'.", data={}, files={})
                files_dict = request.files.to_dict()
                missing_files = set(expected_files) - set(files_dict.keys())
                if missing_files:
                    return RequestProcessed(success=False, message=f"Endpoint: '{request.endpoint}'. Arquivos faltantes na requisição: '{missing_files}'.", data={}, files={})
            elif content_type == "application/json":
                data_dict = request.json
                if not data_dict:
                    return RequestProcessed(success=False, message=f"Endpoint: '{request.endpoint}'. Corpo da requisição não foi enviado como JSON.", data={}, files={})
                missing_data = set(expected_data) - set(data_dict.keys())
                if missing_data:
                    return RequestProcessed(success=False, message=f"Endpoint: '{request.endpoint}'. Dados faltantes na requisição: '{missing_data}'.", data={}, files={})
            else:
                return RequestProcessed(success=False, message="Endpoint: '{request.endpoint}'. Enviar conteúdo da requisição como: {content_type}.", data={}, files={})
            return RequestProcessed(success=True, message=f"\n- Endpoint: '{request.endpoint}'\n- Content-Type: '{content_type}'\n- Expected Data: {expected_data}\n- Expected Files: {expected_files}", data=data_dict, files=files_dict)
        except Exception as error:
            raise Exception(f"\n- Endpoint: '{request.endpoint}'\n- Content-Type: '{content_type}'\n- Form: {request.form.to_dict()}\n- Files: {request.files.to_dict()}\n- JSON: {request.json}\n- Expected Data: {expected_data}\n- Expected Files: {expected_files}\nError Detailed: {error}")
