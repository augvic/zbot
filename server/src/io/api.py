from src.tasks.application.get_wsgi_application import GetWsgiApplication
from src.tasks.application.get_socketio_application import GetSocketIoApplication
from .routes.login import Login
from .routes.main import Main
from .routes.modules_list import ModulesList
from .routes.permissions import Permissions
from .routes.session_modules import SessionModules
from .routes.users import Users
from .routes.session_user import SessionUser
from .routes.registrations_rpa import RegistrationsRpa
from .routes.registrations import Registrations

class Api:
    
    def __init__(self):
        self.get_wsgi_application_task = GetWsgiApplication()
        self.get_socketio_application_task = GetSocketIoApplication()
        self.app = self.get_wsgi_application_task.execute()
        self.socketio = self.get_socketio_application_task.execute(self.app)
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
        Registrations(self.app)
