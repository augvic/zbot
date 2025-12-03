from dataclasses import dataclass, field

@dataclass
class Comission:
    
    key: str
    code: str
    percentage: str

@dataclass
class Item:
    
    sku: str
    center: str
    unit_value: str

@dataclass
class Partner:
    
    key: str
    code: str

@dataclass
class Order:
    date: str = ""
    doc_type: str = ""
    organization: list[str] = field(default_factory=list)
    channel: str = ""
    office: str = ""
    team: str = ""
    order_name: str = ""
    order_site: str = ""
    order_erp: str = ""
    resaler_name: str = ""
    receiver_name: str = ""
    resaler_erp: str = ""
    receiver_erp: str = ""
    receiver_type: str = ""
    payment_condition: str = ""
    incoterm: str = ""
    reason: str = ""
    table: str = ""
    expedition: list[str] = field(default_factory=list)
    payment_way: str = ""
    additional_data: str = ""
    comissions: list[Comission] = field(default_factory=list)
    partners: list[Partner] = field(default_factory=list)
    items: list[Item] = field(default_factory=list)
    receiver_cnpj_cpf: str = ""
    receiver_cnpj_root: str = ""
    total_value: str = ""
    status_site: str = ""
    seller: str = ""
    centers: list[str] = field(default_factory=list)
    over: str = ""
    comission_percentage: str = ""
