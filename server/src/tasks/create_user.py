from src.infrastructure.databases.production.clients.users_client import UsersClient
from src.infrastructure.session_manager import SessionManager
from datetime import datetime

class CreateUser:
    
    def _setup(self) -> None:
        self.users_client = UsersClient()
        self.session_manager = SessionManager()
    
    def execute(self, user_data: dict[str, str]) -> dict[str, str | bool]:
        self._setup()
        try:
            if user_data["user"] == "":
                return {"success": False, "message": "Preencha o usuário."}
            if not str(user_data["user"]).isdigit():
                return {"success": False, "message": "Usuário deve ser somente números."}
            if self.users_client.read(user_data["user"]):
                return {"success": False, "message": f"Usuário ({user_data["user"]}) já existe."}
            if user_data["name"] == "":
                return {"success": False, "message": "Preencha o nome."}
            if user_data["email"] == "":
                return {"success": False, "message": "Preencha o e-mail."}
            if not "@" in user_data["email"] or not "." in user_data["email"]:
                return {"success": False, "message": "Preencha um e-mail válido."}
            if user_data["password"] == "":
                return {"success": False, "message": "Preencha a senha."}
            self.users_client.create(user_data["user"], user_data["name"], user_data["email"], user_data["password"])
            return {"success": True, "message": f"Usuário ({user_data["user"]}) criado."}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": f"Erro ao criar usuário ({user_data["user"]})."}
