from src.tasks.admin.user.get_user.task import GetUser
from src.tasks.admin.user.create_user.task import CreateUser
from src.tasks.admin.user.delete_user.task import DeleteUser
from src.tasks.admin.user.update_user.task import UpdateUser
from src.tasks.auth.verify_if_have_access.task import VerifyIfHaveAccess
from src.components.logic.request_processor.component import RequestProcessor
from src.components.infra.wsgi_application import WsgiApplication
from typing import cast

class Users:
    
    def __init__(self) -> None:
        self.verify_if_have_access_task = VerifyIfHaveAccess()
        self.get_users_task = GetUser()
        self.create_user_task = CreateUser()
        self.delete_user_task = DeleteUser()
        self.update_user_task = UpdateUser()
        self.request_processor = RequestProcessor()
    
    def register(self, app: WsgiApplication) -> None:
        try:
            @app.route("/users/<user>", methods=["GET"])
            def get_user(user: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
                try:
                    response =  self.verify_if_have_access_task.execute("zAdmin")
                    if not response.success:
                        return {"success": False, "message": "Sem autorização."}, 401
                    response = self.get_users_task.execute(user)
                    if response.success:
                        return {"success": True, "message": response.message, "data": response.data}, 200
                    else:
                        return {"success": False, "message": response.message, "data": response.data}, 400
                except Exception as error:
                    return {"success": False, "message": f"{error}"}, 500
            
            @app.route("/users", methods=["POST"])
            def create_user() -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
                try:
                    response =  self.verify_if_have_access_task.execute("zAdmin")
                    if not response.success:
                        return {"success": False, "message": "Sem autorização."}, 401
                    response = self.request_processor.process(
                        content_type="application/json",
                        expected_data=[
                            "user",
                            "name",
                            "email",
                            "password"
                        ],
                        expected_files=[],
                        optional_data=[],
                        optional_files=[]
                    )
                    if not response.success:
                        return {"success": False, "message": response.message}, 400
                    response = self.create_user_task.execute(
                        user=cast(str, response.data.get("user")),
                        name=cast(str, response.data.get("name")),
                        email=cast(str, response.data.get("email")),
                        password=cast(str, response.data.get("password")),
                    )
                    if response.success:
                        return {"success": True, "message": response.message}, 200
                    else:
                        return {"success": False, "message": response.message}, 400
                except Exception as error:
                    return {"success": False, "message": f"{error}"}, 500
            
            @app.route("/users/<user>", methods=["DELETE"])
            def delete_user(user: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
                try:
                    response =  self.verify_if_have_access_task.execute("zAdmin")
                    if not response.success:
                        return {"success": False, "message": "Sem autorização."}, 401
                    response = self.delete_user_task.execute(user)
                    if response.success:
                        return {"success": True, "message": response.message}, 200
                    else:
                        return {"success": False, "message": response.message}, 400
                except Exception as error:
                    return {"success": False, "message": f"{error}"}, 500
            
            @app.route("/users/<user>", methods=["PUT"])
            def update_user(user: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
                try:
                    response =  self.verify_if_have_access_task.execute("zAdmin")
                    if not response.success:
                        return {"success": False, "message": "Sem autorização."}, 401
                    response = self.request_processor.process(
                        content_type="application/json",
                        expected_data=[
                            "user",
                            "name",
                            "email",
                            "password"
                        ],
                        expected_files=[],
                        optional_data=[],
                        optional_files=[]
                    )
                    if not response.success:
                        return {"success": False, "message": response.message}, 400
                    response = self.update_user_task.execute(
                        user=cast(str, response.data.get("user")),
                        name=cast(str, response.data.get("name")),
                        email=cast(str, response.data.get("email")),
                        password=cast(str, response.data.get("password")),
                    )
                    if response.success:
                        return {"success": True, "message": response.message}, 200
                    else:
                        return {"success": False, "message": response.message}, 400
                except Exception as error:
                    return {"success": False, "message": f"{error}"}, 500
        except Exception as error:
            print(f"❌ Error in (Users) route: {error}.")
