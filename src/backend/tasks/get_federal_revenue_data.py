from src.backend.infrastructure.drivers.federal_revenue_apis import PositivoFederalRevenueApi
from src.backend.infrastructure.drivers.federal_revenue_apis.models import *

class GetFederalRevenueData:
    
    def _setup(self) -> None:
        self.federal_revenue_data_driver = PositivoFederalRevenueApi()
    
    def execute(self, cnpj: str) -> FederalRevenueData:
        self._setup()
        try:
            return self.federal_revenue_data_driver.get_data(cnpj=cnpj)
        except:
            raise
