from src.components.infra.socketio_application import SocketIoApplication
from src.components.infra.wsgi_application import WsgiApplication
from src.components.file_system.log_system import LogSystem

class GetSocketIoApplication:
    
    def __init__(self) -> None:
        self.log_system = LogSystem("application/get_applications")
    
    def execute(self, app: WsgiApplication) -> SocketIoApplication:
        try:
            return SocketIoApplication(app)
        except Exception as error:
            self.log_system.write_error(f"❌ Error in (GetSocketIoApplication) task: {error}.")
            raise Exception("❌ Erro interno ao retornar aplicações necessárias.")
