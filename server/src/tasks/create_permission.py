from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.log_system import LogSystem
from src.modules.model_serializer import ModelSerializer

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class CreatePermission:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        log_system: LogSystem,
        serializer: ModelSerializer
    ) -> None:
        self.database_handler = database_handler
        self.log_system = log_system
        self.serializer = serializer
    
    def main(self, task_user: str, user: str, permission: str) -> Response:
        try:
            user_exists = self.database_handler.users_client.read(user)
            if not user_exists:
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Usuário não existe.")
                return Response(success=False, message="❌ Usuário não existe.", data=[])
            if not permission:
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Necessário enviar permissão.")
                return Response(success=False, message="❌ Necessário enviar permissão.", data=[])
            self.database_handler.permissions_client.create(user, permission)
            self.log_system.write_text(f"👤 Usuário ({task_user}): ✅ Permissão ({permission}) adicionada.")
            return Response(success=True, message=f"✅ Permissão ({permission}) adicionada.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({task_user}): ❌ Erro: {error}")
            raise Exception(f"❌ Erro interno ao adicionar permissão. Contate o administrador.")
