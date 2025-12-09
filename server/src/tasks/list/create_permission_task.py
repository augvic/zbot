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
        self.runtime = "cli"
    
    def set_runtime(self, runtime: str) -> None:
        self.runtime = runtime
    
    def main(self, user: str, permission: str) -> Response:
        try:
            if self.runtime == "cli":
                self.session_manager_engine = self.engines.cli_session_engine
            else:
                self.session_manager_engine = self.engines.wsgi_engine.session_manager
            user_exists = self.engines.database_engine.users_client.read(user)
            if not user_exists:
                return Response(success=False, message="❌ Usuário não existe.", data=[])
            if not permission:
                return Response(success=False, message="❌ Necessário enviar permissão.", data=[])
            self.engines.database_engine.permissions_client.create(user, permission)
            self.engines.log_engine.write_text("tasks/create_permission_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Permissão ({permission}) adicionada.")
            return Response(success=True, message=f"✅ Permissão ({permission}) adicionada.", data=[])
        except Exception as error:
            self.engines.log_engine.write_error("tasks/create_permission_task", f"❌ Error in (CreatePermissionTask) task in (main) method: {error}")
            raise Exception(f"❌ Erro interno ao adicionar permissão. Contate o administrador.")
