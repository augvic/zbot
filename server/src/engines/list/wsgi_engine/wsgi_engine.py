from flask import Flask, request, Request, render_template
from flask_socketio import SocketIO
from os import path, getenv
from dotenv import load_dotenv
from dataclasses import dataclass
import sys
import logging
import flask.cli

from .wsgi_session_manager_engine import WsgiSessionManagerEngine

from typing import Callable
from werkzeug.datastructures import FileStorage

@dataclass
class RequestProcessed:
    
    success: bool
    message: str
    data: dict[str, str]
    files: dict[str, FileStorage]


class WsgiEngine:
    
    def __init__(self):
        base_path = getattr(sys, "_MEIPASS", path.join(path.dirname(__file__), "..", ".."))
        load_dotenv(path.abspath(path.join(base_path, ".env")))
        BASE_DIR = path.dirname(path.abspath(__file__))
        STATIC = path.abspath(path.join(BASE_DIR, "../../../../storage/.web/storage"))
        TEMPLATE = path.abspath(path.join(BASE_DIR, "../../../../storage/.web"))
        self.app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)
        self.app.secret_key = getenv("FLASK")
        self.socketio = SocketIO(self.app, async_mode="threading")
        self.session_manager = WsgiSessionManagerEngine()
        flask.cli.show_server_banner = lambda *args: None
        self.log = logging.getLogger('werkzeug')
        self.log.setLevel(logging.ERROR)
    
    def run(self) -> None:
        try:
            self.socketio.run(self.app, host="127.0.0.1", debug=False, use_reloader=False)
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngine) in (run) method: {error}")
    
    def register_route(self, endpoint: str, methods: list[str], function: Callable) -> None:
        try:
            self.app.route(endpoint, methods=methods)(function)
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngine) in (register_route) method: {error}")
    
    def process_request(self, content_type: str, expected_data: list[str], expected_files: list[str]) -> RequestProcessed:
        try:
            data_dict = {}
            files_dict = {}
            if request.content_type is None:
                return RequestProcessed(success=False, message=f"❌ Endpoint ({request.endpoint}). Enviar conteúdo da requisição como ({content_type}).", data={}, files={})
            if content_type not in request.content_type:
                return RequestProcessed(success=False, message=f"❌ Endpoint ({request.endpoint}). Enviar conteúdo da requisição como ({content_type}).", data={}, files={})
            if content_type == "multipart/form-data":
                data_dict = request.form.to_dict()
                missing_data = set(expected_data) - set(data_dict.keys())
                if missing_data:
                    return RequestProcessed(success=False, message=f"❌ Endpoint ({request.endpoint}). Dados faltantes na requisição ({missing_data}).", data={}, files={})
                files_dict = request.files.to_dict()
                missing_files = set(expected_files) - set(files_dict.keys())
                if missing_files:
                    return RequestProcessed(success=False, message=f"❌ Endpoint ({request.endpoint}). Arquivos faltantes na requisição ({missing_files}).", data={}, files={})
            elif content_type == "application/json":
                data_dict = request.json
                if not data_dict:
                    return RequestProcessed(success=False, message=f"❌ Endpoint ({request.endpoint}). Corpo da requisição não foi enviado como JSON.", data={}, files={})
                missing_data = set(expected_data) - set(data_dict.keys())
                if missing_data:
                    return RequestProcessed(success=False, message=f"❌ Endpoint ({request.endpoint}). Dados faltantes na requisição ({missing_data}).", data={}, files={})
            else:
                return RequestProcessed(success=False, message=f"❌ Endpoint ({request.endpoint}). Enviar conteúdo da requisição como ({content_type}).", data={}, files={})
            return RequestProcessed(success=True, message=f"✅ Endpoint ({request.endpoint}). Content-Type ({content_type}). Expected Data ({expected_data}). Expected Files ({expected_files}). Requisição bem sucedida.", data=data_dict, files=files_dict)
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngine) in (process) method: {error}")
    
    def get_request(self) -> Request:
        try:
            return request
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngine) in (get_request) method: {error}")
    
    def get_endpoint(self) -> str | None:
        try:
            return request.endpoint
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngine) in (get_endpoint) method: {error}")
    
    def get_user_ip(self) -> str | None:
        try:
            return request.remote_addr
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngine) in (get_user_ip) method: {error}")
    
    def render_template(self, template: str) -> str:
        try:
            return render_template(template)
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngine) in (render) method: {error}")
        
    def emit_message(self, key: str, message: str) -> None:
        try:
            self.socketio.emit(key, {"message": message})
        except Exception as error:
            raise Exception(f"❌ Error in (WsgiEngine) in (emit_message) method: {error}")
