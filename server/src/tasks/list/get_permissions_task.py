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
        self.runtime = "cli"
    
    def set_runtime(self, runtime: str) -> None:
        self.runtime = runtime
    
    def main(self, user: str) -> Response:
        try:
            if self.runtime == "cli":
                self.session_manager_engine = self.engines.cli_session_engine
            else:
                self.session_manager_engine = self.engines.wsgi_engine.session_manager
            permissions = self.engines.serializer_engine.serialize_sqla_list(self.engines.database_engine.permissions_client.read_all_from_user(user))
            self.engines.log_engine.write_text("tasks/get_permissions_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Permissões coletadas: {permissions}")
            return Response(success=True, message="✅ Permissões coletadas.", data=permissions)
        except Exception as error:
            self.engines.log_engine.write_error("tasks/get_permissions_task", f"❌ Error in (GetPermissionsTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao coletar permissões. Contate o administrador.")