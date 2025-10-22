from src.components.database.clients.users_client import UsersClient
from src.components.database.clients.permissions_client import PermissionsClient
from src.components.database.clients.modules_client import ModulesClient
from src.components.session_manager import SessionManager
from datetime import datetime

class ValidateLogin:
    
    def _setup(self) -> None:
        self.users_client = UsersClient("prd")
        self.permissions_client = PermissionsClient("prd")
        self.modules_client = ModulesClient("prd")
        self.session_manager = SessionManager()
    
    def execute(self, login_data: dict[str, str]) -> dict[str, str | bool]:
        self._setup()
        try:
            user = self.users_client.read(login_data["user"])
            if user == None:
                return {"success": False, "message": "Usuário não enviado."}
            if user.password != login_data["password"]:
                return {"success": False, "message": "Login inválido."}
            modules = self.modules_client.read_all()
            modules_descriptions = {}
            for module in modules:
                modules_descriptions[module.module] = module.description
            user_permissions = self.permissions_client.read_all_from_user(user.user)
            permissions_list: list[dict[str, str]] = []
            for user_permission in user_permissions:
                permissions_list.append({"module": user_permission.module, "description": modules_descriptions[user_permission.module]})
            self.session_manager.save_in_session("user", login_data["user"])
            self.session_manager.save_in_session("session_modules", permissions_list)
            return {"success": True, "message": "Logado com sucesso."}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": "Erro ao processar login."}
