from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class UpdateUserTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
    
    def main(self,
        user: str,
        name: str,
        email: str,
        password: str
    ) -> Response:
        try:
            user_exists = self.engines.database_engine.users_client.read(user)
            if user_exists == None:
                return Response(success=False, message="❌ Usuário não existe.", data=[])
            if not user:
                return Response(success=False, message="❌ Preencha o usuário.", data=[])
            if not str(user).isdigit():
                return Response(success=False, message="❌ Usuário deve ser somente números.", data=[])
            if not name:
                return Response(success=False, message="❌ Preencha o nome.", data=[])
            if not email:
                return Response(success=False, message="❌ Preencha o e-mail.", data=[])
            if not "@" in email or not "." in email:
                return Response(success=False, message="❌ Preencha um e-mail válido.", data=[])
            if not password:
                return Response(success=False, message="❌ Preencha a senha.", data=[])
            if user_exists.name == name and user_exists.email == email and user_exists.password == password:
                return Response(success=True, message="⚠️ Nenhum dado do usuário modificado.", data=[])
            self.engines.database_engine.users_client.update(user, name, email, password)
            return Response(success=True, message="✅ Usuário atualizado.", data=[])
        except Exception as error:
            raise Exception(f"❌ Error in (UpdateUserTask) in (main) method: {error}")
