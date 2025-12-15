from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class CreateUserTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
    
    def main(self, user: str, name: str, email: str, password: str) -> Response:
        try:
            if not user:
                return Response(success=False, message="❌ Preencha o usuário.", data=[])
            if not str(user).isdigit():
                return Response(success=False, message="❌ Usuário deve ser somente números.", data=[])
            if self.engines.database_engine.users_client.read(user):
                return Response(success=False, message=f"❌ Usuário ({user}) já existe.", data=[])
            if not name:
                return Response(success=False, message="❌ Preencha o nome.", data=[])
            if not email:
                return Response(success=False, message="❌ Preencha o e-mail.", data=[])
            if not "@" in email or not "." in email:
                return Response(success=False, message="❌ Preencha um e-mail válido.", data=[])
            if not password:
                return Response(success=False, message="❌ Preencha a senha.", data=[])
            self.engines.database_engine.users_client.create(user, name, email, password)
            return Response(success=True, message=f"✅ Usuário ({user}) criado.", data=[])
        except Exception as error:
            raise Exception(f"❌ Error in (CreateUserTask) in (main) method: {error}")
