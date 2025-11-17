from dataclasses import dataclass
from werkzeug.datastructures import FileStorage

@dataclass
class Response:
    
    success: bool
    message: str

@dataclass
class NewRegistration:
    
    cnpj: str
    seller: str
    email: str
    cpf: str
    cpf_person: str
    tax_regime: str
    article_association_doc: FileStorage
    client_type: str
    suggested_limit: float | None
    bank_doc: FileStorage | None
