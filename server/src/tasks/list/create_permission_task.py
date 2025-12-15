from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class CreatePermissionTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
    
    def main(self, user: str, permission: str) -> Response:
        try:
            user_exists = self.engines.database_engine.users_client.read(user)
            if not user_exists:
                return Response(success=False, message="❌ Usuário não existe.", data=[])
            if not permission:
                return Response(success=False, message="❌ Necessário enviar permissão.", data=[])
            self.engines.database_engine.permissions_client.create(user, permission)
            return Response(success=True, message=f"✅ Permissão ({permission}) adicionada.", data=[])
        except Exception as error:
            raise Exception(f"❌ Error in (CreatePermissionTask) in (main) method: {error}")
