from src.components.sap_clients.clients.financial_data_getter import FinancialDataGetter
from src.components.sap_clients.models import *
from src.components.dataclass_serializer import DataclassSerializer
from typing import Any
from datetime import datetime

class GetFinancialData:
    
    def __init__(self) -> None:
        self.financial_data_driver = FinancialDataGetter()
        self.serializer = DataclassSerializer()
    
    def execute(self, cnpj_root: str) -> dict[str, Any]:
        try:
            data = self.serializer.serialize(self.financial_data_driver.get_data(cnpj_root=cnpj_root))
            data["success"] = True
            return data
        except Exception as error:
            try:
                self.financial_data_driver.go_home()
            except:
                pass
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            return {"success": False, "message": "Erro ao consultar dados financeiros."}
