from flask import Flask
from os import path, getenv
from dotenv import load_dotenv
import sys

class WsgiApplication(Flask):
    
    def __init__(self):
        try:
            base_path = getattr(sys, "_MEIPASS", path.join(path.dirname(__file__), "..", "..", ".."))
            load_dotenv(path.abspath(path.join(base_path, ".env")))
            BASE_DIR = path.dirname(path.abspath(__file__))
            STATIC = path.abspath(path.join(BASE_DIR, "../../storage/.web/storage"))
            TEMPLATE = path.abspath(path.join(BASE_DIR, "../../storage/.web"))
            super().__init__(__name__, template_folder=TEMPLATE, static_folder=STATIC)
            self.secret_key = getenv("FLASK")
        except Exception as error:
            raise Exception(f"Error in (WsgiApplication) component in (__init__) method: {error}.")