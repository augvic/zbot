from src.tasks.get_user.get_user import GetUser
from src.tasks.create_user.create_user import CreateUser
from src.tasks.delete_user.delete_user import DeleteUser
from src.tasks.update_user.update_user import UpdateUser
from src.tasks.process_request.process_request import ProcessRequest
from src.tasks.verify_if_have_access.verify_if_have_access import VerifyIfHaveAccess
from src.tasks.verify_if_user_is_in_session.verify_if_user_is_in_session import VerifyIfUserIsInSession
from src.tasks.register_route import RegisterRoute

from typing import cast

class Users:
    
    def __init__(self,
        verify_if_have_access_task: VerifyIfHaveAccess,
        get_user_task: GetUser,
        create_user_task: CreateUser,
        delete_user_task: DeleteUser,
        update_user_task: UpdateUser,
        process_request_task: ProcessRequest,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession,
        register_route_task: RegisterRoute
    ) -> None:
        self.verify_if_have_access_task = verify_if_have_access_task
        self.get_user_task = get_user_task
        self.create_user_task = create_user_task
        self.delete_user_task = delete_user_task
        self.update_user_task = update_user_task
        self.process_request_task = process_request_task
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
        register_route_task.main("/users/<user>", ["GET"], self.get_user)
        register_route_task.main("/users", ["POST"], self.create_user)
        register_route_task.main("/users/<user>", ["DELETE"], self.delete_user)
        register_route_task.main("/users", ["PUT"], self.update_user)
    
    def get_user(self, user: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response =  self.verify_if_have_access_task.main("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.get_user_task.main(user)
            if response.success:
                return {"success": True, "message": response.message, "data": response.data}, 200
            else:
                return {"success": False, "message": response.message, "data": response.data}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def create_user(self) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response =  self.verify_if_have_access_task.main("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.process_request_task.main(
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
            response = self.create_user_task.main(
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
    
    def delete_user(self, user: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response =  self.verify_if_have_access_task.main("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.delete_user_task.main(user)
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def update_user(self) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response =  self.verify_if_have_access_task.main("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.process_request_task.main(
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
            response = self.update_user_task.main(
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
