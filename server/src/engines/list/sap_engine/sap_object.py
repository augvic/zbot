import pythoncom

from .clients.sap_gui_client import SapGuiClient
from .clients.order_client import OrderClient
from .clients.financial_data_client import FinancialDataClient

class SapObject:
    
    def __init__(self) -> None:
        pythoncom.CoInitialize()
        self.sap_gui = SapGuiClient()
        self.order_client = OrderClient(self.sap_gui)
        self.financial_data_client = FinancialDataClient(self.sap_gui)
