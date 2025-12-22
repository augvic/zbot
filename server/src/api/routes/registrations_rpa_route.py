from src.threads.threads import Threads
from src.engines.engines import Engines

class RegistrationsRpaRoute:
    
    def __init__(self, engines: Engines, threads: Threads) -> None:
        self.engines = engines
        self.threads = threads
        self.engines.wsgi_engine.register_route("/registrations-rpa", ["GET"], self.refresh)
        self.engines.wsgi_engine.register_route("/registrations-rpa", ["POST"], self.turn_on)
        self.engines.wsgi_engine.register_route("/registrations-rpa", ["DELETE"], self.turn_off)
    
    def refresh(self) -> tuple[dict[str, bool | str], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zRegRpa"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            memory = self.threads.registrations_rpa_thread.memory_to_str()
            if self.threads.registrations_rpa_thread.is_running == True:
                return {"success": True, "status": "Em processamento...", "memory": memory}, 200
            else:
                return {"success": True, "status": "Desligado.", "memory": memory}, 200
        except Exception as error:
            self.engines.log_engine.write_error("api/registrations_rpa_route", f"❌ Error in (RegistrationsRpaRoute) in (refresh) method: {error}")
            return {"success": False, "message": f"❌ Erro interno ao verificar status do RPA. Contate o administrador."}, 500
    
    def turn_on(self) -> tuple[dict[str, str | bool], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zRegRpa"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.threads.registrations_rpa_thread.main()
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 401
        except Exception as error:
            self.engines.log_engine.write_error("api/registrations_rpa_route", f"❌ Error in (RegistrationsRpaRoute) in (turn_on) method: {error}")
            return {"success": False, "message": f"❌ Erro interno ao iniciar RPA. Contate o administrador."}, 500
    
    def turn_off(self) -> tuple[dict[str, bool | str], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zRegRpa"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.threads.registrations_rpa_thread.stop_rpa()
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 401
        except Exception as error:
            self.engines.log_engine.write_error("api/registrations_rpa_route", f"❌ Error in (RegistrationsRpaRoute) in (turn_off) method: {error}")
            return {"success": False, "message": f"❌ Erro interno ao desligar RPA. Contate o administrador."}, 500
