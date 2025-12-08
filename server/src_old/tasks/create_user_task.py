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

class CreateUserTask:
    
    def __init__(self,
        database_engine: DatabaseEngine,
        log_system: LogEngine,
        session_manager_engine: WsgiSessionManagerEngine | CliSessionManagerEngine,
        need_authentication: bool
    ) -> None:
        self.database_engine = database_engine
        self.log_engine = log_system
        self.session_manager_engine = session_manager_engine
        self.need_authentication = need_authentication
    
    def main(self, str, user: str, name: str, email: str, password: str) -> Response:
        try:
            if self.need_authentication:
                if not self.session_manager_engine.is_user_in_session():
                    return Response(success=False, message="❌ Necessário fazer login.", data=[])
                if not self.session_manager_engine.have_user_module_access("zAdmin"):
                    return Response(success=False, message="❌ Sem acesso.", data=[])
            if not user:
                return Response(success=False, message="❌ Preencha o usuário.", data=[])
            if not str(user).isdigit():
                return Response(success=False, message="❌ Usuário deve ser somente números.", data=[])
            if self.database_engine.users_client.read(user):
                return Response(success=False, message=f"❌ Usuário ({user}) já existe.", data=[])
            if not name:
                return Response(success=False, message="❌ Preencha o nome.", data=[])
            if not email:
                return Response(success=False, message="❌ Preencha o e-mail.", data=[])
            if not "@" in email or not "." in email:
                return Response(success=False, message="❌ Preencha um e-mail válido.", data=[])
            if not password:
                return Response(success=False, message="❌ Preencha a senha.", data=[])
            self.database_engine.users_client.create(user, name, email, password)
            self.log_engine.write_text(f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Usuário ({user}) criado.")
            return Response(success=True, message=f"✅ Usuário ({user}) criado.", data=[])
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (CreateUserTask) task in (main) method: {error}")
            raise Exception(f"❌ Erro interno ao criar usuário. Contate o administrador.")
