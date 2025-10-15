from flask import Flask
from flask_socketio import SocketIO
from src.tasks.run_registrations_rpa import RunRegistrationsRpa
from src.tasks.verify_if_have_access import VerifyIfHaveAccess

class RegistrationsRpa:
    
    def __init__(self, app: Flask, socketio: SocketIO) -> None:
        self.socketio = socketio
        self.verify_if_have_acess_task = VerifyIfHaveAccess()
        
        @app.route("/registrations-rpa", methods=["GET"])
        def refresh() -> dict[str, str] | tuple[str, int]:
            if not task.execute("zRegRpa"):
                return "Sem autorização.", 401
            memory_string = ""
            for message in self.memory:
                memory_string += message + "\n"
            if self.is_running == True:
                return {"status": "Em processamento.", "memory": memory_string}
            else:
                return {"status": "Desligado.", "memory": memory_string}
        
        @app.route("/registrations-rpa", methods=["POST"])
        def turn_on() -> dict[str, str | bool] | tuple[str, int]:
            task1 = VerifyIfHaveAccess()
            if not task1.execute("zRegRpa"):
                return "Sem autorização.", 401
            if self.is_running == True:
                return {"success": False, "message": "RPA já está em processamento."}
            self.socketio.emit("regrpa_status", {"status": "Iniciando..."})
            task2 = RunRegistrationsRpa()
            task2.execute(self)
            return {"success": True, "message": "Sucesso ao ligar RPA."}
        
        @app.route("/registrations-rpa", methods=["DELETE"])
        def turn_off() -> dict[str, str | bool] | tuple[str, int]:
            task1 = VerifyIfHaveAccess()
            if not task1.execute("zRegRpa"):
                return "Sem autorização.", 401
            if self.is_running == False:
                return {"success": False,  "message": "RPA já está desligado."}
            self.socketio.emit("regrpa_status", {"status": "Desligando..."})
            self.stop = True
            return {"success": True,  "message": "Sucesso ao desligar RPA."}
