from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.log_system import LogSystem

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class CreateUser:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        log_system: LogSystem
    ) -> None:
        self.database_handler = database_handler
        self.log_system = log_system
    
    def main(self, task_user: str, user: str, name: str, email: str, password: str) -> Response:
        try:
            if not user:
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Preencha o usuário.")
                return Response(success=False, message="❌ Preencha o usuário.", data=[])
            if not str(user).isdigit():
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Usuário deve ser somente números.")
                return Response(success=False, message="❌ Usuário deve ser somente números.", data=[])
            if self.database_handler.users_client.read(user):
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Usuário ({user}) já existe.")
                return Response(success=False, message=f"❌ Usuário ({user}) já existe.", data=[])
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
            self.database_handler.users_client.create(user, name, email, password)
            self.log_system.write_text(f"👤 Usuário ({task_user}): ✅ Usuário ({user}) criado.")
            return Response(success=True, message=f"✅ Usuário ({user}) criado.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({task_user}): ❌ Erro: {error}")
            raise Exception(f"❌ Erro interno ao criar usuário ({user}). Contate o administrador.")
