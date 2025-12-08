from typing import TypedDict

from datetime import datetime
from pandas import DataFrame

class FinancialDict(TypedDict):
    
    fbl5n_table: list[dict[str, str]]
    maturity: datetime | str
    limit: float

class CleanedFinancialDict(TypedDict):
    
    fbl5n_table: DataFrame | None
    maturity: datetime | str
    limit: float | str
    in_open: float | str
    overdue_nfs: str
    margin: float | str
