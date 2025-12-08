from dataclasses import dataclass

@dataclass
class FederalRevenueData:
    
    cnpj: str
    opening: str
    company_name: str
    trade_name: str
    legal_nature: str
    legal_nature_id: str
    registration_status: str
    street: str
    number: str
    complement: str
    neighborhood: str
    pac: str
    city: str
    state: str
    fone: str
    email: str
    state_registrations: list[dict[str, str]]
    suframa_registrations: list[dict[str, str]]
    tax_regime: str
    ncea: list[dict[str, str]]
    comission_receipt: str
