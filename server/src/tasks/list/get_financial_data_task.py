from src.engines.engines import Engines

from src.engines.list.sap_engine.models import FinancialData
from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: FinancialData | None

class GetFinancialDataTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
    
    def main(self, cnpj_root: str) -> Response:
        try:
            if len(cnpj_root) != 8:
                return Response(success=False, message=f"❌ Raiz do CNPJ ({cnpj_root}) não possui 8 dígitos.", data=None)
            data = self.engines.sap_engine.financial_data_getter.get_data(cnpj_root=cnpj_root)
            return Response(success=True, message="✅ Dados financeiros coletados.", data=data)
        except Exception as error:
            raise Exception(f"❌ Error in (GetFinancialDataTask) in (main) method: {error}")
