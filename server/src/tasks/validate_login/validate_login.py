from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from .models import Response

class ValidateLogin:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.database_handler = database_handler
        self.session_manager = session_manager
        self.log_system = log_system
    
    def main(self, user: str, password: str) -> Response:
        try:
            user_orm = self.database_handler.users_client.read(user)
            if user_orm == None:
                self.log_system.write_text(f"👤 Usuário ({user}): ❌ Usuário não encontrado.")
                return Response(success=False, message="❌ Usuário não encontrado.")
            if user_orm.password != password:
                self.log_system.write_text(f"👤 Usuário ({user}): ❌ Senha incorreta.")
                return Response(success=False, message="❌ Login inválido.")
            modules = self.database_handler.modules_client.read_all()
            modules_descriptions = {}
            for module in modules:
                modules_descriptions[module.module] = module.description
            user_permissions = self.database_handler.permissions_client.read_all_from_user(user)
            permissions_list: list[dict[str, str]] = []
            for user_permission in user_permissions:
                permissions_list.append({"module": user_permission.module, "description": modules_descriptions[user_permission.module]})
            self.session_manager.save_in_session("user", user)
            self.session_manager.save_in_session("session_modules", permissions_list)
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Login realizado com sucesso.")
            return Response(success=True, message=f"✅ Login realizado com sucesso.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({user}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao processar login. Contate o administrador.")
