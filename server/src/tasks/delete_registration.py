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
            registration_exists = self.database_handler.registrations_client.read(cnpj)
            if registration_exists == None:
                self.log_system.write_text(f"👤 Usuário ({user}): ❌ Cadastro ({cnpj}) não existe.")
                return Response(success=False, message=f"❌ Cadastro ({cnpj}) não existe.", data=[])
            self.database_handler.registrations_client.delete(cnpj)
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Cadastro ({cnpj}) removido.")
            return Response(success=True, message=f"✅ Cadastro ({cnpj}) removido.", data=[])
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({user}): ❌ Erro: {error}")
            raise Exception(f"❌ Erro interno ao deletar cadastro. Contate o administrador.")
