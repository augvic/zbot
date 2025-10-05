from src.infrastructure.federal_revenue_apis.apis import PositivoFederalRevenueApi
from src.infrastructure.federal_revenue_apis.models import *
from src.infrastructure.serializers.dataclass_serializer import DataclassSerializer
from typing import Any
from datetime import datetime

class GetFederalRevenueData:
    
    def _setup(self) -> None:
        self.federal_revenue_data_driver = PositivoFederalRevenueApi()
        self.serializer = DataclassSerializer()
    
    def execute(self, cnpj: str) -> dict[str, Any]:
        self._setup()
        try:
            data = self.serializer.serialize(self.federal_revenue_data_driver.get_data(cnpj=cnpj))
            data["success"] = True
            return data
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": "Erro ao obter dados da Receita Federal."}
