from dataclasses import dataclass

from datetime import datetime
from pandas import DataFrame

@dataclass
class FinancialData:
    
    cnpj_root: str
    limit: str | float
    maturity: str | datetime
    in_open: str | float
    margin: str | float
    overdue_nfs: str
    fbl5n_table: DataFrame | None

@dataclass
class Partner:
    
    key: str
    code: str

@dataclass
class Comission:
    
    key: str
    code: str
    percentage: str

@dataclass
class Item:
    
    sku: str
    quantity: str
    center: str
    deposit: str
    guarantee: str
    over: str
    unit_value: float
    total_value: float
    is_parent_item: bool

@dataclass
class Order:
    
    doc_type: str
    organization: str
    channel: str
    office: str
    team: str
    order_name: str
    issuer: str
    receiver: str
    payment_condition: str
    incoterm: str
    reason: str
    table: str
    expedition: str
    payment_way: str
    additional_data: str
    items: list[Item]
    partners: list[Partner]
    comissions: list[Comission]
