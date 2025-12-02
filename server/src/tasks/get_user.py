from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.log_system import LogSystem
from src.modules.model_serializer import ModelSerializer

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class GetUser:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        log_system: LogSystem,
        model_serializer: ModelSerializer
    ) -> None:
        self.database_handler = database_handler
        self.log_system = log_system
        self.model_serializer = model_serializer
    
    def main(self, task_user: str, user: str) -> Response:
        try:
            if user == "all":
                users = self.database_handler.users_client.read_all()    
            else:
                users = self.database_handler.users_client.read(user)
            if isinstance(users, list):
                users_serialized = self.model_serializer.serialize_sqla_list(users)
            elif not users:
                self.log_system.write_text(f"👤 Usuário ({task_user}): ❌ Usuário ({user}) não existe.")
                return Response(success=False, message=f"❌ Usuário ({user}) não existe.", data=[{}])
            else:
                users_serialized = [self.model_serializer.serialize_sqla(users)]
            self.log_system.write_text(f"👤 Usuário ({task_user}): ✅ Usuário(s) coletado(s) com sucesso.")
            return Response(success=True, message="✅ Usuário(s) coletado(s) com sucesso.", data=users_serialized)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({task_user}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao coletar usuários. Contate o administrador.")
