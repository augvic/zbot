from src.components.database_clients.clients.modules_client import ModulesClient
from src.components.sqla_serializer import SqlaSerializer
from src.components.session_manager import SessionManager
from src.components.log_system import LogSystem
from .models import Response

class GetModulesList:
    
    def __init__(self) -> None:
        self.modules_client = ModulesClient("prd")
        self.session_manager = SessionManager()
        self.serializer = SqlaSerializer()
        self.log_system = LogSystem("get_modules_list")
    
    def execute(self) -> Response:
        try:
            modules = self.serializer.serialize_list(self.modules_client.read_all())
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n✅ Módulos coletados.")
            return Response(success=True, message="✅ Módulos coletados.", data=modules)
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Erro:\n{error}")
            raise Exception("❌ Erro interno ao coletar lista de módulos. Contate o administrador.")
