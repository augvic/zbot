from flask import Blueprint
from flask.views import MethodView
from src.tasks.get_permissions import GetPermissions
from src.tasks.create_permission import CreatePermission
from src.tasks.delete_permission import DeletePermission
from src.tasks.verify_if_have_access import VerifyIfHaveAccess

permissions = Blueprint("permissions", __name__)

class Permissions(MethodView):
    
    def get(self, user: str) -> dict[str, str | bool | list[dict[str, str]]] | tuple[str, int]:
        task1 = VerifyIfHaveAccess()
        task2 = GetPermissions()
        if not task1.execute("zAdmin"):
            return "Sem autorização.", 401
        return task2.execute(user)
    
    def post(self, user: str, permission: str) -> tuple[str, int] | dict[str, str | bool]:
        task1 = VerifyIfHaveAccess()
        task2 = CreatePermission()
        if not task1.execute("zAdmin"):
            return "Sem autorização.", 401
        return task2.execute(user, permission)
    
    def delete(self, user: str, permission: str) -> tuple[str, str | int] | dict[str, str | bool]:
        task1 = VerifyIfHaveAccess()
        task2 = DeletePermission()
        if not task1.execute("zAdmin"):
            return "Sem autorização.", 401
        return task2.execute(user, permission)

permissions.add_url_rule("/permissions/<user>", view_func=Permissions.as_view("permissions_get"), methods=["GET"])
permissions.add_url_rule("/permissions/<user>/<permission>", view_func=Permissions.as_view("permissions_post_delete"), methods=["POST", "DELETE"])
