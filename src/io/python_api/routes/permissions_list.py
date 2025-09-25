from flask import Flask
from src.tasks import GetPermissionsList

class PermissionsList:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/permissions-list/<user>", methods=["GET"])
        def get_permissions_list(user: str) -> dict | str:
            task = GetPermissionsList()
            return task.execute(user)
