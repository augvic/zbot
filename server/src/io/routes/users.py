from flask import Flask, request
from src.tasks.get_users import GetUsers
from src.tasks.create_user import CreateUser
from src.tasks.delete_user import DeleteUser
from src.tasks.update_user import UpdateUser
from src.tasks.verify_if_have_access import VerifyIfHaveAccess
from typing import cast

class Users:
    
    def __init__(self, app: Flask) -> None:
        
        @app.route("/users/<user>", methods=["GET"])
        def get_user(user: str) -> tuple[str, int] | dict[str, str | bool | dict[str, str] | list[dict[str, str]]]:
            task1 = VerifyIfHaveAccess()
            task2 = GetUsers()
            if not task1.execute("zAdmin"):
                return "Sem autorização.", 401
            return task2.execute(user)
        
        @app.route("/users", methods=["POST"])
        def create_user() -> tuple[str, int] | dict[str, str | bool]:
            task1 = VerifyIfHaveAccess()
            task2 = CreateUser()
            if not task1.execute("zAdmin"):
                return "Sem autorização.", 401
            data = cast(dict[str, str], request.json)
            return task2.execute(data)
        
        @app.route("/users/<user>", methods=["DELETE"])
        def delete_user(user: str) -> tuple[str, int] | dict[str, str | bool]:
            task1 = VerifyIfHaveAccess()
            task2 = DeleteUser()
            if not task1.execute("zAdmin"):
                return "Sem autorização.", 401
            return task2.execute(user)
        
        @app.route("/users/<user>", methods=["PUT"])
        def update_user(user: str) -> tuple[str, int] | dict[str, str | bool]:
            task1 = VerifyIfHaveAccess()
            task2 = UpdateUser()
            if not task1.execute("zAdmin"):
                return "Sem autorização.", 401
            data = cast(dict[str, str], request.json)
            return task2.execute(user, data)
