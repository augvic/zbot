from src.components.file_system.log_system import LogSystem
from src.components.gear.date_utility import DateUtility
from src.components.infra.socketio_application import SocketIoApplication
from src.components.gear.application_thread import ApplicationThread
from src.components.gear.time_utility import TimeUtility
from src.components.infra.session_manager import SessionManager
from .models import Response

class RunRegistrationsRpa:
    
    def __init__(self, socketio: SocketIoApplication) -> None:
        self.is_running = False
        self.stop = False
        self.memory: list[str] = []
        self.date_utility = DateUtility()
        self.day = self.date_utility.get_today_datetime()
        self.time_utility = TimeUtility()
        self.socketio = socketio
        self.thread = ApplicationThread(target=self.loop)
        self.log_system = LogSystem("rpa/registrations")
        self.session_manager = SessionManager()
    
    def _message(self, text: str) -> None:
        self.log_system.write_text(text)
        self.memory.append(text)
        self.socketio.emit("regrpa_terminal", {"message": text})
    
    def memory_to_str(self) -> str:
        memory_string = ""
        for message in self.memory:
            memory_string += message + "\n"
        return memory_string
    
    def execute(self) -> Response:
        try:
            if self.is_running == True:
                return Response(success=False, message="❌ RPA já está em processamento.")
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n✅ Solicitação de inicio do RPA.")
            self.socketio.emit("regrpa_status", {"status": "Iniciando..."})
            self.thread.start()
            self.socketio.emit("regrpa_notification", {"success": True, "message": "✅ RPA iniciado."})
            self.socketio.emit("regrpa_status", {"status": "Em processamento..."})
            self.is_running = True
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n✅ RPA iniciado.")
            return Response(success=True, message="✅ RPA iniciado.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Erro ao iniciar RPA:\n{error}")
            raise Exception("❌ Erro interno ao iniciar RPA. Contate o administrador.")
    
    def stop_rpa(self) -> Response:
        if self.is_running == False:
            return Response(success=False, message="❌ RPA já está desligado.")
        self.socketio.emit("regrpa_status", {"status": "Desligando..."})
        self.stop = True
        return Response(success=True, message="✅ RPA desligado.")
    
    def loop(self) -> None:
        try:
            while True:
                if self.day != self.date_utility.get_today_datetime():
                    self.memory.clear()
                    self.day = self.date_utility.get_today_datetime()
                if self.stop == True:
                    self.socketio.emit("regrpa_notification", {"success": True, "message": "✅ RPA desligado."})
                    self.socketio.emit("regrpa_status", {"status": "Desligado."})
                    self.stop = False
                    self.is_running = False
                    break
                self._message("Em execução")
                self.time_utility.sleep(2)
        except Exception as error:
            self.log_system.write_error(f"❌ Erro durante execução do RPA.\n{error}")
            self.socketio.emit("regrpa_status", {"status": "Desligado."})
            self.socketio.emit("regrpa_notification", {"success": False, "message": "❌ Erro durante execução do RPA."})
            self.stop = False
            self.is_running = False
