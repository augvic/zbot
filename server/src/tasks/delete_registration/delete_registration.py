from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from .models import Response

class DeleteRegistration:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        session_manager: SessionManager,
        log_system: LogSystem
    ) -> None:
        self.database_handler = database_handler
        self.session_manager = session_manager
        self.log_system = log_system
    
    def main(self, cnpj: str) -> Response:
        try:
            registration_exists = self.database_handler.registrations_client.read(cnpj)
            if registration_exists == None:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar cadastro: ❌ Cadastro ({cnpj}) não existe.")
                return Response(success=False, message=f"❌ Cadastro ({cnpj}) não existe.")
            self.database_handler.registrations_client.delete(cnpj)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar usuário: ✅ Cadastro ({cnpj}) removido.")
            return Response(success=True, message=f"✅ Cadastro ({cnpj}) removido.")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar usuário: ❌ Erro: {error}.")
            raise Exception(f"❌ Erro interno ao deletar cadastro ({cnpj}). Contate o administrador.")
