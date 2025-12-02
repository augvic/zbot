from src.modules.positivo_federal_revenue_api.positivo_federal_revenue_api import PositivoFederalRevenueApi
from src.modules.log_system import LogSystem

from dataclasses import dataclass
from src.modules.positivo_federal_revenue_api.models import FederalRevenueData

@dataclass
class Response:
    
    success: bool
    message: str
    data: FederalRevenueData | None

class GetFederalRevenueData:
    
    def __init__(self,
        federal_revenue_api: PositivoFederalRevenueApi,
        log_system: LogSystem,
    ) -> None:
        self.federal_revenue_api = federal_revenue_api
        self.log_system = log_system
    
    def main(self, user: str, cnpj: str) -> Response:
        try:
            if len(cnpj) != 14:
                self.log_system.write_text(f"👤 Usuário ({user}): ❌ CNPJ ({cnpj}) não possui 14 dígitos.")
                return Response(success=False, message="❌ CNPJ ({cnpj}) não possui 14 dígitos.", data=None)
            data = self.federal_revenue_api.get_data(cnpj=cnpj)
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Dados da receita coletados: {data}.")
            return Response(success=True, message="✅ Dados da receita coletados.", data=data)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({user}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao obter dados da Receita Federal. Contate o administrador.")
