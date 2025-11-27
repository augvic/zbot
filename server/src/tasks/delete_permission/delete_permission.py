from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from .models import Response

class DeletePermission:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.database_handler = database_handler
        self.session_manager = session_manager
        self.log_system = log_system
    
    def main(self, user: str, permission: str) -> Response:
        try:
            permission_exists = self.database_handler.users_client.read(user)
            if permission_exists == None:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar permissão: ❌ Permissão ({permission}) não existe.")
                return Response(success=False, message=f"❌ Permissão ({permission}) não existe.")
            if user == "72776" and permission == "zAdmin":
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar permissão: ❌ Permissão zAdmin do 72776 não pode ser removida.")
                return Response(success=False, message="❌ Permissão zAdmin do 72776 não pode ser removida.")
            self.database_handler.permissions_client.delete_from_user(user, permission)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar permissão: ✅ Permissão ({permission}) removida.")
            return Response(success=True, message=f"✅ Permissão ({permission}) removida.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar permissão: ❌ Erro: {error}.")
            raise Exception(f"❌ Erro interno ao deletar permissão ({permission}). Contate o administrador.")
