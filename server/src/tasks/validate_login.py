from src.infrastructure.databases.production.clients.users_client import UsersClient
from src.infrastructure.databases.production.clients.permissions_client import PermissionsClient
from src.infrastructure.databases.production.clients.modules_client import ModulesClient
from datetime import datetime

class ValidateLogin:
    
    def _setup(self) -> None:
        self.users_client = UsersClient()
        self.permissions_client = PermissionsClient()
        self.modules_client = ModulesClient()
    
    def execute(self, login_data: dict[str, str]) -> dict[str, str | bool | list[str]]:
        self._setup()
        try:
            user = self.users_client.read(login_data["user"])
            if user == None:
                return {"success": False, "message": "Usuário não enviado."}
            if user.password != login_data["password"]:
                return {"success": False, "message": "Erro ao logar."}
            modules = self.modules_client.read()
            modules_descriptions = {}
            for module in modules:
                modules_descriptions[module.module] = module.description
            user_permissions = self.permissions_client.read(user.user)
            permissions_list: list[str] = []
            for user_permission in user_permissions:
                permissions_list.append({"module": user_permission.module, "description": modules_descriptions[user_permission.module]}) # type: ignore
            return {"success": True, "permissions": permissions_list}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": "Erro ao processar login."}
