from flask import Flask, request
from src.server.tasks import GetPermissions, CreatePermissions, DeletePermission, UpdatePermissions

class Permissions:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/permissions/<user>", methods=["GET"])
        def get_permissions(user: str) -> dict | str:
            task = GetPermissions()
            return task.execute(user)
        
        @self.app.route("/permissions/<user>", methods=["POST"])
        def post_permissions(user: str) -> dict | str:
            data = request.json
            task = CreatePermissions()
            return task.execute(user, data)
        
        @self.app.route("/permissions/<user>/<module>", methods=["DELETE"])
        def delete_permissions(user: str, module: str) -> dict | str:
            task = DeletePermission()
            return task.execute(user, module)
