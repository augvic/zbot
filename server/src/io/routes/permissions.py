from flask import Flask
from src.tasks.get_permissions import GetPermissions
from src.tasks.create_permission import CreatePermission
from src.tasks.delete_permission import DeletePermission
from src.tasks.verify_if_have_access import VerifyIfHaveAccess

class Permissions:
    
    def __init__(self, app: Flask) -> None:
        self.verify_if_have_access_task = VerifyIfHaveAccess()
        self.get_permissions_task = GetPermissions()
        self.create_permission_task = CreatePermission()
        self.delete_permission_task = DeletePermission()
        
        @app.route("/permissions/<user>", methods=["GET"])
        def get_user_permissions(user: str) -> dict[str, str | bool | list[dict[str, str]]] | tuple[str, int]:
            if not self.verify_if_have_access_task.execute("zAdmin"):
                return "Sem autorização.", 401
            return self.get_permissions_task.execute(user)
        
        @app.route("/permissions/<user>/<permission>", methods=["POST"])
        def create_user_permission(user: str, permission: str) -> tuple[str, int] | dict[str, str | bool]:
            if not self.verify_if_have_access_task.execute("zAdmin"):
                return "Sem autorização.", 401
            return self.create_permission_task.execute(user, permission)
        
        @app.route("/permissions/<user>/<permission>", methods=["DELETE"])
        def delete_user_permission(user: str, permission: str) -> tuple[str, int] | dict[str, str | bool]:
            if not self.verify_if_have_access_task.execute("zAdmin"):
                return "Sem autorização.", 401
            return self.delete_permission_task.execute(user, permission)
