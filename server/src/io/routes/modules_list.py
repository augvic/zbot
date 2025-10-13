from flask import Flask, request
from src.tasks.get_modules_list import GetModulesList
from src.tasks.verify_if_have_access import VerifyIfHaveAccess
from src.tasks.create_module import CreateModule
from src.tasks.delete_module import DeleteModule
from typing import cast

class ModulesList:
    
    def __init__(self, app: Flask) -> None:
        
        @app.route("/modules-list", methods=["GET"])
        def get_modules_list() -> dict[str, str | bool | list[dict[str, str]]] | tuple[str, int]:
            task1 = VerifyIfHaveAccess()
            task2 = GetModulesList()
            if not task1.execute("zAdmin"):
                return "Sem autorização.", 401
            return task2.execute()
        
        @app.route("/modules-list", methods=["POST"])
        def create_module() -> tuple[str, int] | dict[str, str | bool]:
            task1 = VerifyIfHaveAccess()
            task2 = CreateModule()
            if not task1.execute("zAdmin"):
                return "Sem autorização.", 401
            data = cast(dict[str, str], request.json)
            return task2.execute(data)
        
        @app.route("/modules-list/<module>", methods=["DELETE"])
        def delete_module(module: str) -> tuple[str, int] | dict[str, str | bool]:
            task1 = VerifyIfHaveAccess()
            task2 = DeleteModule()
            if not task1.execute("zAdmin"):
                return "Sem autorização.", 401
            return task2.execute(module)
