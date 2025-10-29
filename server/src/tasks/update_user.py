from src.components.database_clients.clients.users_client import UsersClient
from src.components.infra.session_manager import SessionManager
from datetime import datetime

class UpdateUser:
    
    def __init__(self) -> None:
        self.users_client = UsersClient("prd")
        self.session_manager = SessionManager()
    
    def execute(self, user: str, user_data: dict[str, str]) -> dict[str, str | bool]:
        try:
            user_exists = self.users_client.read(user)
            if user_exists == None:
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
            if user_exists.name == user_data["name"] and user_exists.email == user_data["email"] and user_exists.password == user_data["password"]:
                return {"success": True, "message": "Nenhum dado do usuário modificado."}
            self.users_client.update(user_data["user"], user_data["name"], user_data["email"], user_data["password"])
            return {"success": True, "message": "Usuário atualizado."}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": "Erro ao atualizar usuário."}
