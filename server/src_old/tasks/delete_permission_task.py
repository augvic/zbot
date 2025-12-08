from src.engines.database_engine.database_engine import DatabaseEngine
from src.engines.log_engine import LogEngine
from src.engines.wsgi_engine.wsgi_session_manager_engine import WsgiSessionManagerEngine
from src.engines.cli_session_manager_engine import CliSessionManagerEngine

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class DeletePermissionTask:
    
    def __init__(self,
        database_engine: DatabaseEngine,
        log_engine: LogEngine,
        session_manager_engine: WsgiSessionManagerEngine | CliSessionManagerEngine,
        need_authentication: bool
    ) -> None:
        self.database_engine = database_engine
        self.log_engine = log_engine
        self.session_manager_engine = session_manager_engine
        self.need_authentication = need_authentication
    
    def main(self, user: str, permission: str) -> Response:
        try:
            if self.need_authentication:
                if not self.session_manager_engine.is_user_in_session():
                    return Response(success=False, message="❌ Necessário fazer login.", data=[])
                if not self.session_manager_engine.have_user_module_access("zAdmin"):
                    return Response(success=False, message="❌ Sem acesso.", data=[])
            permission_exists = self.database_engine.users_client.read(user)
            if permission_exists == None:
                return Response(success=False, message=f"❌ Permissão ({permission}) não existe.", data=[])
            if user == "72776" and permission == "zAdmin":
                return Response(success=False, message="❌ Permissão zAdmin do 72776 não pode ser removida.", data=[])
            self.database_engine.permissions_client.delete_from_user(user, permission)
            self.log_engine.write_text(f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Permissão ({permission}) removida.")
            return Response(success=True, message=f"✅ Permissão ({permission}) removida.", data=[])
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (DeletePermissionTask) task in (main) method: {error}")
            raise Exception(f"❌ Erro interno ao deletar permissão. Contate o administrador.")
