from src.engines.wsgi_engine.wsgi_session_manager_engine import WsgiSessionManagerEngine
from src.engines.cli_session_manager_engine import CliSessionManagerEngine
from src.engines.log_engine import LogEngine
from src.engines.database_engine.database_engine import DatabaseEngine

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str


class LoginTask:
    
    def __init__(self,
        session_manager_engine: WsgiSessionManagerEngine | CliSessionManagerEngine,
        log_engine: LogEngine,
        database_engine: DatabaseEngine
    ) -> None:
        self.session_manager_engine = session_manager_engine
        self.log_engine = log_engine
        self.database_engine = database_engine
    
    def main(self, user: str, password: str) -> Response:
        try:
            if self.session_manager_engine.is_user_in_session():
                return Response(success=False, message="❌ Usuário já está logado.")                
            user_orm = self.database_engine.users_client.read(user)
            if user_orm == None:
                return Response(success=False, message="❌ Usuário não encontrado.")
            if user_orm.password != password:
                return Response(success=False, message="❌ Login inválido.")
            modules = self.database_engine.modules_client.read_all()
            modules_descriptions = {}
            for module in modules:
                modules_descriptions[module.module] = module.description
            user_permissions = self.database_engine.permissions_client.read_all_from_user(user)
            permissions_list: list[dict[str, str]] = []
            for user_permission in user_permissions:
                permissions_list.append({"module": user_permission.module, "description": modules_descriptions[user_permission.module]})
            self.session_manager_engine.save_in_session("user", user)
            self.session_manager_engine.save_in_session("session_modules", permissions_list)
            self.log_engine.write_text(f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Login realizado com sucesso.")
            return Response(success=True, message=f"✅ Login realizado com sucesso.")
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (LoginTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao processar login. Contate o administrador.")
