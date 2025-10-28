from src.components.pos_fr_api.component import PositivoFederalRevenueApi
from src.components.pos_fr_api.models import *
from src.components.dataclass_serializer import DataclassSerializer
from src.components.log_system import LogSystem
from src.components.session_manager import SessionManager
from .models import Response

class GetFederalRevenueData:
    
    def __init__(self) -> None:
        self.federal_revenue_data_driver = PositivoFederalRevenueApi()
        self.serializer = DataclassSerializer()
        self.log_system = LogSystem("get_federal_revenue_data")
        self.session_manager = SessionManager()
    
    def execute(self, cnpj: str) -> Response:
        try:
            if len(cnpj) != 14:
                self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ CNPJ: {cnpj} não possui 14 dígitos.")
                return Response(success=False, message="❌ CNPJ: {cnpj} não possui 14 dígitos.", data={})
            data = self.serializer.serialize(self.federal_revenue_data_driver.get_data(cnpj=cnpj))
            self.log_system.write_text(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n✅ Dados da receita coletados:\n{data}.")
            return Response(success=True, message="✅ Dados da receita coletados.", data=data)
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário: {self.session_manager.get_from_session("user")}.\n❌ Erro:\n{error}")
            raise Exception("❌ Erro interno ao obter dados da Receita Federal. Contate o administrador.")
