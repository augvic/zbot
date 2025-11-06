from src.tasks.get_data.get_modules_list.task import GetModulesList
from src.tasks.auth.verify_if_have_access.task import VerifyIfHaveAccess
from src.tasks.admin.module.create_module.task import CreateModule
from src.tasks.admin.module.delete_module.task import DeleteModule
from src.tasks.application.process_request.task import ProcessRequest
from src.tasks.application.route_registry import RouteRegistryTask
from typing import cast

class ModulesList:
    
    def __init__(self,
        verify_if_have_access_task: VerifyIfHaveAccess,
        get_modules_list_task: GetModulesList,
        create_module_task: CreateModule,
        delete_module_task: DeleteModule,
        process_request_task: ProcessRequest,
        route_registry_task: RouteRegistryTask
    ) -> None:
        self.verify_if_have_access_task = verify_if_have_access_task
        self.get_modules_list_task = get_modules_list_task
        self.create_module_task = create_module_task
        self.delete_module_task = delete_module_task
        self.process_request_task = process_request_task
        self.route_registry_task = route_registry_task
    
    def init(self) -> None:
        try:
            def get_modules_list() -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
                try:
                    response = self.verify_if_have_access_task.execute("zAdmin")
                    if not response.success:
                        return {"success": False, "message": response.message}, 401
                    response = self.get_modules_list_task.execute()
                    return {"success": True, "data": response.data}, 200
                except Exception as error:
                    return {"success": False, "data": f"{error}"}, 500
            
            def create_module() -> tuple[dict[str, str | bool], int]:
                try:
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
                        return {"success": False, "message": response.message}, 400
                    response = self.create_module_task.execute(
                        cast(str, response.data.get("module")),
                        cast(str, response.data.get("description"))
                    )
                    if response.success:
                        return {"success": True, "message": response.message}, 200
                    else:
                        return {"success": False, "message": response.message}, 400
                except Exception as error:
                    return {"success": False, "data": f"{error}"}, 500
            
            def delete_module(module: str) -> tuple[dict[str, str | bool], int]:
                try:
                    response = self.verify_if_have_access_task.execute("zAdmin")
                    if not response.success:
                        return {"success": False, "message": response.message}, 401
                    response = self.delete_module_task.execute(module)
                    if response.success:
                        return {"success": True, "message": response.message}, 200
                    else:
                        return {"success": True, "message": response.message}, 400
                except Exception as error:
                    return {"success": False, "data": f"{error}"}, 500
            
            self.route_registry_task.execute("/modules-list", ["GET"], get_modules_list)
            self.route_registry_task.execute("/modules-list", ["POST"], create_module)
            self.route_registry_task.execute("/modules-list/<module>", ["DELETE"], delete_module)
        except Exception as error:
            print(f"❌ Error in (ModulesList) route: {error}.")
