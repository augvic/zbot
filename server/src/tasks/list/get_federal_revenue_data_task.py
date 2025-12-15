from src.engines.engines import Engines

from dataclasses import dataclass
from src.engines.list.federal_revenue_api_engine.models import FederalRevenueData

@dataclass
class Response:
    
    success: bool
    message: str
    data: FederalRevenueData | None

class GetFederalRevenueDataTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
    
    def main(self, cnpj: str) -> Response:
        try:
            if len(cnpj) != 14:
                return Response(success=False, message=f"❌ CNPJ ({cnpj}) não possui 14 dígitos.", data=None)
            data = self.engines.federal_revenue_api_engine.get_data(cnpj=cnpj)
            return Response(success=True, message="✅ Dados da receita coletados.", data=data)
        except Exception as error:
            raise Exception(f"❌ Error in (GetFederalRevenueDataTask) in (main) method: {error}")
