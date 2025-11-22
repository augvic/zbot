from src.tasks.auth.get_permissions.task import GetPermissions
from src.tasks.admin.permission.create_permission.task import CreatePermission
from src.tasks.admin.permission.delete_permission.task import DeletePermission
from src.tasks.auth.verify_if_have_access.task import VerifyIfHaveAccess
from src.tasks.auth.verify_if_user_is_in_session.task import VerifyIfUserIsInSession

class Permissions:
    
    def __init__(self,
        verify_if_have_access_task: VerifyIfHaveAccess,
        get_permissions_task: GetPermissions,
        create_permission_task: CreatePermission,
        delete_permission_task: DeletePermission,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession
    ) -> None:
        self.verify_if_have_access_task = verify_if_have_access_task
        self.get_permissions_task = get_permissions_task
        self.create_permission_task = create_permission_task
        self.delete_permission_task = delete_permission_task
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
    
    def get_user_permissions(self, user: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            response = self.verify_if_user_is_in_session_task.execute()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.verify_if_have_access_task.execute("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.get_permissions_task.execute(user)
            return {"success": True, "message": response.message, "data": response.data}, 200
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def create_user_permission(self, user: str, permission: str) -> tuple[dict[str, str | bool], int]:
        try:
            response = self.verify_if_user_is_in_session_task.execute()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.verify_if_have_access_task.execute("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.create_permission_task.execute(user, permission)
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def delete_user_permission(self, user: str, permission: str) -> tuple[dict[str, str | bool], int]:
        try:
            response = self.verify_if_user_is_in_session_task.execute()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response =  self.verify_if_have_access_task.execute("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.delete_permission_task.execute(user, permission)
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
