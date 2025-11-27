from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from .models import Response

class CreateUser:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.database_handler = database_handler
        self.session_manager = session_manager
        self.log_system = log_system
    
    def main(self, user: str, name: str, email: str, password: str) -> Response:
        try:
            if not user:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Preencha o usuário.")
                return Response(success=False, message="❌ Preencha o usuário.")
            if not str(user).isdigit():
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Usuário deve ser somente números.")
                return Response(success=False, message="❌ Usuário deve ser somente números.")
            if self.database_handler.users_client.read(user):
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Usuário ({user}) já existe.")
                return Response(success=False, message=f"❌ Usuário ({user}) já existe.")
            if not name:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Preencha o nome.")
                return Response(success=False, message="❌ Preencha o nome.")
            if not email:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Preencha o e-mail.")
                return Response(success=False, message="❌ Preencha o e-mail.")
            if not "@" in email or not "." in email:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Preencha um e-mail válido.")
                return Response(success=False, message="❌ Preencha um e-mail válido.")
            if not password:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Preencha a senha.")
                return Response(success=False, message="❌ Preencha a senha.")
            self.database_handler.users_client.create(user, name, email, password)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ✅ Usuário ({user}) criado.")
            return Response(success=True, message=f"✅ Usuário ({user}) criado.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Erro: {error}.")
            raise Exception(f"❌ Erro interno ao criar usuário ({user}). Contate o administrador.")
