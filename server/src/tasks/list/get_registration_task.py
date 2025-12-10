from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class GetRegistrationTask:
    
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
            if cnpj == "all":
                registrations = self.engines.database_engine.registrations_client.read_all()    
            else:
                registrations = self.engines.database_engine.registrations_client.read(cnpj)
            if isinstance(registrations, list):
                registrations_serialized = self.engines.serializer_engine.serialize_sqla_list(registrations)
            elif not registrations:
                return Response(success=False, message=f"❌ Cadastro ({cnpj}) não existe.", data=[])
            else:
                registrations_serialized = [self.engines.serializer_engine.serialize_sqla(registrations)]
            self.engines.log_engine.write_text("tasks/get_registration_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Cadastro(s) coletado(s) com sucesso.")
            return Response(success=True, message="✅ Cadastro(s) coletado(s) com sucesso.", data=registrations_serialized)
        except Exception as error:
            self.engines.log_engine.write_error("tasks/get_registration_task", f"❌ Error in (GetRegistrationTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao coletar cadastros. Contate o administrador.")
