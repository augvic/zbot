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
        self.runtime = "cli"
    
    def set_runtime(self, runtime: str) -> None:
        self.runtime = runtime
    
    def main(self, cnpj_root: str) -> Response:
        try:
            if self.runtime == "cli":
                self.session_manager_engine = self.engines.cli_session_engine
            else:
                self.session_manager_engine = self.engines.wsgi_engine.session_manager
            if len(cnpj_root) != 8:
                return Response(success=False, message=f"❌ Raiz do CNPJ ({cnpj_root}) não possui 8 dígitos.", data=None)
            data = self.engines.sap_engine.financial_data_getter.get_data(cnpj_root=cnpj_root)
            self.engines.log_engine.write_text("tasks/get_financial_data_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Dados financeiros coletados: {self.engines.serializer_engine.serialize_dataclass(data)}")
            return Response(success=True, message="✅ Dados financeiros coletados.", data=data)
        except Exception as error:
            self.engines.log_engine.write_error("tasks/get_financial_data_task", f"❌ Error in (GetFinancialDataTask) task in (main) method: {error}")
            raise Exception("❌ Erro interno ao consultar dados financeiros. Contate o administrador.")
