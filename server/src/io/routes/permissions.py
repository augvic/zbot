from flask import Flask
from src.tasks.get_permissions import GetPermissions
from src.tasks.create_permission import CreatePermission
from src.tasks.delete_permission import DeletePermission
from src.tasks.verify_if_have_access import VerifyIfHaveAccess

class Permissions:
    
    def __init__(self, app: Flask) -> None:
        
        @app.route("/permissions/<user>", methods=["GET"])
        def get_user_permissions(user: str) -> dict[str, str | bool | list[dict[str, str]]] | tuple[str, int]:
            task1 = VerifyIfHaveAccess()
            task2 = GetPermissions()
            if not task1.execute("zAdmin"):
                return "Sem autorização.", 401
            return task2.execute(user)
        
        @app.route("/permissions/<user>/<permission>", methods=["POST"])
        def create_user_permission(user: str, permission: str) -> tuple[str, int] | dict[str, str | bool]:
            task1 = VerifyIfHaveAccess()
            task2 = CreatePermission()
            if not task1.execute("zAdmin"):
                return "Sem autorização.", 401
            return task2.execute(user, permission)
        
        @app.route("/permissions/<user>/<permission>", methods=["DELETE"])
        def delete_user_permission(user: str, permission: str) -> tuple[str, int] | dict[str, str | bool]:
            task1 = VerifyIfHaveAccess()
            task2 = DeletePermission()
            if not task1.execute("zAdmin"):
                return "Sem autorização.", 401
            return task2.execute(user, permission)
