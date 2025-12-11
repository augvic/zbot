from src.rpas.rpas import Rpas
from src.engines.engines import Engines

class RegistrationsRpaRoute:
    
    def __init__(self, engines: Engines, rpas: Rpas) -> None:
        self.engines = engines
        self.rpas = rpas
        self.engines.wsgi_engine.register_route("/registrations-rpa", ["GET"], self.refresh)
        self.engines.wsgi_engine.register_route("/registrations-rpa", ["POST"], self.turn_on)
        self.engines.wsgi_engine.register_route("/registrations-rpa", ["DELETE"], self.turn_off)
    
    def refresh(self) -> tuple[dict[str, bool | str], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zRegRpa"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            memory = self.rpas.registrations_rpa.memory_to_str()
            if self.rpas.registrations_rpa.is_running == True:
                return {"success": True, "status": "Em processamento...", "memory": memory}, 200
            else:
                return {"success": True, "status": "Desligado.", "memory": memory}, 200
        except Exception as error:
            self.engines.log_engine.write_error("api/permissions_route", f"❌ Error in (PermissionsRoute) in (get_user_permissions) method: {error}")
            return {"success": False, "message": f"{error}"}, 500
    
    def turn_on(self) -> tuple[dict[str, str | bool], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zRegRpa"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.rpas.registrations_rpa.main()
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 409
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def turn_off(self) -> tuple[dict[str, bool | str], int]:
        try:
            if not self.engines.wsgi_engine.session_manager.is_user_in_session():
                return {"success": False, "message": "❌ Usuário não está na sessão."}, 401
            if not self.engines.wsgi_engine.session_manager.have_user_module_access("zRegRpa"):
                return {"success": False, "message": "❌ Sem autorização."}, 401
            response = self.rpas.registrations_rpa.stop_rpa()
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 409
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
