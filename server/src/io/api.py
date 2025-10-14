from flask import Flask
from flask_socketio import SocketIO
from .routes.login import Login
from .routes.main import Main
from .routes.modules_list import ModulesList
from .routes.permissions import Permissions
from .routes.session_modules import SessionModules
from .routes.users import Users
from .routes.session_user import SessionUser
from .routes.registrations_rpa import RegistrationsRpa
from os import path, getenv
from dotenv import load_dotenv

class Api:
    
    def __init__(self):
        load_dotenv()
        BASE_DIR = path.dirname(path.abspath(__file__))
        STATIC = path.abspath(path.join(BASE_DIR, "../../storage/.web/storage"))
        TEMPLATE = path.abspath(path.join(BASE_DIR, "../../storage/.web"))
        self.app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)
        self.socketio = SocketIO(self.app)
        self.app.secret_key = getenv("FLASK")
        self.register_routes()
        self.socketio.run(self.app, host="127.0.0.1", debug=True)
    
    def register_routes(self) -> None:
        Login(self.app)
        Main(self.app)
        ModulesList(self.app)
        Permissions(self.app)
        SessionModules(self.app)
        Users(self.app)
        SessionUser(self.app)
        RegistrationsRpa(self.app, self.socketio)
