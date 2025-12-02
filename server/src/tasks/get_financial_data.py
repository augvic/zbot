from src.modules.sap_handler.sap_handler import SapHandler
from src.modules.log_system import LogSystem
from src.modules.model_serializer import ModelSerializer

from src.modules.sap_handler.models import FinancialData
from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: FinancialData | None

class GetFinancialData:
    
    def __init__(self,
        sap_handler: SapHandler,
        log_system: LogSystem,
        serializer: ModelSerializer
    ) -> None:
        self.sap_handler = sap_handler
        self.log_system = log_system
        self.serializer = serializer
    
    def main(self, user: str, cnpj_root: str) -> Response:
        try:
            if len(cnpj_root) != 8:
                self.log_system.write_text(f"👤 Usuário ({user}): ❌ Raiz do CNPJ ({cnpj_root}) não possui 8 dígitos.")
                return Response(success=False, message=f"❌ Raiz do CNPJ ({cnpj_root}) não possui 8 dígitos.", data=None)
            data = self.sap_handler.financial_data_getter.get_data(cnpj_root=cnpj_root)
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Dados financeiros coletados: {self.serializer.serialize_dataclass(data)}")
            return Response(success=True, message="✅ Dados financeiros coletados.", data=data)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({user}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao consultar dados financeiros. Contate o administrador.")
