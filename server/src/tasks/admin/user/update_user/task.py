from src.components.infra.database_clients.clients.users_client import UsersClient
from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class UpdateUser:
    
    def __init__(self) -> None:
        self.users_client = UsersClient("prd")
        self.session_manager = SessionManager()
        self.log_system = LogSystem("admin/user")
    
    def execute(self,
        user: str,
        name: str,
        email: str,
        password: str
    ) -> Response:
        try:
            user_exists = self.users_client.read(user)
            if user_exists == None:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Usuário não existe.")
                return Response(success=False, message="❌ Usuário não existe.")
            if user == "":
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Preencha o usuário.")
                return Response(success=False, message="❌ Preencha o usuário.")
            if not str(user).isdigit():
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Usuário deve ser somente números.")
                return Response(success=False, message="❌ Usuário deve ser somente números.")
            if name == "":
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Preencha o nome.")
                return Response(success=False, message="❌ Preencha o nome.")
            if email == "":
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Preencha o e-mail.")
                return Response(success=False, message="❌ Preencha o e-mail.")
            if not "@" in email or not "." in email:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Preencha um e-mail válido.")
                return Response(success=False, message="❌ Preencha um e-mail válido.")
            if password == "":
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Preencha a senha.")
                return Response(success=False, message="❌ Preencha a senha.")
            if user_exists.name == name and user_exists.email == email and user_exists.password == password:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Nenhum dado do usuário modificado.")
                return Response(success=False, message="❌ Nenhum dado do usuário modificado.")
            self.users_client.update(user, name, email, password)
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n✅ Usuário atualizado.")
            return Response(success=True, message="✅ Usuário atualizado.")
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Erro:\n{error}")
            raise Exception("❌ Erro interno ao atualizar usuário. Contate o administrador.")
