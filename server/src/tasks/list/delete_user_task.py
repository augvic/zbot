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
        self.runtime = "cli"
    
    def set_runtime(self, runtime: str) -> None:
        self.runtime = runtime
    
    def main(self, user: str) -> Response:
        try:
            if self.runtime == "cli":
                self.session_manager_engine = self.engines.cli_session_engine
            else:
                self.session_manager_engine = self.engines.wsgi_engine.session_manager
            user_exists = self.engines.database_engine.users_client.read(user)
            if user_exists == None:
                return Response(success=False, message=f"❌ Usuário ({user}) não existe.", data=[])
            if user == "72776":
                return Response(success=False, message="❌ Usuário 72776 não pode ser removido.", data=[])
            self.engines.database_engine.users_client.delete(user)
            self.engines.log_engine.write_text("tasks/delete_user_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Usuário ({user}) removido.")
            return Response(success=True, message=f"✅ Usuário ({user}) removido.", data=[])
        except Exception as error:
            self.engines.log_engine.write_error("tasks/delete_user_task", f"❌ Error in (DeleteUserTask) task in (main) method: {error}")
            raise Exception(f"❌ Erro interno ao deletar usuário. Contate o administrador.")
