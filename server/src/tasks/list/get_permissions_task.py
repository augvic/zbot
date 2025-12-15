from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class GetPermissionsTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
    
    def main(self, user: str) -> Response:
        try:
            permissions = self.engines.serializer_engine.serialize_sqla_list(self.engines.database_engine.permissions_client.read_all_from_user(user))
            return Response(success=True, message="✅ Permissões coletadas.", data=permissions)
        except Exception as error:
            raise Exception(f"❌ Error in (GetPermissionsTask) in (main) method: {error}")