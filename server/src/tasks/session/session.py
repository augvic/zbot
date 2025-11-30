from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from src.modules.request_manager import RequestManager
from src.modules.database_handler.database_handler import DatabaseHandler

from .models import Response

class Session:
    
    def __init__(self,
        session_manager: SessionManager,
        log_system: LogSystem,
        request_manager: RequestManager,
        database_handler: DatabaseHandler
    ) -> None:
        self.session_manager = session_manager
        self.log_system = log_system
        self.request_manager = request_manager
        self.database_handler = database_handler
    
    def get_modules(self) -> Response:
        try:
            session_modules = self.session_manager.get_from_session("session_modules")
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Módulos de sessão coletados: {session_modules}.")
            return Response(success=True, message="✅ Módulos de sessão coletados.", data=session_modules)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao coletar módulos da sessão.")
    
    def get_user(self) -> Response:
        try:
            session_user = self.session_manager.get_from_session("user")
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Usuário de sessão coletado: {session_user}.")
            return Response(success=True, message="✅ Usuário da sessão coletado.", data=session_user)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao coletar usuário de sessão. Contate o administrador.")
    
    def logout(self) -> Response:
        try:
            user = self.session_manager.get_from_session("user")
            self.session_manager.clear_session()
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Logout realizado.")
            return Response(success=True, message="✅ Logout realizado.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.request_manager.get_user_ip()}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao fazer logout. Contate o administrador.")
    
    def login(self, user: str, password: str) -> Response:
        try:
            user_orm = self.database_handler.users_client.read(user)
            if user_orm == None:
                self.log_system.write_text(f"👤 Usuário ({user}): ❌ Usuário não encontrado.")
                return Response(success=False, message="❌ Usuário não encontrado.", data=[])
            if user_orm.password != password:
                self.log_system.write_text(f"👤 Usuário ({user}): ❌ Senha incorreta.")
                return Response(success=False, message="❌ Login inválido.", data=[])
            modules = self.database_handler.modules_client.read_all()
            modules_descriptions = {}
            for module in modules:
                modules_descriptions[module.module] = module.description
            user_permissions = self.database_handler.permissions_client.read_all_from_user(user)
            permissions_list: list[dict[str, str]] = []
            for user_permission in user_permissions:
                permissions_list.append({"module": user_permission.module, "description": modules_descriptions[user_permission.module]})
            self.session_manager.save_in_session("user", user)
            self.session_manager.save_in_session("session_modules", permissions_list)
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Login realizado com sucesso.")
            return Response(success=True, message=f"✅ Login realizado com sucesso.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({user}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao processar login. Contate o administrador.")
    
    def verify_access(self, module: str) -> Response:
        try:
            if not self.session_manager.have_user_module_access(module):
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Não tem acesso ao módulo: ({module}).")
                return Response(success=False, message="❌ Sem autorização.", data=[])
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Tem acesso ao módulo: ({module}).")
            return Response(success=True, message="✅ Tem acesso.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao verificar se possui acesso. Contate o administrador.")
    
    def is_in_session(self) -> Response:
        try:
            if self.session_manager.is_user_in_session():
                self.log_system.write_text(f"✅ Usuário ({self.session_manager.get_from_session("user")}) está na sessão.")
                return Response(success=True, message=f"✅ Usuário ({self.session_manager.get_from_session("user")}) está na sessão.", data=[])
            else:
                self.log_system.write_text(f"❌ Usuário ({self.request_manager.get_user_ip()}) não está na sessão.")
                return Response(success=False, message=f"❌ Não está na sessão.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.request_manager.get_user_ip()}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao verificar se usuário está na sessão. Contate o administrador.")
