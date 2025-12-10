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
        self.runtime = "cli"
    
    def set_runtime(self, runtime: str) -> None:
        self.runtime = runtime
    
    def main(self, cnpj: str) -> Response:
        try:
            if self.runtime == "cli":
                self.session_manager_engine = self.engines.cli_session_engine
            else:
                self.session_manager_engine = self.engines.wsgi_engine.session_manager
            if len(cnpj) != 14:
                return Response(success=False, message="❌ CNPJ ({cnpj}) não possui 14 dígitos.", data=None)
            data = self.engines.federal_revenue_api_engine.get_data(cnpj=cnpj)
            self.engines.log_engine.write_text("tasks/get_federal_revenue_data_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Dados da receita coletados: {self.engines.serializer_engine.serialize_dataclass(data)}.")
            return Response(success=True, message="✅ Dados da receita coletados.", data=data)
        except Exception as error:
            self.engines.log_engine.write_error("tasks/get_federal_revenue_data_task", f"❌ Error in (GetFederalRevenueDataTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao obter dados da Receita Federal. Contate o administrador.")
