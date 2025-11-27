from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from .models import Response

class CreatePermission:
    
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
            user_exists = self.database_handler.users_client.read(user)
            if not user_exists:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar permissão: ❌ Usuário não existe.")
                return Response(success=False, message="❌ Usuário não existe.")
            if not permission:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar permissão: ❌ Necessário enviar permissão.")
                return Response(success=False, message="❌ Necessário enviar permissão.")
            self.database_handler.permissions_client.create(user, permission)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar permissão: ✅ Permissão ({permission}) adicionada.")
            return Response(success=True, message=f"✅ Permissão ({permission}) adicionada.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar permissão: ❌ Erro: {error}.")
            raise Exception(f"❌ Erro interno ao adicionar permissão ({permission}). Contate o administrador.")
