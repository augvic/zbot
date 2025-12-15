from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class GetUserTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
    
    def main(self, user: str) -> Response:
        try:
            if user == "all":
                users = self.engines.database_engine.users_client.read_all()    
            else:
                users = self.engines.database_engine.users_client.read(user)
            if isinstance(users, list):
                users_serialized = self.engines.serializer_engine.serialize_sqla_list(users)
            elif not users:
                return Response(success=False, message=f"❌ Usuário ({user}) não existe.", data=[{}])
            else:
                users_serialized = [self.engines.serializer_engine.serialize_sqla(users)]
            return Response(success=True, message="✅ Usuário(s) coletado(s) com sucesso.", data=users_serialized)
        except Exception as error:
            raise Exception(f"❌ Error in (GetUserTask) in (main) method: {error}")
