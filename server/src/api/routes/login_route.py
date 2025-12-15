from src.tasks.tasks import Tasks
from src.engines.engines import Engines

from typing import cast

class LoginRoute:
    
    def __init__(self, tasks: Tasks, engines: Engines) -> None:
        self.tasks = tasks
        self.engines = engines
        self.engines.wsgi_engine.register_route("/login", ["POST"], self.validate_login)
        self.engines.wsgi_engine.register_route("/login", ["GET"], self.is_user_in_session)
        self.engines.wsgi_engine.register_route("/login", ["DELETE"], self.logout)
    
    def validate_login(self) -> tuple[dict[str, str | bool], int]:
        try:
            response = self.engines.wsgi_engine.process_request(
                content_type="application/json",
                expected_data=[
                    "user",
                    "password"
                ],
                expected_files=[]
            )
            if not response.success:
                return {"success": False, "message": response.message}, 400
            if self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário já está logado."}, 401                
            user = cast(str, response.data.get("user"))
            password = cast(str, response.data.get("password"))
            user_orm = self.engines.database_engine.users_client.read(user)
            if user_orm == None:
                return {"success": False, "message": "❌ Usuário não encontrado."}, 401
            if user_orm.password != password:
                return {"success": False, "message": "❌ Login inválido."}, 401
            modules = self.engines.database_engine.modules_client.read_all()
            modules_descriptions = {}
            for module in modules:
                modules_descriptions[module.module] = module.description
            user_permissions = self.engines.database_engine.permissions_client.read_all_from_user(user)
            permissions_list: list[dict[str, str]] = []
            for user_permission in user_permissions:
                permissions_list.append({"module": user_permission.module, "description": modules_descriptions[user_permission.module]})
            self.engines.wsgi_engine.session_manager.save_in_session("user", user)
            self.engines.wsgi_engine.session_manager.save_in_session("session_modules", permissions_list)
            self.engines.log_engine.write_text("api/login_route", f"👤 Usuário ({self.engines.wsgi_engine.session_manager.get_session_user()}): ✅ Login realizado com sucesso.")
            return {"success": True, "message": f"✅ Login realizado com sucesso."}, 200
        except Exception as error:
            self.engines.log_engine.write_error("api/login_route", f"❌ Error in (LoginRoute) in (validate_login) method: {error}")
            return {"success": False, "message": "❌ Erro interno ao processar login. Contate o administrador."}, 500
    
    def is_user_in_session(self) -> tuple[dict[str, str | bool], int]:
        try:
            if self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": True, "message": "✅ Está na sessão."}, 200
            else:
                return {"success": False, "message": "❌ Não está na sessão."}, 401
        except Exception as error:
            self.engines.log_engine.write_error("api/login_route", f"❌ Error in (LoginRoute) in (is_user_in_session) method: {error}")
            return {"success": False, "message": "❌ Erro interno ao verificar se usuário está na sessão. Contate o administrador."}, 500
    
    def logout(self) -> tuple[dict[str, str | bool], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está logado."}, 401
            user = self.engines.wsgi_engine.session_manager.get_session_user()
            self.engines.wsgi_engine.session_manager.clear_session()
            self.engines.log_engine.write_text("api/login_route", f"👤 Usuário ({user}): ✅ Logout realizado.")
            return {"success": True, "message": "✅ Logout realizado."}, 200
        except Exception as error:
            self.engines.log_engine.write_error("api/login_route", f"❌ Error in (LoginRoute) in (logout) method: {error}")
            return {"success": False, "message": f"❌ Erro interno ao deslogar. Contate o administrador."}, 500
