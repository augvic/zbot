from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.log_system import LogSystem

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class User:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        log_system: LogSystem,
    ) -> None:
        self.database_handler = database_handler
        self.log_system = log_system
    
    def main(self, task_user: str, user: str) -> Response:
        try:
            user_exists = self.database_handler.users_client.read(user)
            if user_exists == None:
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Usuário ({user}) não existe.")
                return Response(success=False, message=f"❌ Usuário ({user}) não existe.", data=[])
            if user == "72776":
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Usuário 72776 não pode ser removido.")
                return Response(success=False, message="❌ Usuário 72776 não pode ser removido.", data=[])
            self.database_handler.users_client.delete(user)
            self.log_system.write_text(f"👤 Usuário ({task_user}): ✅ Usuário ({user}) removido.")
            return Response(success=True, message=f"✅ Usuário ({user}) removido.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({task_user}): ❌ Erro: {error}")
            raise Exception(f"❌ Erro interno ao deletar usuário ({user}). Contate o administrador.")
