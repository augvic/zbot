from src.modules.positivo_federal_revenue_api.positivo_federal_revenue_api import PositivoFederalRevenueApi
from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.log_system import LogSystem
from src.modules.date_utility import DateUtility
from src.modules.registrations_docs_handler import RegistrationsDocsHandler
from src.modules.model_serializer import ModelSerializer

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: list[dict]

class Registration:
    
    def __init__(self,
        federal_revenue_api: PositivoFederalRevenueApi,
        database_handler: DatabaseHandler,
        log_system: LogSystem,
        date_utility: DateUtility,
        docs_handler: RegistrationsDocsHandler,
        serializer: ModelSerializer
    ) -> None:
        self.federal_revenue_api = federal_revenue_api
        self.database_handler = database_handler
        self.log_system = log_system
        self.date_utility = date_utility
        self.docs_handler = docs_handler
        self.serializer = serializer
    
    def main(self, user: str, cnpj: str) -> Response:
        try:
            if cnpj == "all":
                registrations = self.database_handler.registrations_client.read_all()    
            else:
                registrations = self.database_handler.registrations_client.read(cnpj)
            if isinstance(registrations, list):
                registrations_serialized = self.serializer.serialize_sqla_list(registrations)
            elif not registrations:
                self.log_system.write_text(f"👤 Usuário ({user}): ❌ Cadastro ({cnpj}) não existe.")
                return Response(success=False, message=f"❌ Cadastro ({cnpj}) não existe.", data=[])
            else:
                registrations_serialized = [self.serializer.serialize_sqla(registrations)]
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Cadastro(s) coletado(s) com sucesso.")
            return Response(success=True, message="✅ Cadastro(s) coletado(s) com sucesso.", data=registrations_serialized)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({user}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao coletar cadastros. Contate o administrador.")
