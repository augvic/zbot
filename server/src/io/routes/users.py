from flask import Blueprint, request
from flask.views import MethodView
from src.tasks.get_users import GetUsers
from src.tasks.create_user import CreateUser
from src.tasks.delete_user import DeleteUser
from src.tasks.update_user import UpdateUser
from src.tasks.verify_if_have_access import VerifyIfHaveAccess
from typing import cast

users = Blueprint("users", __name__)

class Users(MethodView):
    
    def get(self, user: str) -> tuple[str, int] | dict[str, str | bool | dict[str, str] | list[dict[str, str]]]:
        task1 = VerifyIfHaveAccess()
        task2 = GetUsers()
        if not task1.execute("zAdmin"):
            return "Sem autorização.", 401
        return task2.execute(user)
    
    def post(self) -> tuple[str, int] | dict[str, str | bool]:
        task1 = VerifyIfHaveAccess()
        task2 = CreateUser()
        if not task1.execute("zAdmin"):
            return "Sem autorização.", 401
        data = cast(dict[str, str], request.json)
        return task2.execute(data)
    
    def delete(self, user: str) -> tuple[str, int] | dict[str, str | bool]:
        task1 = VerifyIfHaveAccess()
        task2 = DeleteUser()
        if not task1.execute("zAdmin"):
            return "Sem autorização.", 401
        return task2.execute(user)
    
    def put(self, user: str) -> tuple[str, int] | dict[str, str | bool]:
        task1 = VerifyIfHaveAccess()
        task2 = UpdateUser()
        if not task1.execute("zAdmin"):
            return "Sem autorização.", 401
        data = cast(dict[str, str], request.json)
        return task2.execute(user, data)

users.add_url_rule("/users/<user>", view_func=Users.as_view("users_get_delete_put"), methods=["GET", "DELETE", "PUT"])
users.add_url_rule("/users", view_func=Users.as_view("users_post"), methods=["POST"])
