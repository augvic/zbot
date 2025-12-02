from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.log_system import LogSystem
from src.modules.model_serializer import ModelSerializer

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class Module:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        log_system: LogSystem,
        serializer: ModelSerializer
    ) -> None:
        self.database_handler = database_handler
        self.log_system = log_system
        self.serializer = serializer
    
    def create(self, user: str, module: str, description: str) -> Response:
        try:
            if not module:
                self.log_system.write_text(f"👤 Usuário ({user}): ❌ Preencha o módulo.")
                return Response(success=False, message="❌ Preencha o módulo.", data=[])
            if self.database_handler.modules_client.read(module):
                self.log_system.write_text(f"👤 Usuário ({user}): ❌ Módulo ({module}) já existe.")
                return Response(success=False, message=f"❌ Módulo ({module}) já existe.", data=[])
            if description == "":
                self.log_system.write_text(f"👤 Usuário ({user}): ❌ Preencha a descrição.")
                return Response(success=False, message="❌ Preencha a descrição.", data=[])
            self.database_handler.modules_client.create(module, description)
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Módulo ({module}) adicionado.")
            return Response(success=True, message=f"✅ Módulo ({module}) adicionado.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({user}) ao criar módulo ({module}). ❌ Erro: {error}")
            raise Exception(f"❌ Erro interno ao criar módulo. Contate o administrador.")
