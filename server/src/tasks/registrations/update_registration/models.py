from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str

@dataclass
class RegistrationData:
    
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
    tax_regime: str
    comission_receipt: str
    status: str
    client_type: str
    suggested_limit: float
    seller: str
    cpf: str
    cpf_person: str
