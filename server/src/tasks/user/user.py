from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from src.modules.sqla_serializer import SqlaSerializer

from .models import Response

class User:
    
    def __init__(self,
        database_handler: DatabaseHandler,
        session_manager: SessionManager,
        log_system: LogSystem,
        serializer: SqlaSerializer
    ) -> None:
        self.database_handler = database_handler
        self.session_manager = session_manager
        self.log_system = log_system
        self.serializer = serializer
    
    def create(self, user: str, name: str, email: str, password: str) -> Response:
        try:
            if not user:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Preencha o usuário.")
                return Response(success=False, message="❌ Preencha o usuário.", data=[])
            if not str(user).isdigit():
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Usuário deve ser somente números.")
                return Response(success=False, message="❌ Usuário deve ser somente números.", data=[])
            if self.database_handler.users_client.read(user):
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Usuário ({user}) já existe.")
                return Response(success=False, message=f"❌ Usuário ({user}) já existe.", data=[])
            if not name:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Preencha o nome.")
                return Response(success=False, message="❌ Preencha o nome.", data=[])
            if not email:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Preencha o e-mail.")
                return Response(success=False, message="❌ Preencha o e-mail.", data=[])
            if not "@" in email or not "." in email:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Preencha um e-mail válido.")
                return Response(success=False, message="❌ Preencha um e-mail válido.", data=[])
            if not password:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Preencha a senha.")
                return Response(success=False, message="❌ Preencha a senha.", data=[])
            self.database_handler.users_client.create(user, name, email, password)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ✅ Usuário ({user}) criado.")
            return Response(success=True, message=f"✅ Usuário ({user}) criado.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar usuário: ❌ Erro: {error}")
            raise Exception(f"❌ Erro interno ao criar usuário ({user}). Contate o administrador.")
    
    def get(self, user: str) -> Response:
        try:
            if user == "all":
                users = self.database_handler.users_client.read_all()    
            else:
                users = self.database_handler.users_client.read(user)
            if isinstance(users, list):
                users_serialized = self.serializer.serialize_list(users)
            elif not users:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Usuário ({user}) não existe.")
                return Response(success=False, message=f"❌ Usuário ({user}) não existe.", data=[{}])
            else:
                users_serialized = [self.serializer.serialize(users)]
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Usuário(s) coletado(s) com sucesso.")
            return Response(success=True, message="✅ Usuário(s) coletado(s) com sucesso.", data=users_serialized)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao coletar usuários. Contate o administrador.")
    
    def delete(self, user: str) -> Response:
        try:
            user_exists = self.database_handler.users_client.read(user)
            if user_exists == None:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar usuário: ❌ Usuário ({user}) não existe.")
                return Response(success=False, message=f"❌ Usuário ({user}) não existe.", data=[])
            if user == "72776":
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar usuário: ❌ Usuário 72776 não pode ser removido.")
                return Response(success=False, message="❌ Usuário 72776 não pode ser removido.", data=[])
            self.database_handler.users_client.delete(user)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar usuário: ✅ Usuário ({user}) removido.")
            return Response(success=True, message=f"✅ Usuário ({user}) removido.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar usuário: ❌ Erro: {error}")
            raise Exception(f"❌ Erro interno ao deletar usuário ({user}). Contate o administrador.")
    
    def update(self,
        user: str,
        name: str,
        email: str,
        password: str
    ) -> Response:
        try:
            user_exists = self.database_handler.users_client.read(user)
            if user_exists == None:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Usuário ({user}) não existe.")
                return Response(success=False, message="❌ Usuário não existe.", data=[])
            if not user:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o usuário.")
                return Response(success=False, message="❌ Preencha o usuário.", data=[])
            if not str(user).isdigit():
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Usuário deve ser somente números.")
                return Response(success=False, message="❌ Usuário deve ser somente números.", data=[])
            if not name:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o nome.")
                return Response(success=False, message="❌ Preencha o nome.", data=[])
            if not email:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha o e-mail.")
                return Response(success=False, message="❌ Preencha o e-mail.", data=[])
            if not "@" in email or not "." in email:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha um e-mail válido.")
                return Response(success=False, message="❌ Preencha um e-mail válido.", data=[])
            if not password:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Preencha a senha.")
                return Response(success=False, message="❌ Preencha a senha.", data=[])
            if user_exists.name == name and user_exists.email == email and user_exists.password == password:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ⚠️ Nenhum dado do usuário modificado.")
                return Response(success=True, message="⚠️ Nenhum dado do usuário modificado.", data=[])
            self.database_handler.users_client.update(user, name, email, password)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Usuário ({user}) atualizado.")
            return Response(success=True, message="✅ Usuário atualizado.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao atualizar usuário. Contate o administrador.")
