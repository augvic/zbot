from flask import Flask
from .routes.login import login
from os import path, getenv
from dotenv import load_dotenv

class Api:
    
    def __init__(self):
        load_dotenv()
        BASE_DIR = path.dirname(path.abspath(__file__))
        STATIC = path.abspath(path.join(BASE_DIR, "../../storage/.web_output/static"))
        TEMPLATE = path.abspath(path.join(BASE_DIR, "../../storage/.web_output/template"))
        self.app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)
        self.app.secret_key = getenv("FLASK")
        self.app.register_blueprint(login)
        self.app.run(debug=True)

Api()
