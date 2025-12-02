from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.log_system import LogSystem
from src.modules.model_serializer import ModelSerializer

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class GetModules:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        log_system: LogSystem,
        serializer: ModelSerializer
    ) -> None:
        self.database_handler = database_handler
        self.log_system = log_system
        self.serializer = serializer
    
    def main(self, user: str) -> Response:
        try:
            modules = self.serializer.serialize_sqla_list(self.database_handler.modules_client.read_all())
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Módulos coletados.")
            return Response(success=True, message="✅ Módulos coletados.", data=modules)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({user}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao coletar lista de módulos. Contate o administrador.")
