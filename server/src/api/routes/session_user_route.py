from src.tasks.tasks import Tasks
from src.engines.engines import Engines

from typing import Any

class SessionUserRoute:
    
    def __init__(self, tasks: Tasks, engines: Engines) -> None:
        self.tasks = tasks
        self.engines = engines
        self.engines.wsgi_engine.register_route("/session-user", ["GET"], self.get_session_user)
    
    def get_session_user(self) -> tuple[dict[str, str | bool | Any], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            user = self.engines.wsgi_engine.session_manager.get_session_user()
            return {"success": True, "message": user}, 200
        except Exception as error:
            self.engines.log_engine.write_error("api/session_user_route", f"❌ Error in (SessionUserRoute) in (get_session_user) method: {error}")
            return {"success": False, "message": f"❌ Erro interno ao coletar usuário da sessão. Contate o administrador."}, 500
