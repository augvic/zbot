from flask import Flask
from src.tasks import GetPermissions, CreatePermission, DeletePermission

class Permissions:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/permissions/<user>", methods=["GET"])
        def get_permissions(user: str) -> dict | str:
            if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access("zAdmin"):
                return "Sem autorização.", 401
            task = GetPermissions()
            return task.execute(user)
        
        @self.app.route("/permissions/<user>/<permission>", methods=["POST"])
        def post_permissions(user: str, permission: str) -> dict | str:
            if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access("zAdmin"):
                return "Sem autorização.", 401
            task = CreatePermission()
            return task.execute(user, permission)
        
        @self.app.route("/permissions/<user>/<permission>", methods=["DELETE"])
        def delete_permissions(user: str, permission: str) -> dict | str:
            if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access("zAdmin"):
                return "Sem autorização.", 401
            task = DeletePermission()
            return task.execute(user, permission)
