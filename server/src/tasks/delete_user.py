from src.infrastructure.databases.production.clients.users_client import UsersClient
from src.infrastructure.session_manager import SessionManager
from datetime import datetime

class DeleteUser:
    
    def _setup(self) -> None:
        self.users_client = UsersClient()
        self.session_manager = SessionManager()
    
    def execute(self, user: str) -> dict[str, str | bool]:
        self._setup()
        try:
            user_exists = self.users_client.read(user)
            if not user_exists:
                return {"success": False, "message": "Usuário não existe."}
            self.users_client.delete(user)
            return {"success": True, "message": "Usuário removido."}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": "Erro ao deletar usuário."}
