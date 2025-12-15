from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class DeletePermissionTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
    
    def main(self, user: str, permission: str) -> Response:
        try:
            permission_exists = self.engines.database_engine.users_client.read(user)
            if permission_exists == None:
                return Response(success=False, message=f"❌ Permissão ({permission}) não existe.", data=[])
            if user == "72776" and permission == "zAdmin":
                return Response(success=False, message="❌ Permissão zAdmin do 72776 não pode ser removida.", data=[])
            self.engines.database_engine.permissions_client.delete_from_user(user, permission)
            return Response(success=True, message=f"✅ Permissão ({permission}) removida.", data=[])
        except Exception as error:
            raise Exception(f"❌ Error in (DeletePermissionTask) in (main) method: {error}")
