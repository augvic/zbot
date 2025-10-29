from src.components.database_clients.clients.permissions_client import PermissionsClient
from src.components.adapter.sqla_serializer import SqlaSerializer
from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class GetPermissions:
    
    def __init__(self) -> None:
        self.permissions_client = PermissionsClient("prd")
        self.session_manager = SessionManager()
        self.serializer = SqlaSerializer()
        self.log_system = LogSystem("auth")
    
    def execute(self, user: str) -> Response:
        try:
            permissions = self.serializer.serialize_list(self.permissions_client.read_all_from_user(user))
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n✅ Permissões coletadas.")
            return Response(success=True, message="✅ Permissões coletadas.", data=permissions)
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Erro:\n{error}")
            raise Exception("❌ Erro interno ao coletar permissões. Contate o administrador.")
