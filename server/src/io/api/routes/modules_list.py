from src.tasks.get_data.get_modules_list.task import GetModulesList
from src.tasks.auth.verify_if_have_access.task import VerifyIfHaveAccess
from src.tasks.admin.module.create_module.task import CreateModule
from src.tasks.admin.module.delete_module.task import DeleteModule
from src.tasks.application.process_request.task import ProcessRequest
from src.components.infra.wsgi_application import WsgiApplication
from typing import cast

class ModulesList:
    
    def __init__(self, app: WsgiApplication) -> None:
        self.verify_if_have_access_task = VerifyIfHaveAccess()
        self.get_modules_list_task = GetModulesList()
        self.create_module_task = CreateModule()
        self.delete_module_task = DeleteModule()
        self.process_request_task = ProcessRequest()
        
        @app.route("/modules-list", methods=["GET"])
        def get_modules_list() -> tuple[dict[str, str | bool], int] | dict[str, list[dict[str, str]] | bool]:
            response = self.verify_if_have_access_task.execute("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.get_modules_list_task.execute()
            return {"success": True, "data": response.data}
        
        @app.route("/modules-list", methods=["POST"])
        def create_module() -> tuple[dict[str, str | bool], int] | dict[str, str | bool]:
            response = self.verify_if_have_access_task.execute("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.process_request_task.execute(
                content_type= "application/json",
                expected_data=[
                    "module",
                    "description"
                ],
                expected_files=[],
                optional_data=[],
                optional_files=[]
            )
            if not response.success:
                return {"success": False, "message": response.message}, 415
            response = self.create_module_task.execute(
                cast(str, response.data.get("module")),
                cast(str, response.data.get("description"))
            )
            return {"success": response.success, "message": response.message}
        
        @app.route("/modules-list/<module>", methods=["DELETE"])
        def delete_module(module: str) -> tuple[dict[str, str | bool], int] | dict[str, str | bool]:
            response = self.verify_if_have_access_task.execute("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.delete_module_task.execute(module)
            return {"success": False, "message": response.message}
