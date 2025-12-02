from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.log_system import LogSystem
from src.modules.model_serializer import ModelSerializer

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class GetPermissions:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        log_system: LogSystem,
        serializer: ModelSerializer
    ) -> None:
        self.database_handler = database_handler
        self.log_system = log_system
        self.serializer = serializer
    
    def main(self, task_user: str, user: str) -> Response:
        try:
            permissions = self.serializer.serialize_sqla_list(self.database_handler.permissions_client.read_all_from_user(user))
            self.log_system.write_text(f"👤 Usuário ({task_user}): ✅ Permissões coletadas.")
            return Response(success=True, message="✅ Permissões coletadas.", data=permissions)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({task_user}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao coletar permissões. Contate o administrador.")