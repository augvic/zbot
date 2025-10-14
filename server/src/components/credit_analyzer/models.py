from datetime import datetime

class CreditAnalysisResponse:
    
    def __init__(self, 
        order: str,
        order_value: str,
        status: str,
        message: str,
        client_margin: str | float,
        client_maturity: str | datetime,
        client_overdue_nfs: str
    ) -> None:
        self.order = order
        self.order_value = order_value
        self.status = status
        self.message = message
        self.client_margin = client_margin
        self.client_maturity = client_maturity
        self.client_overdue_nfs = client_overdue_nfs

class DataToAnalyse:
    
    def __init__(self, 
        order: str,
        order_value: float,
        limit: str,
        margin: float | str,
        maturity: datetime | str,
        overdue_nfs: str
    ) -> None:
        self.order = order
        self.order_value = order_value
        self.limit = limit
        self.margin = margin
        self.maturity = maturity
        self.overdue_nfs = overdue_nfs