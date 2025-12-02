from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.log_system import LogSystem
from src.modules.model_serializer import ModelSerializer

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class DeletePermission:
    
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
            permission_exists = self.database_handler.users_client.read(user)
            if permission_exists == None:
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Permissão ({permission}) não existe.")
                return Response(success=False, message=f"❌ Permissão ({permission}) não existe.", data=[])
            if user == "72776" and permission == "zAdmin":
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Permissão zAdmin do 72776 não pode ser removida.")
                return Response(success=False, message="❌ Permissão zAdmin do 72776 não pode ser removida.", data=[])
            self.database_handler.permissions_client.delete_from_user(user, permission)
            self.log_system.write_text(f"👤 Usuário ({task_user}): ✅ Permissão ({permission}) removida.")
            return Response(success=True, message=f"✅ Permissão ({permission}) removida.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({task_user}): ❌ Erro: {error}")
            raise Exception(f"❌ Erro interno ao deletar permissão ({permission}). Contate o administrador.")
