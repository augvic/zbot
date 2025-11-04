from src.components.infra.wsgi_application import WsgiApplication
from src.components.file_system.log_system import LogSystem

class GetWsgiApplication:
    
    def __init__(self) -> None:
        self.log_system = LogSystem("application/get_applications")
    
    def execute(self) -> WsgiApplication:
        try:
            return WsgiApplication()
        except Exception as error:
            self.log_system.write_error(f"❌ Error on (GetWsgiApplication) task: {error}.")
            raise Exception("❌ Erro interno ao retornar aplicações necessárias.")
