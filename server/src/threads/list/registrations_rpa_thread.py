from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: str

class RegistrationsRpa:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
        self.is_running = False
        self.stop = False
        self.memory: list[str] = []
        self.day = self.engines.date_engine.get_today_datetime()
    
    def _message(self, text: str) -> None:
        self.engines.log_engine.write_text("rpas/registrations_rpa", text)
        self.memory.append(text)
        self.engines.event_bus_engine.emit("regrpa_terminal", {"message": text})
    
    def _loop(self) -> None:
        try:
            self.engines.event_bus_engine.emit("regrpa_notification", {"success": True, "message": "✅ RPA iniciado."})
            self.engines.event_bus_engine.emit("regrpa_status", {"message": "Em processamento..."})
            self._message(f"✅ RPA iniciado.")
            self.is_running = True
            while True:
                if self.day != self.engines.date_engine.get_today_datetime():
                    self.memory.clear()
                    self.day = self.engines.date_engine.get_today_datetime()
                if self.stop == True:
                    self.engines.event_bus_engine.emit("regrpa_notification", {"success": True, "message": "✅ RPA desligado."})
                    self.engines.event_bus_engine.emit("regrpa_status", {"message": "Desligado."})
                    self._message(f"✅ RPA desligado.")
                    self.stop = False
                    self.is_running = False
                    break
                self._message("Em execução")
                self.engines.time_engine.sleep(2)
        except Exception:
            self.engines.event_bus_engine.emit("regrpa_status", {"message": "Desligado."})
            self.engines.event_bus_engine.emit("regrpa_notification", {"success": False, "message": "❌ Erro durante execução do RPA."})
            self.stop = False
            self.is_running = False
    
    def memory_to_str(self) -> str:
        try:
            memory_string = ""
            for message in self.memory:
                memory_string += message + "\n"
            return memory_string
        except Exception as error:
            raise Exception(f"❌ Error in (RegistrationsRpa) in (memory_to_str) method: {error}")
    
    def stop_rpa(self) -> Response:
        try:
            if self.is_running == False:
                return Response(success=False, message="❌ RPA já está desligado.", data="")
            self.engines.event_bus_engine.emit("regrpa_status", {"message": "Desligando..."})
            self.stop = True
            return Response(success=True, message="✅ Solicitação de encerramento do RPA bem sucedida.", data="")
        except Exception as error:
            raise Exception(f"❌ Error in (RegistrationsRpa) in (stop_rpa) method: {error}")
    
    def main(self) -> Response:
        try:
            if self.is_running == True:
                return Response(success=False, message="❌ RPA já está em processamento.", data="")
            self.engines.thread_engine.start_single_thread(target=self._loop)
            return Response(success=True, message="✅ Solicitação de inicio do RPA bem sucedida.", data="")
        except Exception as error:
            raise Exception(f"❌ Error in (RegistrationsRpa) in (main) method: {error}")
