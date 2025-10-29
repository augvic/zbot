from flask import Flask
from flask_socketio import SocketIO
from src.tasks.rpa.run_registrations_rpa.task import RunRegistrationsRpa
from src.tasks.verify_if_have_access import VerifyIfHaveAccess

class RegistrationsRpa:
    
    def __init__(self, app: Flask, socketio: SocketIO) -> None:
        self.socketio = socketio
        self.verify_if_have_acess_task = VerifyIfHaveAccess()
        self.run_registrations_rpa_task = RunRegistrationsRpa(self.socketio)
        
        @app.route("/registrations-rpa", methods=["GET"])
        def refresh() -> dict[str, str] | tuple[str, int]:
            if not self.verify_if_have_acess_task.execute("zRegRpa"):
                return "Sem autorização.", 401
            memory = self.run_registrations_rpa_task.memory_to_str()
            if self.run_registrations_rpa_task.is_running == True:
                return {"status": "Em processamento.", "memory": memory}
            else:
                return {"status": "Desligado.", "memory": memory}
        
        @app.route("/registrations-rpa", methods=["POST"])
        def turn_on() -> dict[str, str | bool] | tuple[str, int]:
            if not self.verify_if_have_acess_task.execute("zRegRpa"):
                return "Sem autorização.", 401
            if self.run_registrations_rpa_task.is_running == True:
                return {"success": False, "message": "RPA já está em processamento."}
            self.run_registrations_rpa_task.execute()
            return {"success": True, "message": "Sucesso ao ligar RPA."}
        
        @app.route("/registrations-rpa", methods=["DELETE"])
        def turn_off() -> dict[str, str | bool] | tuple[str, int]:
            if not self.verify_if_have_acess_task.execute("zRegRpa"):
                return "Sem autorização.", 401
            if self.run_registrations_rpa_task.is_running == False:
                return {"success": False,  "message": "RPA já está desligado."}
            self.socketio.emit("regrpa_status", {"status": "Desligando..."})
            self.run_registrations_rpa_task.stop = True
            return {"success": True,  "message": "Sucesso ao desligar RPA."}
