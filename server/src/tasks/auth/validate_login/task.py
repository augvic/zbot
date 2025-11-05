from src.components.infra.database_clients.clients.users_client import UsersClient
from src.components.infra.database_clients.clients.permissions_client import PermissionsClient
from src.components.infra.database_clients.clients.modules_client import ModulesClient
from src.components.infra.session_manager import SessionManager
from src.components.file_system.log_system import LogSystem
from .models import Response

class ValidateLogin:
    
    def __init__(self,
        users_client: UsersClient,
        permissions_client: PermissionsClient,
        modules_client: ModulesClient,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.users_client = users_client
        self.permissions_client = permissions_client
        self.modules_client = modules_client
        self.session_manager = session_manager
        self.log_system = log_system
    
    def execute(self, user: str, password: str) -> Response:
        try:
            user_orm = self.users_client.read(user)
            if user_orm == None:
                self.log_system.write_text(f"👤 Usuário identificado como ({user}): ❌ Usuário não encontrado.")
                return Response(success=False, message="❌ Usuário não encontrado.")
            if user_orm.password != password:
                self.log_system.write_text(f"👤 Por usuário ({user}): ❌ Senha incorreta.")
                return Response(success=False, message="❌ Login inválido.")
            modules = self.modules_client.read_all()
            modules_descriptions = {}
            for module in modules:
                modules_descriptions[module.module] = module.description
            user_permissions = self.permissions_client.read_all_from_user(user)
            permissions_list: list[dict[str, str]] = []
            for user_permission in user_permissions:
                permissions_list.append({"module": user_permission.module, "description": modules_descriptions[user_permission.module]})
            self.session_manager.save_in_session("user", user)
            self.session_manager.save_in_session("session_modules", permissions_list)
            self.log_system.write_text(f"👤 Por usuário ({user}): ✅ Login realizado com sucesso. Módulos disponíveis: {permissions_list}.")
            return Response(success=True, message=f"✅ Login realizado com sucesso. Módulos disponíveis: {permissions_list}.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário identificado como ({user}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao processar login. Contate o administrador.")
