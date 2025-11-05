from src.components.infra.sap_clients.clients.financial_data_getter import FinancialDataGetter
from src.components.infra.sap_clients.models import *
from src.components.adapter.dataclass_serializer import DataclassSerializer
from src.components.file_system.log_system import LogSystem
from src.components.infra.session_manager import SessionManager
from .models import Response

class GetFinancialData:
    
    def __init__(self,
        financial_data_driver: FinancialDataGetter,
        serializer: DataclassSerializer,
        log_system: LogSystem,
        session_manager: SessionManager
    ) -> None:
        self.financial_data_driver = financial_data_driver
        self.serializer = serializer
        self.log_system = log_system
        self.session_manager = session_manager
    
    def execute(self, cnpj_root: str) -> Response:
        try:
            if len(cnpj_root) != 8:
                self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Raiz do CNPJ ({cnpj_root}) não possui 8 dígitos.")
                return Response(success=False, message=f"❌ Raiz do CNPJ ({cnpj_root}) não possui 8 dígitos.", data={})
            data = self.serializer.serialize(self.financial_data_driver.get_data(cnpj_root=cnpj_root))
            self.log_system.write_text(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ✅ Dados financeiros coletados: {data}.")
            return Response(success=True, message="✅ Dados financeiros coletados.", data=data)
        except Exception as error:
            self.log_system.write_error(f"👤 Por usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            raise Exception("❌ Erro interno ao consultar dados financeiros. Contate o administrador.")
