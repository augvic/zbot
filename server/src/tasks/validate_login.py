from src.components.database.clients.users_client import UsersClient
from src.components.database.clients.permissions_client import PermissionsClient
from src.components.database.clients.modules_client import ModulesClient
from src.components.session_manager import SessionManager
from src.components.log_system import LogSystem

from .models import Response

from src.io.models import LoginData

class ValidateLogin:
    
    def __init__(self) -> None:
        self.users_client = UsersClient("prd")
        self.permissions_client = PermissionsClient("prd")
        self.modules_client = ModulesClient("prd")
        self.session_manager = SessionManager()
        self.log_system = LogSystem("login")
    
    def execute(self, login: LoginData) -> Response:
        try:
            user = self.users_client.read(login.user)
            if user == None:
                self.log_system.write_text(f"👤 Usuário identificado como: {login.user}. ❌ Usuário não encontrado.")
                return Response(success=False, message="❌ Usuário não encontrado.")
            if user.password != login.password:
                self.log_system.write_text(f"👤 Por usuário: {login.user}. ❌ Senha incorreta.")
                return Response(success=False, message="❌ Login inválido.")
            modules = self.modules_client.read_all()
            modules_descriptions = {}
            for module in modules:
                modules_descriptions[module.module] = module.description
            user_permissions = self.permissions_client.read_all_from_user(user.user)
            permissions_list: list[dict[str, str]] = []
            for user_permission in user_permissions:
                permissions_list.append({"module": user_permission.module, "description": modules_descriptions[user_permission.module]})
            self.session_manager.save_in_session("user", login.user)
            self.session_manager.save_in_session("session_modules", permissions_list)
            self.log_system.write_text(f"👤 Por usuário: {login.user}\n✅ Login realizado com sucesso. Módulos disponíveis:\n- {'\n- '.join(module['module'] for module in permissions_list)}.")
            return Response(success=True, message=f"✅ Login realizado com sucesso. Módulos disponíveis:\n- {'\n- '.join(module['module'] for module in permissions_list)}.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário identificado como: {login.user}\n❌ Erro:\n{error}")
            raise Exception("❌ Erro interno ao processar login. Contate o administrador.")
