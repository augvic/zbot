from src.engines.sap_engine.sap_engine import SapEngine
from src.engines.log_engine import LogEngine
from src.engines.serializer_engine import SerializerEngine
from src.engines.wsgi_engine.wsgi_session_manager_engine import WsgiSessionManagerEngine
from src.engines.cli_session_manager_engine import CliSessionManagerEngine

from src.engines.sap_engine.models import FinancialData
from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: FinancialData | None

class GetFinancialDataTask:
    
    def __init__(self,
        sap_engine: SapEngine,
        log_engine: LogEngine,
        serializer_engine: SerializerEngine,
        session_manager_engine: WsgiSessionManagerEngine | CliSessionManagerEngine,
        need_authentication: bool
    ) -> None:
        self.sap_engine = sap_engine
        self.log_engine = log_engine
        self.serializer_engine = serializer_engine
        self.session_manager_engine = session_manager_engine
        self.need_authentication = need_authentication
    
    def main(self, cnpj_root: str) -> Response:
        try:
            if self.need_authentication:
                if not self.session_manager_engine.is_user_in_session():
                    return Response(success=False, message="❌ Necessário fazer login.", data=None)
                if not self.session_manager_engine.have_user_module_access("zFin"):
                    return Response(success=False, message="❌ Sem acesso.", data=None)
            if len(cnpj_root) != 8:
                return Response(success=False, message=f"❌ Raiz do CNPJ ({cnpj_root}) não possui 8 dígitos.", data=None)
            data = self.sap_engine.financial_data_getter.get_data(cnpj_root=cnpj_root)
            self.log_engine.write_text(f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Dados financeiros coletados: {self.serializer_engine.serialize_dataclass(data)}")
            return Response(success=True, message="✅ Dados financeiros coletados.", data=data)
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (GetFinancialDataTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao consultar dados financeiros. Contate o administrador.")
