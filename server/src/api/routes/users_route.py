from src.tasks.tasks import Tasks
from src.engines.engines import Engines

from typing import cast

class UsersRoute:
    
    def __init__(self, tasks: Tasks, engines: Engines) -> None:
        self.tasks = tasks
        self.engines = engines
        self.engines.wsgi_engine.register_route("/users/<user>", ["GET"], self.get_user)
        self.engines.wsgi_engine.register_route("/users", ["POST"], self.create_user)
        self.engines.wsgi_engine.register_route("/users/<user>", ["DELETE"], self.delete_user)
        self.engines.wsgi_engine.register_route("/users", ["PUT"], self.update_user)
    
    def get_user(self, user: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zAdmin"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.tasks.get_user_task.main(user)
            if response.success:
                return {"success": True, "message": response.message, "data": response.data}, 200
            else:
                return {"success": False, "message": response.message, "data": response.data}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def create_user(self) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zAdmin"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.engines.wsgi_engine.process_request(
                content_type="application/json",
                expected_data=[
                    "user",
                    "name",
                    "email",
                    "password"
                ],
                expected_files=[]
            )
            if not response.success:
                return {"success": False, "message": response.message}, 400
            response = self.tasks.create_user_task.main(
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
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zAdmin"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.tasks.delete_user_task.main(user)
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def update_user(self) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zAdmin"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.engines.wsgi_engine.process_request(
                content_type="application/json",
                expected_data=[
                    "user",
                    "name",
                    "email",
                    "password"
                ],
                expected_files=[]
            )
            if not response.success:
                return {"success": False, "message": response.message}, 400
            response = self.tasks.update_user_task.main(
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
