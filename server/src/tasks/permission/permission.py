from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from src.modules.sqla_serializer import SqlaSerializer

from .models import Response

class Permission:
    
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
    
    def create(self, user: str, permission: str) -> Response:
        try:
            user_exists = self.database_handler.users_client.read(user)
            if not user_exists:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar permissão: ❌ Usuário não existe.")
                return Response(success=False, message="❌ Usuário não existe.", data=[])
            if not permission:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar permissão: ❌ Necessário enviar permissão.")
                return Response(success=False, message="❌ Necessário enviar permissão.", data=[])
            self.database_handler.permissions_client.create(user, permission)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar permissão: ✅ Permissão ({permission}) adicionada.")
            return Response(success=True, message=f"✅ Permissão ({permission}) adicionada.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao criar permissão: ❌ Erro: {error}")
            raise Exception(f"❌ Erro interno ao adicionar permissão ({permission}). Contate o administrador.")
    
    def delete(self, user: str, permission: str) -> Response:
        try:
            permission_exists = self.database_handler.users_client.read(user)
            if permission_exists == None:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar permissão: ❌ Permissão ({permission}) não existe.")
                return Response(success=False, message=f"❌ Permissão ({permission}) não existe.", data=[])
            if user == "72776" and permission == "zAdmin":
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar permissão: ❌ Permissão zAdmin do 72776 não pode ser removida.")
                return Response(success=False, message="❌ Permissão zAdmin do 72776 não pode ser removida.", data=[])
            self.database_handler.permissions_client.delete_from_user(user, permission)
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar permissão: ✅ Permissão ({permission}) removida.")
            return Response(success=True, message=f"✅ Permissão ({permission}) removida.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}) ao deletar permissão: ❌ Erro: {error}")
            raise Exception(f"❌ Erro interno ao deletar permissão ({permission}). Contate o administrador.")
    
    def get_all(self, user: str) -> Response:
        try:
            permissions = self.serializer.serialize_list(self.database_handler.permissions_client.read_all_from_user(user))
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Permissões coletadas.")
            return Response(success=True, message="✅ Permissões coletadas.", data=permissions)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao coletar permissões. Contate o administrador.")