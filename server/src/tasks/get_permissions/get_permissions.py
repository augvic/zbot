from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.sqla_serializer import SqlaSerializer
from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from .models import Response

class GetPermissions:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        session_manager: SessionManager,
        serializer: SqlaSerializer,
        log_system: LogSystem
    ) -> None:
        self.database_handler = database_handler
        self.session_manager = session_manager
        self.serializer = serializer
        self.log_system = log_system
    
    def main(self, user: str) -> Response:
        try:
            permissions = self.serializer.serialize_list(self.database_handler.permissions_client.read_all_from_user(user))
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Permissões coletadas.")
            return Response(success=True, message="✅ Permissões coletadas.", data=permissions)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao coletar permissões. Contate o administrador.")
