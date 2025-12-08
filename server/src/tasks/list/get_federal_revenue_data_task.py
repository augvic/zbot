from src.engines.federal_revenue_api_engine.federal_revenue_api_engine import FederalRevenueApiEngine
from src.engines.log_engine import LogEngine
from src.engines.serializer_engine import SerializerEngine
from src.engines.wsgi_engine.wsgi_session_manager_engine import WsgiSessionManagerEngine
from src.engines.cli_session_manager_engine import CliSessionManagerEngine

from dataclasses import dataclass
from src.engines.federal_revenue_api_engine.models import FederalRevenueData

@dataclass
class Response:
    
    success: bool
    message: str
    data: FederalRevenueData | None

class GetFederalRevenueDataTask:
    
    def __init__(self,
        federal_revenue_api_engine: FederalRevenueApiEngine,
        log_engine: LogEngine,
        serializer_engine: SerializerEngine,
        session_manager_engine: WsgiSessionManagerEngine | CliSessionManagerEngine,
        need_authentication: bool
    ) -> None:
        self.federal_revenue_api_engine = federal_revenue_api_engine
        self.log_engine = log_engine
        self.serializer_engine = serializer_engine
        self.session_manager_engine = session_manager_engine
        self.need_authentication = need_authentication
    
    def main(self, cnpj: str) -> Response:
        try:
            if self.need_authentication:
                if not self.session_manager_engine.is_user_in_session():
                    return Response(success=False, message="❌ Necessário fazer login.", data=None)
                if not self.session_manager_engine.have_user_module_access("zRecFed"):
                    return Response(success=False, message="❌ Sem acesso.", data=None)
            if len(cnpj) != 14:
                return Response(success=False, message="❌ CNPJ ({cnpj}) não possui 14 dígitos.", data=None)
            data = self.federal_revenue_api_engine.get_data(cnpj=cnpj)
            self.log_engine.write_text(f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Dados da receita coletados: {self.serializer_engine.serialize_dataclass(data)}.")
            return Response(success=True, message="✅ Dados da receita coletados.", data=data)
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (GetFederalRevenueDataTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao obter dados da Receita Federal. Contate o administrador.")
