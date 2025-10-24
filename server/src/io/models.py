from werkzeug.datastructures import FileStorage
from dataclasses import dataclass

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
    suggested_limit: str | None
    bank_doc: FileStorage | None

@dataclass
class LoginData:
    
    user: str
    password: str
