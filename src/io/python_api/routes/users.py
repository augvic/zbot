from flask import Flask, Response
from src.tasks import GetAllUsers

class Users:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/users/<user>", methods=["GET"])
        def get_users(user: str) -> Response:
            task = GetAllUsers()
            return task.execute(user)
