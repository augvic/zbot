from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class CreateUserTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
        self.runtime = "cli"
    
    def set_runtime(self, runtime: str) -> None:
        self.runtime = runtime
    
    def main(self, user: str, name: str, email: str, password: str) -> Response:
        try:
            if self.runtime == "cli":
                self.session_manager_engine = self.engines.cli_session_engine
            else:
                self.session_manager_engine = self.engines.wsgi_engine.session_manager
            if not user:
                return Response(success=False, message="❌ Preencha o usuário.", data=[])
            if not str(user).isdigit():
                return Response(success=False, message="❌ Usuário deve ser somente números.", data=[])
            if self.engines.database_engine.users_client.read(user):
                return Response(success=False, message=f"❌ Usuário ({user}) já existe.", data=[])
            if not name:
                return Response(success=False, message="❌ Preencha o nome.", data=[])
            if not email:
                return Response(success=False, message="❌ Preencha o e-mail.", data=[])
            if not "@" in email or not "." in email:
                return Response(success=False, message="❌ Preencha um e-mail válido.", data=[])
            if not password:
                return Response(success=False, message="❌ Preencha a senha.", data=[])
            self.engines.database_engine.users_client.create(user, name, email, password)
            self.engines.log_engine.write_text("tasks/create_user_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Usuário ({user}) criado.")
            return Response(success=True, message=f"✅ Usuário ({user}) criado.", data=[])
        except Exception as error:
            self.engines.log_engine.write_error("tasks/create_user_task", f"❌ Error in (CreateUserTask) task in (main) method: {error}")
            raise Exception(f"❌ Erro interno ao criar usuário. Contate o administrador.")
