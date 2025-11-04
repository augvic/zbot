from src.components.infra.socketio_application import SocketIoApplication
from src.components.infra.wsgi_application import WsgiApplication
from src.io.api.login import Login
from src.io.api.main import Main
from src.io.api.modules_list import ModulesList
from src.io.api.permissions import Permissions
from src.io.api.session_modules import SessionModules
from src.io.api.users import Users
from src.io.api.session_user import SessionUser
from src.io.api.registrations_rpa import RegistrationsRpa
from src.io.api.registrations import Registrations

app = WsgiApplication()
socketio = SocketIoApplication(app)
Login().register(app)
Main().register(app)
ModulesList().register(app)
Permissions().register(app)
SessionModules().register(app)
Users().register(app)
SessionUser().register(app)
RegistrationsRpa().register(app, socketio)
Registrations().register(app)
socketio.run(app, host="127.0.0.1", debug=True)
