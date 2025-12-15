from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class DeleteUserTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
    
    def main(self, user: str) -> Response:
        try:
            user_exists = self.engines.database_engine.users_client.read(user)
            if user_exists == None:
                return Response(success=False, message=f"❌ Usuário ({user}) não existe.", data=[])
            if user == "72776":
                return Response(success=False, message="❌ Usuário 72776 não pode ser removido.", data=[])
            self.engines.database_engine.users_client.delete(user)
            return Response(success=True, message=f"✅ Usuário ({user}) removido.", data=[])
        except Exception as error:
            raise Exception(f"❌ Error in (DeleteUserTask) in (main) method: {error}")
