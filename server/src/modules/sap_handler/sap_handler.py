from .clients.sap_gui import SapGui
from .clients.order_creator import OrderCreator
from .clients.financial_data_getter import FinancialDataGetter

class SapHandler:
    
    def __init__(self) -> None:
        self.sap_gui = SapGui()
        self.order_creator = OrderCreator(self.sap_gui)
        self.financial_data_getter = FinancialDataGetter(self.sap_gui)
