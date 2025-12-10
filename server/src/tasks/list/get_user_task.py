from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class GetUserTask:
    
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
            if user == "all":
                users = self.engines.database_engine.users_client.read_all()    
            else:
                users = self.engines.database_engine.users_client.read(user)
            if isinstance(users, list):
                users_serialized = self.engines.serializer_engine.serialize_sqla_list(users)
            elif not users:
                return Response(success=False, message=f"❌ Usuário ({user}) não existe.", data=[{}])
            else:
                users_serialized = [self.engines.serializer_engine.serialize_sqla(users)]
            self.engines.log_engine.write_text("tasks/get_user_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Usuário(s) coletado(s) com sucesso.")
            return Response(success=True, message="✅ Usuário(s) coletado(s) com sucesso.", data=users_serialized)
        except Exception as error:
            self.engines.log_engine.write_error("tasks/get_user_task", f"❌ Error in (GetUserTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao coletar usuários. Contate o administrador.")
