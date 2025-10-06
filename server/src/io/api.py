from flask import Flask
from .routes.login import login
from .routes.main import main
from .routes.module_bundle import module_bundle
from .routes.modules_list import modules_list
from .routes.page_bundle import page_bundle
from .routes.permissions import permissions
from .routes.session_modules import session_modules
from .routes.users import users
from .routes.session_user import session_user
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
        self.app.register_blueprint(login)
        self.app.register_blueprint(main)
        self.app.register_blueprint(module_bundle)
        self.app.register_blueprint(modules_list)
        self.app.register_blueprint(page_bundle)
        self.app.register_blueprint(permissions)
        self.app.register_blueprint(session_modules)
        self.app.register_blueprint(users)
        self.app.register_blueprint(session_user)
        self.app.run(debug=True)

Api()
