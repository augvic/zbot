from flask import Flask
from flask_socketio import SocketIO
from os import path, getenv
from dotenv import load_dotenv
import sys

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