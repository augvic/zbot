from flask import Flask
from flask_socketio import SocketIO
from os import path, getenv
from dotenv import load_dotenv
import sys

from typing import Callable

class WsgiApplication:
    
    def __init__(self):
        base_path = getattr(sys, "_MEIPASS", path.join(path.dirname(__file__), "..", "..", ".."))
        load_dotenv(path.abspath(path.join(base_path, ".env")))
        BASE_DIR = path.dirname(path.abspath(__file__))
        STATIC = path.abspath(path.join(BASE_DIR, "../../../storage/.web/storage"))
        TEMPLATE = path.abspath(path.join(BASE_DIR, "../../../storage/.web"))
        self.app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)
        self.app.secret_key = getenv("FLASK")
        self.socketio = SocketIO(self.app)
    
    def run(self) -> None:
        try:
            self.socketio.run(self.app, host="127.0.0.1", debug=True)
        except Exception as error:
            raise Exception(f"Error in (WsgiApplication) module in (run) method: {error}")
    
    def register_route(self, endpoint: str, methods: list[str], function: Callable) -> None:
        try:
            self.app.route(endpoint, methods=methods)(function)
        except Exception as error:
            raise Exception(f"Error in (WsgiApplication) module in (register_route) method: {error}")