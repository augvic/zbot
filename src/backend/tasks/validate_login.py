from src.backend.infrastructure.drivers.databases.production.clients import UsersClient, PermissionsClient, ModulesClient
from src.backend.infrastructure.managers import SessionManager

class ValidateLogin:
    
    def _setup(self) -> None:
        self.users_client = UsersClient()
        self.session_manager = SessionManager()
        self.permissions_client = PermissionsClient()
        self.modules_client = ModulesClient()
    
    def execute(self, login_data: dict) -> dict:
        self._setup()
        user = self.users_client.read(login_data["user"])
        if user == None:
            return {"success": False}
        if user.password != login_data["password"]:
            return {"success": False}
        self.session_manager.save_in_session("user", user.user)
        modules = self.modules_client.read("all")
        modules_descriptions = {}
        for module in modules:
            modules_descriptions[module.module] = module.description
        user_permissions = self.permissions_client.read(user.user)
        permissions_list = []
        for user_permission in user_permissions:
            permissions_list.append({"module": user_permission.module, "description": modules_descriptions[user_permission.module]})
        self.session_manager.save_in_session("session_modules", permissions_list)
        return {"success": True}
