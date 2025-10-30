from flask import Flask, request
from src.tasks.admin.user.get_user.task import GetUsers
from src.tasks.admin.user.create_user.task import CreateUser
from src.tasks.admin.user.delete_user.task import DeleteUser
from src.tasks.admin.user.update_user.task import UpdateUser
from src.tasks.auth.verify_if_have_access.task import VerifyIfHaveAccess
from typing import cast

class Users:
    
    def __init__(self, app: Flask) -> None:
        self.verify_if_have_access_task = VerifyIfHaveAccess()
        self.get_users_task = GetUsers()
        self.create_user_task = CreateUser()
        self.delete_user_task = DeleteUser()
        self.update_user_task = UpdateUser()

        @app.route("/users/<user>", methods=["GET"])
        def get_user(user: str) -> tuple[str, int] | dict[str, str | bool | dict[str, str] | list[dict[str, str]]]:
            if not self.verify_if_have_access_task.execute("zAdmin"):
                return "Sem autorização.", 401
            return self.get_users_task.execute(user)
        
        @app.route("/users", methods=["POST"])
        def create_user() -> tuple[str, int] | dict[str, str | bool]:
            if not self.verify_if_have_access_task.execute("zAdmin"):
                return "Sem autorização.", 401
            data = cast(dict[str, str], request.json)
            return self.create_user_task.execute(data)
        
        @app.route("/users/<user>", methods=["DELETE"])
        def delete_user(user: str) -> tuple[str, int] | dict[str, str | bool]:
            if not self.verify_if_have_access_task.execute("zAdmin"):
                return "Sem autorização.", 401
            return self.delete_user_task.execute(user)
        
        @app.route("/users/<user>", methods=["PUT"])
        def update_user(user: str) -> tuple[str, int] | dict[str, str | bool]:
            if not self.verify_if_have_access_task.execute("zAdmin"):
                return "Sem autorização.", 401
            data = cast(dict[str, str], request.json)
            return self.update_user_task.execute(user, data)
