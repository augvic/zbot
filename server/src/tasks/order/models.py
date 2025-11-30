from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str

@dataclass
class PartnerModel:
    
    key: str
    code: str

@dataclass
class ComissionModel:
    
    key: str
    code: str
    percentage: str

@dataclass
class ItemModel:
    
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
class OrderModel:
    
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
    items: list[ItemModel]
    partners: list[PartnerModel]
    comissions: list[ComissionModel]
