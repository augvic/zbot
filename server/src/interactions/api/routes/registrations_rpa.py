from src.tasks.run_registrations_rpa.run_registrations_rpa import RunRegistrationsRpa
from src.tasks.verify_if_have_access.verify_if_have_access import VerifyIfHaveAccess
from tasks.verify_if_user_is_in_session_task import VerifyIfUserIsInSession
from tasks.register_route_task import RegisterRoute

class RegistrationsRpa:
    
    def __init__(self,
        verify_if_have_acess_task: VerifyIfHaveAccess,
        run_registrations_rpa_task: RunRegistrationsRpa,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession,
        register_route_task: RegisterRoute
    ) -> None:
        self.verify_if_have_acess_task = verify_if_have_acess_task
        self.run_registrations_rpa_task = run_registrations_rpa_task
        self.verify_if_user_is_in_session_task = verify_if_user_is_in_session_task
        register_route_task.main("/registrations-rpa", ["GET"], self.refresh)
        register_route_task.main("/registrations-rpa", ["POST"], self.turn_on)
        register_route_task.main("/registrations-rpa", ["DELETE"], self.turn_off)
    
    def refresh(self) -> tuple[dict[str, bool | str], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.verify_if_have_acess_task.main("zRegRpa")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            memory = self.run_registrations_rpa_task.memory_to_str()
            if self.run_registrations_rpa_task.is_running == True:
                return {"success": True, "status": "Em processamento...", "memory": memory}, 200
            else:
                return {"success": True, "status": "Desligado.", "memory": memory}, 200
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def turn_on(self) -> tuple[dict[str, str | bool], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.verify_if_have_acess_task.main("zRegRpa")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.run_registrations_rpa_task.main()
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 409
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
    
    def turn_off(self) -> tuple[dict[str, bool | str], int]:
        try:
            response = self.verify_if_user_is_in_session_task.main()
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.verify_if_have_acess_task.main("zRegRpa")
            if not response.success:
                return {"success": False, "message": response.message}, 401
            response = self.run_registrations_rpa_task.stop_rpa()
            if response.success:
                return {"success": True, "message": response.message}, 200
            else:
                return {"success": False, "message": response.message}, 409
        except Exception as error:
            return {"success": False, "message": f"{error}"}, 500
