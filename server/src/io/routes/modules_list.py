from flask import Blueprint
from flask.views import MethodView
from src.tasks.get_modules_list import GetModulesList
from src.tasks.verify_if_have_access import VerifyIfHaveAccess

modules_list = Blueprint("modules_list", __name__)

class ModulesList(MethodView):
    
    def get(self) -> dict[str, str | bool | list[dict[str, str]]] | tuple[str, int]:
        task1 = VerifyIfHaveAccess()
        task2 = GetModulesList()
        if not task1.execute("zAdmin"):
            return "Sem autorização.", 401
        return task2.execute()

modules_list.add_url_rule("/modules-list", view_func=ModulesList.as_view("modules_list"), methods=["GET"])
