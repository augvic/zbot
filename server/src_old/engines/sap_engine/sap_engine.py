from .clients.sap_gui_client import SapGuiClient
from .clients.order_client import OrderClient
from .clients.financial_data_client import FinancialDataClient

class SapEngine:
    
    def __init__(self) -> None:
        self.sap_gui = SapGuiClient()
        self.order_creator = OrderClient(self.sap_gui)
        self.financial_data_getter = FinancialDataClient(self.sap_gui)
