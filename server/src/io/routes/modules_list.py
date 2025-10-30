from flask import Flask, request
from src.tasks.get_data.get_modules_list.task import GetModulesList
from src.tasks.auth.verify_if_have_access.task import VerifyIfHaveAccess
from src.tasks.module_related.create_module.task import CreateModule
from src.tasks.module_related.delete_module.task import DeleteModule
from typing import cast

class ModulesList:
    
    def __init__(self, app: Flask) -> None:
        self.verify_if_have_access_task = VerifyIfHaveAccess()
        self.get_modules_list_task = GetModulesList()
        self.create_module_task = CreateModule()
        self.delete_module_task = DeleteModule()
        
        @app.route("/modules-list", methods=["GET"])
        def get_modules_list() -> dict[str, str | bool | list[dict[str, str]]] | tuple[str, int]:
            if not self.verify_if_have_access_task.execute("zAdmin"):
                return "Sem autorização.", 401
            return self.get_modules_list_task.execute()
        
        @app.route("/modules-list", methods=["POST"])
        def create_module() -> tuple[str, int] | dict[str, str | bool]:
            if not self.verify_if_have_access_task.execute("zAdmin"):
                return "Sem autorização.", 401
            data = cast(dict[str, str], request.json)
            return self.create_module_task.execute(data)
        
        @app.route("/modules-list/<module>", methods=["DELETE"])
        def delete_module(module: str) -> tuple[str, int] | dict[str, str | bool]:
            if not self.verify_if_have_access_task.execute("zAdmin"):
                return "Sem autorização.", 401
            return self.delete_module_task.execute(module)
