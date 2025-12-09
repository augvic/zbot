from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class DeleteRegistrationTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
        self.runtime = "cli"
    
    def set_runtime(self, runtime: str) -> None:
        self.runtime = runtime
    
    def main(self, cnpj: str) -> Response:
        try:
            if self.runtime == "cli":
                self.session_manager_engine = self.engines.cli_session_engine
            else:
                self.session_manager_engine = self.engines.wsgi_engine.session_manager
            registration_exists = self.engines.database_engine.registrations_client.read(cnpj)
            if registration_exists == None:
                return Response(success=False, message=f"❌ Cadastro ({cnpj}) não existe.", data=[])
            self.engines.database_engine.registrations_client.delete(cnpj)
            self.engines.log_engine.write_text("tasks/delete_registration_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Cadastro ({cnpj}) removido.")
            return Response(success=True, message=f"✅ Cadastro ({cnpj}) removido.", data=[])
        except Exception as error:
            self.engines.log_engine.write_error("tasks/delete_registration_task", f"❌ Error in (DeleteRegistrationTask) task in (main) method: {error}")
            raise Exception(f"❌ Erro interno ao deletar cadastro. Contate o administrador.")
