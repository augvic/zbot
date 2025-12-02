from src.modules.log_system import LogSystem
from src.modules.date_utility import DateUtility
from src.modules.application_thread import ApplicationThread
from src.modules.time_utility import TimeUtility
from src.modules.event_bus import EventBus

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str

class RegistrationsRpa:
    
    def __init__(self,
        time_utility: TimeUtility,
        log_system: LogSystem,
        thread: ApplicationThread,
        date_utility: DateUtility,
        event_bus: EventBus
    ) -> None:
        self.time_utility = time_utility
        self.log_system = log_system
        self.event_bus = event_bus
        self.thread = thread
        self.date_utility = date_utility
        self.is_running = False
        self.stop = False
        self.memory: list[str] = []
        self.day = self.date_utility.get_today_datetime()
    
    def _message(self, text: str) -> None:
        self.log_system.write_text(text)
        self.memory.append(text)
        self.event_bus.emit("regrpa_terminal", {"message": text})
    
    def memory_to_str(self, user: str) -> str:
        try:
            memory_string = ""
            for message in self.memory:
                memory_string += message + "\n"
            return memory_string
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({user}): ❌ Erro coletar memória do RPA: {error}")
            raise Exception("❌ Erro interno ao coletar memória do RPA. Contate o administrador.")
    
    def run(self, user: str) -> Response:
        try:
            if self.is_running == True:
                return Response(success=False, message="❌ RPA já está em processamento.")
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Solicitação de inicio do RPA.")
            self.user = user
            self.thread.init(target=self.loop)
            self.thread.start()
            return Response(success=True, message="✅ Solicitação de inicio do RPA bem sucedida.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({user}): ❌ Erro ao iniciar RPA: {error}")
            raise Exception("❌ Erro interno ao iniciar RPA. Contate o administrador.")
    
    def stop_rpa(self, user: str) -> Response:
        try:
            if self.is_running == False:
                return Response(success=False, message="❌ RPA já está desligado.")
            self.event_bus.emit("regrpa_status", {"message": "Desligando..."})
            self.stop = True
            return Response(success=True, message="✅ Solicitação de encerramento do RPA bem sucedida.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({user}): ❌ Erro desligar RPA: {error}")
            raise Exception("❌ Erro interno ao desligar RPA. Contate o administrador.")
    
    def loop(self) -> None:
        try:
            self.event_bus.emit("regrpa_notification", {"success": True, "message": "✅ RPA iniciado."})
            self.event_bus.emit("regrpa_status", {"message": "Em processamento..."})
            self.is_running = True
            self.log_system.write_text(f"👤 Usuário ({self.user}): ✅ RPA iniciado.")
            self.user = ""
            while True:
                if self.day != self.date_utility.get_today_datetime():
                    self.memory.clear()
                    self.day = self.date_utility.get_today_datetime()
                if self.stop == True:
                    self.event_bus.emit("regrpa_notification", {"success": True, "message": "✅ RPA desligado."})
                    self.event_bus.emit("regrpa_status", {"message": "Desligado."})
                    self.stop = False
                    self.is_running = False
                    break
                self._message("Em execução")
                self.time_utility.sleep(2)
        except Exception as error:
            self.log_system.write_error(f"❌ Erro durante execução do RPA: {error}")
            self.event_bus.emit("regrpa_status", {"message": "Desligado."})
            self.event_bus.emit("regrpa_notification", {"success": False, "message": "❌ Erro durante execução do RPA."})
            self.stop = False
            self.is_running = False
