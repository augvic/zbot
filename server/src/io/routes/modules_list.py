from flask import Blueprint, request
from flask.views import MethodView
from src.tasks.get_modules_list import GetModulesList
from src.tasks.verify_if_have_access import VerifyIfHaveAccess
from src.tasks.create_module import CreateModule
from src.tasks.delete_module import DeleteModule
from typing import cast

modules_list = Blueprint("modules_list", __name__)

class ModulesList(MethodView):
    
    def get(self) -> dict[str, str | bool | list[dict[str, str]]] | tuple[str, int]:
        task1 = VerifyIfHaveAccess()
        task2 = GetModulesList()
        if not task1.execute("zAdmin"):
            return "Sem autorização.", 401
        return task2.execute()
    
    def post(self) -> tuple[str, int] | dict[str, str | bool]:
        task1 = VerifyIfHaveAccess()
        task2 = CreateModule()
        if not task1.execute("zAdmin"):
            return "Sem autorização.", 401
        data = cast(dict[str, str], request.json)
        return task2.execute(data)
    
    def delete(self, module: str) -> tuple[str, int] | dict[str, str | bool]:
        task1 = VerifyIfHaveAccess()
        task2 = DeleteModule()
        if not task1.execute("zAdmin"):
            return "Sem autorização.", 401
        return task2.execute(module)

modules_list.add_url_rule("/modules-list", view_func=ModulesList.as_view("modules_list_get_post"), methods=["GET", "POST"])
modules_list.add_url_rule("/modules-list/<module>", view_func=ModulesList.as_view("modules_list_delete"), methods=["DELETE"])
