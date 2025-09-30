from src.infrastructure.drivers.databases.production.clients import UsersClient
from src.infrastructure.managers import SessionManager

class DeleteUser:
    
    def _setup(self) -> None:
        self.users_client = UsersClient()
        self.session_manager = SessionManager()
    
    def execute(self, user: str) -> dict | str:
        self._setup()
        if not self.session_manager.is_user_in_session() or not self.session_manager.have_user_module_access("zAdmin"):
            return "Sem autorização.", 401
        user_exists = self.users_client.read(user)
        if not user_exists:
            return {"success": False, "message": "Usuário não existe."}
        self.users_client.delete(user)
        return {"success": True, "message": "Usuário removido."}
