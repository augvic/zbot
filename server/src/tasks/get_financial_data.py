from src.infrastructure.drivers.sap_clients import FinancialDataGetter
from src.infrastructure.drivers.sap_clients.models import *

class GetFinancialData:
    
    def _setup(self) -> None:
        self.financial_data_driver = FinancialDataGetter()
    
    def execute(self, cnpj_root: str) -> FinancialData:
        self._setup()
        try:
            return self.financial_data_driver.get_data(cnpj_root=cnpj_root)
        except:
            try:
                self.financial_data_driver.go_home()
            except:
                pass
            raise