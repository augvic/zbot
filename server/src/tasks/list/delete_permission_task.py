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
        self.runtime = "cli"
    
    def set_runtime(self, runtime: str) -> None:
        self.runtime = runtime
    
    def main(self, user: str, permission: str) -> Response:
        try:
            if self.runtime == "cli":
                self.session_manager_engine = self.engines.cli_session_engine
            else:
                self.session_manager_engine = self.engines.wsgi_engine.session_manager
            permission_exists = self.engines.database_engine.users_client.read(user)
            if permission_exists == None:
                return Response(success=False, message=f"❌ Permissão ({permission}) não existe.", data=[])
            if user == "72776" and permission == "zAdmin":
                return Response(success=False, message="❌ Permissão zAdmin do 72776 não pode ser removida.", data=[])
            self.engines.database_engine.permissions_client.delete_from_user(user, permission)
            self.engines.log_engine.write_text("tasks/delete_permission_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Permissão ({permission}) removida.")
            return Response(success=True, message=f"✅ Permissão ({permission}) removida.", data=[])
        except Exception as error:
            self.engines.log_engine.write_error("tasks/delete_permission_task", f"❌ Error in (DeletePermissionTask) task in (main) method: {error}")
            raise Exception(f"❌ Erro interno ao deletar permissão. Contate o administrador.")
