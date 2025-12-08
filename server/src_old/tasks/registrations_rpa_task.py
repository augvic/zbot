from src.engines.log_engine import LogEngine
from src.engines.date_engine import DateEngine
from src.engines.thread_engine import ThreadEngine
from src.engines.time_engine import TimeEngine
from src.engines.event_bus_engine import EventBusEngine
from src.engines.wsgi_engine.wsgi_session_manager_engine import WsgiSessionManagerEngine
from src.engines.cli_session_manager_engine import CliSessionManagerEngine

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: str

class RegistrationsRpaTask:
    
    def __init__(self,
        session_manager_engine: WsgiSessionManagerEngine | CliSessionManagerEngine,
        time_engine: TimeEngine,
        log_engine: LogEngine,
        thread_engine: ThreadEngine,
        date_engine: DateEngine,
        event_bus_engine: EventBusEngine,
        need_authentication: bool
    ) -> None:
        self.time_engine = time_engine
        self.log_engine = log_engine
        self.event_bus_engine = event_bus_engine
        self.thread_engine = thread_engine
        self.date_engine = date_engine
        self.session_manager_engine = session_manager_engine
        self.need_authentication = need_authentication
        self.is_running = False
        self.stop = False
        self.memory: list[str] = []
        self.day = self.date_engine.get_today_datetime()
    
    def _message(self, text: str) -> None:
        self.log_engine.write_text(text)
        self.memory.append(text)
        self.event_bus_engine.emit("regrpa_terminal", {"message": text})
    
    def _loop(self) -> None:
        try:
            self.event_bus_engine.emit("regrpa_notification", {"success": True, "message": "✅ RPA iniciado."})
            self.event_bus_engine.emit("regrpa_status", {"message": "Em processamento..."})
            self._message(f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ RPA iniciado.")
            self.is_running = True
            while True:
                if self.day != self.date_engine.get_today_datetime():
                    self.memory.clear()
                    self.day = self.date_engine.get_today_datetime()
                if self.stop == True:
                    self.event_bus_engine.emit("regrpa_notification", {"success": True, "message": "✅ RPA desligado."})
                    self.event_bus_engine.emit("regrpa_status", {"message": "Desligado."})
                    self._message(f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ RPA desligado.")
                    self.stop = False
                    self.is_running = False
                    break
                self._message("Em execução")
                self.time_engine.sleep(2)
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (RegistrationsRpaTask) task in (loop) method: {error}")
            self.event_bus_engine.emit("regrpa_status", {"message": "Desligado."})
            self.event_bus_engine.emit("regrpa_notification", {"success": False, "message": "❌ Erro durante execução do RPA."})
            self.stop = False
            self.is_running = False
    
    def memory_to_str(self) -> Response:
        try:
            if not self.session_manager_engine.is_user_in_session():
                return Response(success=False, message="❌ Necessário fazer login.", data="")
            if not self.session_manager_engine.have_user_module_access("zRegRpa"):
                return Response(success=False, message="❌ Sem acesso.", data="")
            memory_string = ""
            for message in self.memory:
                memory_string += message + "\n"
            return Response(success=True, message="✅ Memória coletada.", data=memory_string)
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (RegistrationsRpaTask) task in (memory_to_str) method: {error}")
            raise Exception("❌ Erro interno ao coletar memória do RPA. Contate o administrador.")
    
    def stop_rpa(self) -> Response:
        try:
            if not self.session_manager_engine.is_user_in_session():
                return Response(success=False, message="❌ Necessário fazer login.", data="")
            if not self.session_manager_engine.have_user_module_access("zRegRpa"):
                return Response(success=False, message="❌ Sem acesso.", data="")
            if self.is_running == False:
                return Response(success=False, message="❌ RPA já está desligado.", data="")
            self.event_bus_engine.emit("regrpa_status", {"message": "Desligando..."})
            self.stop = True
            return Response(success=True, message="✅ Solicitação de encerramento do RPA bem sucedida.", data="")
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (RegistrationsRpaTask) task in (run) method: {error}")
            raise Exception("❌ Erro interno ao desligar RPA. Contate o administrador.")
    
    def main(self) -> Response:
        try:
            if self.need_authentication:
                if not self.session_manager_engine.is_user_in_session():
                    return Response(success=False, message="❌ Necessário fazer login.", data="")
                if not self.session_manager_engine.have_user_module_access("zRegRpa"):
                    return Response(success=False, message="❌ Sem acesso.", data="")
            if self.is_running == True:
                return Response(success=False, message="❌ RPA já está em processamento.", data="")
            self.thread_engine.init(target=self._loop)
            self.thread_engine.start()
            return Response(success=True, message="✅ Solicitação de inicio do RPA bem sucedida.", data="")
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (RegistrationsRpaTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao iniciar RPA. Contate o administrador.")
