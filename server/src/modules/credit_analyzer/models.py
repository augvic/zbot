from dataclasses import dataclass
from datetime import datetime

@dataclass
class CreditAnalysisResponse:
    
    order: str
    order_value: str
    status: str
    message: str
    client_margin: str | float
    client_maturity: str | datetime
    client_overdue_nfs: str
