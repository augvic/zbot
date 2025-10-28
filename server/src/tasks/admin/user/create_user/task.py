from src.components.database_clients.clients.users_client import UsersClient
from src.components.session_manager import SessionManager
from src.components.log_system import LogSystem
from .models import Response

class CreateUser:
    
    def __init__(self) -> None:
        self.users_client = UsersClient("prd")
        self.session_manager = SessionManager()
        self.log_system = LogSystem("admin")
    
    def execute(self, user: str, name: str, email: str, password: str) -> Response:
        try:
            if not user:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao criar usuário).\n❌ Preencha o usuário.")
                return Response(success=False, message="❌ Preencha o usuário.")
            if not str(user).isdigit():
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao criar usuário).\n❌ Usuário deve ser somente números.")
                return Response(success=False, message="❌ Usuário deve ser somente números.")
            if self.users_client.read(user):
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao criar usuário).\n❌ Usuário ({user}) já existe.")
                return Response(success=False, message=f"❌ Usuário ({user}) já existe.")
            if not name:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao criar usuário).\n❌ Preencha o nome.")
                return Response(success=False, message="❌ Preencha o nome.")
            if not email:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao criar usuário).\n❌ Preencha o e-mail.")
                return Response(success=False, message="❌ Preencha o e-mail.")
            if not "@" in email or not "." in email:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao criar usuário).\n❌ Preencha um e-mail válido.")
                return Response(success=False, message="❌ Preencha um e-mail válido.")
            if not password:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao criar usuário).\n❌ Preencha a senha.")
                return Response(success=False, message="❌ Preencha a senha.")
            self.users_client.create(user, name, email, password)
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao criar usuário).\n✅ Usuário ({user}) criado.")
            return Response(success=True, message=f"✅ Usuário ({user}) criado.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")} (ao criar usuário).\n❌ Erro:\n{error}")
            raise Exception(f"❌ Erro interno ao criar usuário ({user}). Contate o administrador.")
