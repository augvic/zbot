from src.tasks.get_modules_list.get_modules_list import GetModulesList
from src.tasks.verify_if_have_access.verify_if_have_access import VerifyIfHaveAccess
from src.tasks.create_module.create_module import CreateModule
from src.tasks.delete_module.delete_module import DeleteModule
from src.tasks.process_request.process_request import ProcessRequest
from tasks.verify_if_user_is_in_session_task import VerifyIfUserIsInSession
from tasks.register_route_task import RegisterRoute

from typing import cast

class ModulesList:
    
    def __init__(self,
        verify_if_have_access_task: VerifyIfHaveAccess,
        get_modules_list_task: GetModulesList,
        create_module_task: CreateModule,
        delete_module_task: DeleteModule,
        process_request_task: ProcessRequest,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession,
        register_route_task: RegisterRoute
    ) -> None:
        self.verify_if_have_access_task = verify_if_have_access_task
        self.get_modules_list_task = get_modules_list_task
        self.create_module_task = create_module_task
        self.delete_module_task = delete_module_task
        self.process_request_task = process_request_task
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
        register_route_task.main("/modules-list", ["GET"], self.get_modules_list)
        register_route_task.main("/modules-list", ["POST"], self.create_module)
        register_route_task.main("/modules-list/<module>", ["DELETE"], self.delete_module)
    
    def get_modules_list(self) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.verify_if_have_access_task.main("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.get_modules_list_task.main()
            return {"success": True, "data": response.data}, 200
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def create_module(self) -> tuple[dict[str, str | bool], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.verify_if_have_access_task.main("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.process_request_task.main(
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
            response = self.create_module_task.main(
                cast(str, response.data.get("module")),
                cast(str, response.data.get("description"))
            )
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def delete_module(self, module: str) -> tuple[dict[str, str | bool], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.verify_if_have_access_task.main("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.delete_module_task.main(module)
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": True, "message": response.message}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
