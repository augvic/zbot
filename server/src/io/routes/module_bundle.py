from flask import Blueprint, Response
from flask.views import MethodView
from src.tasks.send_module import SendModule
from src.tasks.verify_if_have_access import VerifyIfHaveAccess

module_bundle = Blueprint("module_bundle", __name__)

class ModuleBundle(MethodView):
    
    def get(self, module: str) -> Response | str | tuple[str, int]:
        task1 = VerifyIfHaveAccess()
        task2 = SendModule()
        moduleUpperCase = (module[0] + module[1].upper() + module[2:]).replace(".js", "")
        if not task1.execute(moduleUpperCase):
            return "Sem autorização.", 401
        return task2.execute(module)

module_bundle.add_url_rule("/module-bundle/<module>", view_func=ModuleBundle.as_view("module_bundle"), methods=["GET"])
