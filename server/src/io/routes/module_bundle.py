from flask import Flask, Response
from src.tasks import SendModule

class ModuleBundle:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/module-bundle/<module>", methods=["GET"])
        def get_module_bundle(module) -> Response:
            moduleUpperCase = (module[0] + module[1].upper() + module[2:]).replace(".js", "")
            if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access(moduleUpperCase):
                return "Sem autorização.", 401
            task = SendModule()
            return task.execute(module)
