from src.components.database.clients.users_client import UsersClient
from src.components.session_manager import SessionManager
from datetime import datetime

class DeleteUser:
    
    def __init__(self) -> None:
        self.users_client = UsersClient("prd")
        self.session_manager = SessionManager()
    
    def execute(self, user: str) -> dict[str, str | bool]:
        try:
            user_exists = self.users_client.read(user)
            if user_exists == None:
                return {"success": False, "message": f"Usuário ({user}) não existe."}
            if user == "72776":
                return {"success": False, "message": "Criador não pode ser removido."}
            self.users_client.delete(user)
            return {"success": True, "message": f"Usuário ({user}) removido."}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": f"Erro ao deletar usuário ({user})."}
