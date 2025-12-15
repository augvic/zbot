from src.tasks.tasks import Tasks
from src.engines.engines import Engines

from typing import cast

class ModulesRoute:
    
    def __init__(self, engines: Engines, tasks: Tasks) -> None:
        self.engines = engines
        self.tasks = tasks
        self.engines.wsgi_engine.register_route("/modules-list", ["GET"], self.get_modules_list)
        self.engines.wsgi_engine.register_route("/modules-list", ["POST"], self.create_module)
        self.engines.wsgi_engine.register_route("/modules-list/<module>", ["DELETE"], self.delete_module)
    
    def get_modules_list(self) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zAdmin"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.tasks.get_modules_task.main()
            return {"success": True, "data": response.data}, 200
        except Exception as error:
            self.engines.log_engine.write_error("api/modules_route", f"❌ Error in (ModulesRoute) in (get_modules_list) method: {error}")
            return {"success": False, "message": f"❌ Erro interno ao coletar módulos. Contate o administrador."}, 500
    
    def create_module(self) -> tuple[dict[str, str | bool], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zAdmin"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.engines.wsgi_engine.process_request(
                content_type= "application/json",
                expected_data=[
                    "module",
                    "description"
                ],
                expected_files=[]
            )
            if not response.success:
                return {"success": False, "message": response.message}, 400
            module = cast(str, response.data.get("module"))
            description = cast(str, response.data.get("description"))
            response = self.tasks.create_module_task.main(
                module,
                description
            )
            if response.success:
                self.engines.log_engine.write_text("api/modules_route", f"👤 Usuário ({self.engines.wsgi_engine.session_manager.get_session_user()}): ✅ Módulo ({module}) adicionado.")
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            self.engines.log_engine.write_error("api/modules_route", f"❌ Error in (ModulesRoute) in (create_module) method: {error}")
            return {"success": False, "message": f"❌ Erro interno ao criar módulo. Contate o administrador."}, 500
    
    def delete_module(self, module: str) -> tuple[dict[str, str | bool], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zAdmin"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.tasks.delete_module_task.main(module)
            if response.success:
                self.engines.log_engine.write_text("api/modules_route", f"👤 Usuário ({self.engines.wsgi_engine.session_manager.get_session_user()}): ✅ Módulo ({module}) removido.")
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": True, "message": response.message}, 400
        except Exception as error:
            self.engines.log_engine.write_error("api/modules_route", f"❌ Error in (ModulesRoute) in (delete_module) method: {error}")
            return {"success": False, "message": f"❌ Erro interno ao deletar módulo. Contate o administrador."}, 500
