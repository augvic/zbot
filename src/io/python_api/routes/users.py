from flask import Flask, request
from src.tasks import GetUsers, CreateUser, DeleteUser, UpdateUser

class Users:
    
    def __init__(self, app: Flask):
        self.app = app
        self.routes()
    
    def routes(self) -> None:
        @self.app.route("/users/<user>", methods=["GET"])
        def get_users(user: str) -> dict | str:
            task = GetUsers()
            return task.execute(user)
        
        @self.app.route("/users", methods=["POST"])
        def post_users() -> dict | str:
            data = request.json
            task = CreateUser()
            return task.execute(data)
        
        @self.app.route("/users/<user>", methods=["DELETE"])
        def delete_users(user: str) -> dict | str:
            task = DeleteUser()
            return task.execute(user)
        
        @self.app.route("/users/<user>", methods=["PUT"])
        def update_users(user: str) -> dict | str:
            data = request.json
            task = UpdateUser()
            return task.execute(user, data)
