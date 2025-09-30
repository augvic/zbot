class CreditAnalysisResponse:
    
    def __init__(self, 
        order: str,
        order_value: str,
        status: str,
        message: str,
        client_margin: str,
        client_maturity: str,
        client_overdue_nfs: str
    ) -> None:
        self.order = order
        self.order_value = order_value
        self.status = status
        self.message = message
        self.client_margin = client_margin
        self.client_maturity = client_maturity
        self.client_overdue_nfs = client_overdue_nfs
