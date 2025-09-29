from flask import Flask
from .routes import *
from os import path, getenv
from dotenv import load_dotenv

class Api:
    
    def __init__(self):
        load_dotenv()
        BASE_DIR = path.dirname(path.abspath(__file__))
        STATIC = path.abspath(path.join(BASE_DIR, "../../../.javascript/io/static"))
        TEMPLATE = path.abspath(path.join(BASE_DIR, "../../../.javascript/io/template"))
        self.app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)
        self.app.secret_key = getenv("FLASK")
        self.index_route = Pages(self.app)
        self.login_route = Login(self.app)
        self.main_route = Main(self.app)
        self.modules_allowed_route = ModulesAllowed(self.app)
        self.modules_route = ModuleBundle(self.app)
        self.modules_list_route = ModulesList(self.app)
        self.permissions_route = Permissions(self.app)
        self.users_route = Users(self.app)
        self.app.run(debug=True)

Api()
