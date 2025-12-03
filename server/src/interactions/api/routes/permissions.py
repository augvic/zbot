from src.tasks.get_permissions.get_permissions import GetPermissions
from src.tasks.create_permission.permission import CreatePermission
from src.tasks.delete_permission.delete_permission import DeletePermission
from src.tasks.verify_if_have_access.verify_if_have_access import VerifyIfHaveAccess
from tasks.verify_if_user_is_in_session_task import VerifyIfUserIsInSession
from tasks.register_route_task import RegisterRoute

class Permissions:
    
    def __init__(self,
        verify_if_have_access_task: VerifyIfHaveAccess,
        get_permissions_task: GetPermissions,
        create_permission_task: CreatePermission,
        delete_permission_task: DeletePermission,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession,
        register_route_task: RegisterRoute
    ) -> None:
        self.verify_if_have_access_task = verify_if_have_access_task
        self.get_permissions_task = get_permissions_task
        self.create_permission_task = create_permission_task
        self.delete_permission_task = delete_permission_task
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
        register_route_task.main("/permissions/<user>", ["GET"], self.get_user_permissions)
        register_route_task.main("/permissions/<user>/<permission>", ["POST"], self.create_user_permission)
        register_route_task.main("/permissions/<user>/<permission>", ["DELETE"], self.delete_user_permission)
    
    def get_user_permissions(self, user: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.verify_if_have_access_task.main("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.get_permissions_task.main(user)
            return {"success": True, "message": response.message, "data": response.data}, 200
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def create_user_permission(self, user: str, permission: str) -> tuple[dict[str, str | bool], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.verify_if_have_access_task.main("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.create_permission_task.main(user, permission)
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def delete_user_permission(self, user: str, permission: str) -> tuple[dict[str, str | bool], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response =  self.verify_if_have_access_task.main("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.delete_permission_task.main(user, permission)
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
