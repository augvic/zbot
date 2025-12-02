from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.log_system import LogSystem

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class UpdateUser:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        log_system: LogSystem
    ) -> None:
        self.database_handler = database_handler
        self.log_system = log_system
    
    def main(self,
        task_user: str,
        user: str,
        name: str,
        email: str,
        password: str
    ) -> Response:
        try:
            user_exists = self.database_handler.users_client.read(user)
            if user_exists == None:
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Usuário ({user}) não existe.")
                return Response(success=False, message="❌ Usuário não existe.", data=[])
            if not user:
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Preencha o usuário.")
                return Response(success=False, message="❌ Preencha o usuário.", data=[])
            if not str(user).isdigit():
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Usuário deve ser somente números.")
                return Response(success=False, message="❌ Usuário deve ser somente números.", data=[])
            if not name:
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Preencha o nome.")
                return Response(success=False, message="❌ Preencha o nome.", data=[])
            if not email:
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Preencha o e-mail.")
                return Response(success=False, message="❌ Preencha o e-mail.", data=[])
            if not "@" in email or not "." in email:
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Preencha um e-mail válido.")
                return Response(success=False, message="❌ Preencha um e-mail válido.", data=[])
            if not password:
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Preencha a senha.")
                return Response(success=False, message="❌ Preencha a senha.", data=[])
            if user_exists.name == name and user_exists.email == email and user_exists.password == password:
                self.log_system.write_text(f"👤 Usuário ({task_user}): ⚠️ Nenhum dado do usuário modificado.")
                return Response(success=True, message="⚠️ Nenhum dado do usuário modificado.", data=[])
            self.database_handler.users_client.update(user, name, email, password)
            self.log_system.write_text(f"👤 Usuário ({task_user}): ✅ Usuário ({user}) atualizado.")
            return Response(success=True, message="✅ Usuário atualizado.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({task_user}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao atualizar usuário. Contate o administrador.")
