from .components import Components
from .tasks import Tasks
from .io import IO

class Controller:
    
    def __init__(self) -> None:
        self.components = Components()
        self.tasks = Tasks(self.components)
        self.io = IO(self.tasks)
    
    def run_process(self) -> None:
        self.components.app.route("/", methods=["GET"])(self.io.main_route.render_application)
        self.components.app.route("/modules-list", methods=["GET"])(self.io.modules_list_route.get_modules_list)
        self.components.app.route("/modules-list", methods=["POST"])(self.io.modules_list_route.create_module)
        self.components.app.route("/modules-list/<module>", methods=["DELETE"])(self.io.modules_list_route.delete_module)
        self.components.app.route("/permissions/<user>", methods=["GET"])(self.io.permissions_route.get_user_permissions)
        self.components.app.route("/permissions/<user>/<permission>", methods=["POST"])(self.io.permissions_route.create_user_permission)
        self.components.app.route("/permissions/<user>/<permission>", methods=["DELETE"])(self.io.permissions_route.delete_user_permission)
        self.components.app.route("/registrations-rpa", methods=["GET"])(self.io.registrations_rpa_route.refresh)
        self.components.app.route("/registrations-rpa", methods=["POST"])(self.io.registrations_rpa_route.turn_on)
        self.components.app.route("/registrations-rpa", methods=["DELETE"])(self.io.registrations_rpa_route.turn_off)
        self.components.app.route("/registrations", methods=["POST"])(self.io.registrations_route.include_registration)
        self.components.app.route("/registrations/<cnpj>", methods=["GET"])(self.io.registrations_route.get_registration)
        self.components.app.route("/registrations/<cnpj>", methods=["DELETE"])(self.io.registrations_route.delete_registration)
        self.components.app.route("/registrations", methods=["PUT"])(self.io.registrations_route.update_registration)
        self.components.app.route("/session-modules", methods=["GET"])(self.io.session_modules_route.get_session_modules)
        self.components.app.route("/session-user", methods=["GET"])(self.io.session_user_route.get_session_user)
        self.components.app.route("/users/<user>", methods=["GET"])(self.io.users_route.get_user)
        self.components.app.route("/users", methods=["POST"])(self.io.users_route.create_user)
        self.components.app.route("/users/<user>", methods=["DELETE"])(self.io.users_route.delete_user)
        self.components.app.route("/users", methods=["PUT"])(self.io.users_route.update_user)
        self.components.socketio.run(self.components.app, host="127.0.0.1", debug=True)
