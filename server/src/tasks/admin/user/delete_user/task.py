from src.components.infra.database_clients.clients.users_client import UsersClient
from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class DeleteUser:
    
    def __init__(self) -> None:
        self.users_client = UsersClient("prd")
        self.session_manager = SessionManager()
        self.log_system = LogSystem("admin/user/delete_user")
    
    def execute(self, user: str) -> Response:
        try:
            user_exists = self.users_client.read(user)
            if user_exists == None:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}) ao deletar usuário: ❌ Usuário ({user}) não existe.")
                return Response(success=False, message=f"❌ Usuário ({user}) não existe.")
            if user == "72776":
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}) ao deletar usuário: ❌ Usuário 72776 não pode ser removido.")
                return Response(success=False, message="❌ Usuário 72776 não pode ser removido.")
            self.users_client.delete(user)
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}) ao deletar usuário: ✅ Usuário ({user}) removido.")
            return Response(success=True, message=f"✅ Usuário ({user}) removido.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário ({self.session_manager.get_from_session("user")}) ao deletar usuário: ❌ Erro: {error}.")
            raise Exception(f"❌ Erro interno ao deletar usuário ({user}). Contate o administrador.")
