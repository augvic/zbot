from dataclasses import dataclass
from werkzeug.datastructures import FileStorage
from datetime import datetime

@dataclass
class RequestProcessed:
    
    success: bool
    message: str
    data: dict[str, str]
    files: dict[str, FileStorage]

@dataclass
class CreditAnalysisResponse:
    
    order: str
    order_value: str
    status: str
    message: str
    client_margin: str | float
    client_maturity: str | datetime
    client_overdue_nfs: str

@dataclass
class DataToAnalyse:
    
    order: str
    order_value: float
    limit: str
    margin: float | str
    maturity: datetime | str
    overdue_nfs: str
