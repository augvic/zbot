from src.components.infra.database_clients.clients.users_client import UsersClient
from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class UpdateUser:
    
    def __init__(self,
        users_client: UsersClient,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.users_client = users_client
        self.session_manager = session_manager
        self.log_system = log_system
    
    def execute(self,
        user: str,
        name: str,
        email: str,
        password: str
    ) -> Response:
        try:
            user_exists = self.users_client.read(user)
            if user_exists == None:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Usuário ({user}) não existe.")
                return Response(success=False, message="❌ Usuário não existe.")
            if not user:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o usuário.")
                return Response(success=False, message="❌ Preencha o usuário.")
            if not str(user).isdigit():
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Usuário deve ser somente números.")
                return Response(success=False, message="❌ Usuário deve ser somente números.")
            if not name:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o nome.")
                return Response(success=False, message="❌ Preencha o nome.")
            if not email:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o e-mail.")
                return Response(success=False, message="❌ Preencha o e-mail.")
            if not "@" in email or not "." in email:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha um e-mail válido.")
                return Response(success=False, message="❌ Preencha um e-mail válido.")
            if not password:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a senha.")
                return Response(success=False, message="❌ Preencha a senha.")
            if user_exists.name == name and user_exists.email == email and user_exists.password == password:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ⚠️ Nenhum dado do usuário modificado.")
                return Response(success=True, message="⚠️ Nenhum dado do usuário modificado.")
            self.users_client.update(user, name, email, password)
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ✅ Usuário ({user}) atualizado.")
            return Response(success=True, message="✅ Usuário atualizado.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao atualizar usuário. Contate o administrador.")
