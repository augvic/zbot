from src.tasks.tasks import Tasks
from src.engines.engines import Engines

class SessionModulesRoute:
    
    def __init__(self, tasks: Tasks, engines: Engines) -> None:
        self.tasks = tasks
        self.engines = engines
        self.engines.wsgi_engine.register_route("/session-modules", ["GET"], self.get_session_modules)
    
    def get_session_modules(self) -> tuple[dict[str, str | bool | list[str]], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            session_modules = self.engines.wsgi_engine.session_manager.get_session_modules()
            return {"success": True, "message": session_modules}, 200
        except Exception as error:
            self.engines.log_engine.write_error("api/session_modules_route", f"❌ Error in (SessionModulesRoute) in (get_session_modules) method: {error}")
            return {"success": False, "message": f"❌ Erro interno ao coletar módulos da sessão. Contate o administrador."}, 500
