from src.infrastructure.drivers.databases.production.clients import UsersClient
from src.infrastructure.managers import SessionManager

class UpdateUser:
    
    def _setup(self) -> None:
        self.users_client = UsersClient()
        self.session_manager = SessionManager()
    
    def execute(self, user: str, user_data: dict) -> dict | str:
        self._setup()
        if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access("zAdmin"):
            return "Sem autorização.", 401
        user_exists = self.users_client.read(user)
        if not user_exists:
            return {"success": False, "message": "Usuário não existe."}
        if user_data["user"] == "":
            return {"success": False, "message": "Preencha o usuário."}
        if not str(user_data["user"]).isdigit():
            return {"success": False, "message": "Usuário deve ser somente números."}
        if user_data["name"] == "":
            return {"success": False, "message": "Preencha o nome."}
        if user_data["email"] == "":
            return {"success": False, "message": "Preencha o e-mail."}
        if not "@" in user_data["email"] or not "." in user_data["email"]:
            return {"success": False, "message": "Preencha um e-mail válido."}
        if user_data["password"] == "":
            return {"success": False, "message": "Preencha a senha."}
        self.users_client.update(user_data["user"], user_data["name"], user_data["email"], user_data["password"])
        return {"success": True, "message": "Usuário atualizado."}
