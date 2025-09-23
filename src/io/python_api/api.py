from flask import Flask
from .routes import *
from os import path, getenv
from dotenv import load_dotenv

class Api:
    
    def __init__(self):
        load_dotenv()
        BASE_DIR = path.dirname(path.abspath(__file__))
        TEMPLATES_DIR = path.abspath(path.join(BASE_DIR, "../../storage/web/templates"))
        STATIC_DIR = path.abspath(path.join(BASE_DIR, "../../storage/web/.javascript/static"))
        self.app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
        self.app.secret_key = getenv("FLASK")
        self.index_route = Index(self.app)
        self.login_route = Login(self.app)
        self.main_route = Main(self.app)
        self.modules_allowed_route = ModulesAllowed(self.app)
        self.modules_route = Modules(self.app)
        self.users_route = Users(self.app)
        self.app.run(debug=True)

Api()
