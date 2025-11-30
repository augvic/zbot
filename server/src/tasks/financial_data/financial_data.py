from src.modules.sap_handler.sap_handler import SapHandler
from src.modules.dataclass_serializer import DataclassSerializer
from src.modules.log_system import LogSystem
from src.modules.session_manager import SessionManager
from .models import Response

class FinancialData:
    
    def __init__(self,
        sap_handler: SapHandler,
        serializer: DataclassSerializer,
        log_system: LogSystem,
        session_manager: SessionManager
    ) -> None:
        self.sap_handler = sap_handler
        self.serializer = serializer
        self.log_system = log_system
        self.session_manager = session_manager
    
    def get(self, cnpj_root: str) -> Response:
        try:
            if len(cnpj_root) != 8:
                self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Raiz do CNPJ ({cnpj_root}) não possui 8 dígitos.")
                return Response(success=False, message=f"❌ Raiz do CNPJ ({cnpj_root}) não possui 8 dígitos.", data={})
            data = self.serializer.serialize(self.sap_handler.financial_data_getter.get_data(cnpj_root=cnpj_root))
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Dados financeiros coletados: {data}.")
            return Response(success=True, message="✅ Dados financeiros coletados.", data=data)
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}")
            raise Exception("❌ Erro interno ao consultar dados financeiros. Contate o administrador.")
