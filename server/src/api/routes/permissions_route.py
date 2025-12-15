from src.tasks.tasks import Tasks
from src.engines.engines import Engines

class PermissionsRoute:
    
    def __init__(self, engines: Engines, tasks: Tasks) -> None:
        self.engines = engines
        self.tasks = tasks
        self.engines.wsgi_engine.register_route("/permissions/<user>", ["GET"], self.get_user_permissions)
        self.engines.wsgi_engine.register_route("/permissions/<user>/<permission>", ["POST"], self.create_user_permission)
        self.engines.wsgi_engine.register_route("/permissions/<user>/<permission>", ["DELETE"], self.delete_user_permission)
    
    def get_user_permissions(self, user: str) -> tuple[dict[str, str | bool | list[dict[str, str]]], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zAdmin"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.tasks.get_permissions_task.main(user)
            return {"success": True, "message": response.message, "data": response.data}, 200
        except Exception as error:
            self.engines.log_engine.write_error("api/permissions_route", f"❌ Error in (PermissionsRoute) in (get_user_permissions) method: {error}")
            return {"success": False, "message": f"❌ Erro interno ao coletar permissões. Contate o administrador."}, 500
    
    def create_user_permission(self, user: str, permission: str) -> tuple[dict[str, str | bool], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zAdmin"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.tasks.create_permission_task.main(user, permission)
            if response.success:
                self.engines.log_engine.write_text("api/permissions_route", f"👤 Usuário ({self.engines.wsgi_engine.session_manager.get_session_user()}): ✅ Permissão ({permission}) adicionada.")
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            self.engines.log_engine.write_error("api/permissions_route", f"❌ Error in (PermissionsRoute) in (create_user_permission) method: {error}")
            return {"success": False, "message": f"❌ Erro interno ao criar permissão. Contate o administrador."}, 500
    
    def delete_user_permission(self, user: str, permission: str) -> tuple[dict[str, str | bool], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zAdmin"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.tasks.delete_permission_task.main(user, permission)
            if response.success:
                self.engines.log_engine.write_text("api/permissions_route", f"👤 Usuário ({self.engines.wsgi_engine.session_manager.get_session_user()}): ✅ Permissão ({permission}) removida.")
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 400
        except Exception as error:
            self.engines.log_engine.write_error("api/permissions_route", f"❌ Error in (PermissionsRoute) in (delete_user_permission) method: {error}")
            return {"success": False, "message": f"❌ Erro interno ao deletar permissão. Contate o administrador."}, 500
