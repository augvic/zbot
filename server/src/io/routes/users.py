from src.tasks.admin.user.get_user.task import GetUser
from src.tasks.admin.user.create_user.task import CreateUser
from src.tasks.admin.user.delete_user.task import DeleteUser
from src.tasks.admin.user.update_user.task import UpdateUser
from src.tasks.application.process_request.task import ProcessRequest
from src.tasks.auth.verify_if_have_access.task import VerifyIfHaveAccess
from src.tasks.auth.verify_if_user_is_in_session.task import VerifyIfUserIsInSession
from typing import cast

class Users:
    
    def __init__(self,
        verify_if_have_access_task: VerifyIfHaveAccess,
        get_users_task: GetUser,
        create_user_task: CreateUser,
        delete_user_task: DeleteUser,
        update_user_task: UpdateUser,
        process_request_task: ProcessRequest,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession
    ) -> None:
        self.verify_if_have_access_task = verify_if_have_access_task
        self.get_users_task = get_users_task
        self.create_user_task = create_user_task
        self.delete_user_task = delete_user_task
        self.update_user_task = update_user_task
        self.process_request_task = process_request_task
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
    
    def get_user(self, user: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response =  self.verify_if_have_access_task.main("zAdmin")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.get_users_task.main(user)
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
