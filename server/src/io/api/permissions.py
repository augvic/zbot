from src.tasks.auth.get_permissions.task import GetPermissions
from src.tasks.admin.permission.create_permission.task import CreatePermission
from src.tasks.admin.permission.delete_permission.task import DeletePermission
from src.tasks.auth.verify_if_have_access.task import VerifyIfHaveAccess
from src.components.infra.wsgi_application import WsgiApplication

class Permissions:
    
    def __init__(self,
        verify_if_have_access_task: VerifyIfHaveAccess,
        get_permissions_task: GetPermissions,
        create_permission_task: CreatePermission,
        delete_permission_task: DeletePermission
    ) -> None:
        self.verify_if_have_access_task = verify_if_have_access_task
        self.get_permissions_task = get_permissions_task
        self.create_permission_task = create_permission_task
        self.delete_permission_task = delete_permission_task
    
    def register(self, app: WsgiApplication) -> None:
        try:
            @app.route("/permissions/<user>", methods=["GET"])
            def get_user_permissions(user: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
                try:
                    response = self.verify_if_have_access_task.execute("zAdmin")
                    if not response.success:
                        return {"success": False, "message": response.message}, 401
                    response = self.get_permissions_task.execute(user)
                    return {"success": True, "message": response.message, "data": response.data}, 200
                except Exception as error:
                    return {"success": False, "message": f"{error}"}, 500
            
            @app.route("/permissions/<user>/<permission>", methods=["POST"])
            def create_user_permission(user: str, permission: str) -> tuple[dict[str, str | bool], int]:
                try:
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
            
            @app.route("/permissions/<user>/<permission>", methods=["DELETE"])
            def delete_user_permission(user: str, permission: str) -> tuple[dict[str, str | bool], int]:
                try:
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
        except Exception as error:
            print(f"❌ Error in (Permissions) route: {error}.")
