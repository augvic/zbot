from flask import Flask
from flask_socketio import SocketIO
from .routes.login import login
from .routes.main import main
from .routes.module_bundle import module_bundle
from .routes.modules_list import modules_list
from .routes.page_bundle import page_bundle
from .routes.permissions import permissions
from .routes.session_modules import session_modules
from .routes.users import users
from .routes.session_user import session_user
from .routes.credit_rpa import CreditRpa
from os import path, getenv
from dotenv import load_dotenv

class Api:
    
    def __init__(self):
        load_dotenv()
        BASE_DIR = path.dirname(path.abspath(__file__))
        STATIC = path.abspath(path.join(BASE_DIR, "../storage/.web_output/static"))
        TEMPLATE = path.abspath(path.join(BASE_DIR, "../storage/.web_output/template"))
        self.app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)
        self.app.secret_key = getenv("FLASK")
        self.register_routes()
        self.socketio = SocketIO(self.app)
        self.register_web_socket_events()
        self.socketio.run(self.app, host="127.0.0.1", debug=True) # type: ignore

    def register_routes(self) -> None:
        self.app.register_blueprint(login)
        self.app.register_blueprint(main)
        self.app.register_blueprint(module_bundle)
        self.app.register_blueprint(modules_list)
        self.app.register_blueprint(page_bundle)
        self.app.register_blueprint(permissions)
        self.app.register_blueprint(session_modules)
        self.app.register_blueprint(users)
        self.app.register_blueprint(session_user)
    
    def register_web_socket_events(self) -> None:
        CreditRpa(self.socketio)

Api()
