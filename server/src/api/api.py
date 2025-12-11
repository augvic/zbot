from src.rpas.rpas import Rpas
from src.engines.engines import Engines
from src.tasks.tasks import Tasks

from .routes.login_route import LoginRoute
from .routes.main_route import MainRoute
from .routes.modules_route import ModulesRoute
from .routes.permissions_route import PermissionsRoute
from .routes.registrations_rpa_route import RegistrationsRpaRoute
from .routes.registrations_route import RegistrationsRoute
from .routes.session_modules_route import SessionModulesRoute
from .routes.session_user_route import SessionUserRoute
from .routes.users_route import UsersRoute

class Api:
    
    def __init__(self, engines: Engines, tasks: Tasks, rpas: Rpas) -> None:
        self.engines = engines
        self.tasks = tasks
        self.rpas = rpas
        self.login_route = LoginRoute(tasks=self.tasks, engines=self.engines)
        self.main_route = MainRoute(engines=self.engines)
        self.modules_route = ModulesRoute(tasks=self.tasks, engines=self.engines)
        self.permissions_route = PermissionsRoute(tasks=self.tasks, engines=self.engines)
        self.session_modules_route = SessionModulesRoute(tasks=self.tasks, engines=self.engines)
        self.users_route = UsersRoute(tasks=self.tasks, engines=self.engines)
        self.session_user_route = SessionUserRoute(tasks=self.tasks, engines=self.engines)
        self.registrations_rpa_route = RegistrationsRpaRoute(rpas=self.rpas, engines=self.engines)
        self.registrations_route = RegistrationsRoute(tasks=self.tasks, engines=self.engines)
    
    def main(self) -> None:
        self.engines.wsgi_engine.run()
