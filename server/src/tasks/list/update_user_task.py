from src.engines.list.database_engine.database_engine import DatabaseEngine
from src.engines.list.log_engine import LogEngine
from src.engines.list.wsgi_engine.wsgi_session_manager_engine import WsgiSessionManagerEngine
from src.engines.list.cli_session_manager_engine import CliSessionManagerEngine

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class UpdateUserTask:
    
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
    
    def main(self,
        user: str,
        name: str,
        email: str,
        password: str
    ) -> Response:
        try:
            if self.need_authentication:
                if not self.session_manager_engine.is_user_in_session():
                    return Response(success=False, message="❌ Necessário fazer login.", data=[])
                if not self.session_manager_engine.have_user_module_access("zAdmin"):
                    return Response(success=False, message="❌ Sem acesso.", data=[])
            user_exists = self.database_engine.users_client.read(user)
            if user_exists == None:
                return Response(success=False, message="❌ Usuário não existe.", data=[])
            if not user:
                return Response(success=False, message="❌ Preencha o usuário.", data=[])
            if not str(user).isdigit():
                return Response(success=False, message="❌ Usuário deve ser somente números.", data=[])
            if not name:
                return Response(success=False, message="❌ Preencha o nome.", data=[])
            if not email:
                return Response(success=False, message="❌ Preencha o e-mail.", data=[])
            if not "@" in email or not "." in email:
                return Response(success=False, message="❌ Preencha um e-mail válido.", data=[])
            if not password:
                return Response(success=False, message="❌ Preencha a senha.", data=[])
            if user_exists.name == name and user_exists.email == email and user_exists.password == password:
                return Response(success=True, message="⚠️ Nenhum dado do usuário modificado.", data=[])
            self.database_engine.users_client.update(user, name, email, password)
            self.log_engine.write_text("tasks/update_user_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Usuário ({user}) atualizado.")
            return Response(success=True, message="✅ Usuário atualizado.", data=[])
        except Exception as error:
            self.log_engine.write_error("tasks/update_user_task", f"❌ Error in (UpdateUserTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao atualizar usuário. Contate o administrador.")
