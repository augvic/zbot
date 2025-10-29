from flask import Flask
from os import path, getenv
from dotenv import load_dotenv

class WsgiApplication(Flask):
    
    def __init__(self):
        load_dotenv()
        BASE_DIR = path.dirname(path.abspath(__file__))
        STATIC = path.abspath(path.join(BASE_DIR, "../../storage/.web/storage"))
        TEMPLATE = path.abspath(path.join(BASE_DIR, "../../storage/.web"))
        super().__init__(__name__, template_folder=TEMPLATE, static_folder=STATIC)
        self.secret_key = getenv("FLASK")