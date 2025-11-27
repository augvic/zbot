from src.modules.positivo_federal_revenue_api.positivo_federal_revenue_api import PositivoFederalRevenueApi
from src.modules.positivo_federal_revenue_api.models import *
from src.modules.dataclass_serializer import DataclassSerializer
from src.modules.log_system import LogSystem
from src.modules.session_manager import SessionManager
from .models import Response

class GetFederalRevenueData:
    
    def __init__(self,
        federal_revenue_data_driver: PositivoFederalRevenueApi,
        serializer: DataclassSerializer,
        log_system: LogSystem,
        session_manager: SessionManager
    ) -> None:
        self.federal_revenue_data_driver = federal_revenue_data_driver
        self.serializer = serializer
        self.log_system = log_system
        self.session_manager = session_manager
    
    def main(self, cnpj: str) -> Response:
        try:
            if len(cnpj) != 14:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ CNPJ ({cnpj}) não possui 14 dígitos.")
                return Response(success=False, message="❌ CNPJ ({cnpj}) não possui 14 dígitos.", data={})
            data = self.serializer.serialize(self.federal_revenue_data_driver.get_data(cnpj=cnpj))
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Dados da receita coletados: {data}.")
            return Response(success=True, message="✅ Dados da receita coletados.", data=data)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao obter dados da Receita Federal. Contate o administrador.")
