from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.log_system import LogSystem
from src.modules.model_serializer import ModelSerializer

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class DeleteModule:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        log_system: LogSystem,
        serializer: ModelSerializer
    ) -> None:
        self.database_handler = database_handler
        self.log_system = log_system
        self.serializer = serializer
    
    def main(self, user: str, module: str) -> Response:
        try:
            module_exists = self.database_handler.modules_client.read(module)
            if module_exists == None:
                self.log_system.write_text(f"👤 Usuário ({user}): ❌ Módulo ({module}) não existe.")
                return Response(success=False, message=f"❌ Módulo ({module}) não existe.", data=[])
            if module == "zAdmin":
                self.log_system.write_text(f"👤 Usuário ({user}): ❌ zAdmin não pode ser removido.")
                return Response(success=False, message="❌ zAdmin não pode ser removido.", data=[])
            self.database_handler.modules_client.delete(module)
            self.database_handler.permissions_client.delete_all(module)
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Módulo ({module}) removido.")
            return Response(success=True, message=f"✅ Módulo ({module}) removido.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({user}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao deletar módulo ({module}). Contate o administrador.")
