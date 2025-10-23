from flask import request
from .models import RequestProcessed

from typing import cast
from werkzeug.datastructures import FileStorage

class RequestProcessor:

    def process(self, content_type: str, expected_data: list[str], not_expected_data: list[str], expected_files: list[str], not_expected_files: list[str]) -> RequestProcessed:
        data_dict = {}
        files_dict = {}
        if request.content_type is None:
            return RequestProcessed(success=False, message=f"Tipo de conteúdo da requisição deve ser: {content_type}.", data={}, files={})
        if not content_type in request.content_type:
            return RequestProcessed(success=False, message=f"Tipo de conteúdo da requisição deve ser: {content_type}.", data={}, files={})
        if content_type == "multipart/form-data":
            data_dict = request.form.to_dict()
            missing_data = expected_data - data_dict.keys()
            if missing_data:
                return RequestProcessed(success=False, message=f"Dados faltantes na requisição: '{missing_data}'.", data={}, files={})
            files_dict = request.files.to_dict()
            missing_files = expected_files - files_dict.keys()
            if missing_files:
                return RequestProcessed(success=False, message=f"Dados faltantes na requisição: '{missing_data}'.", data={}, files={})
        elif content_type == "application/json":
            data_dict = cast(dict[str, str], request.json)
            missing_data = expected_data - data_dict.keys()
            if missing_data:
                return RequestProcessed(success=False, message=f"Dados faltantes na requisição: '{missing_data}'.", data={}, files={})
        else:
            return RequestProcessed(success=False, message="Tipo de conteúdo da requisição é inválido.", data={}, files={})
        for key, value in data_dict.items():
            if not value and key in expected_data:
                return RequestProcessed(success=False, message=f"Chave: '{key}' obrigatória da requisição não possui valor.", data={}, files={})
        for key, value in files_dict.items():
            if not value or not value.filename and key in expected_data:
                return RequestProcessed(success=False, message=f"Chave: '{key}' obrigatória da requisição não possui valor.", data={}, files={})
        for key, value in data_dict.items():
            if key in not_expected_data and not value:
                return RequestProcessed(success=False, message=f"Chave: '{key}' é opcional. Mas para passar como nulo envie como '-' (hífen).", data={}, files={})
        for key, value in files_dict.items():
            if key in not_expected_files and value.filename == key:
                value = "-"
                return RequestProcessed(success=False, message=f"Chave: '{key}' é opcional. Mas para passar como nulo envie como '-' (hífen).", data={}, files={})
        return RequestProcessed(success=True, message="Sucesso.", data=data_dict, files=files_dict)
