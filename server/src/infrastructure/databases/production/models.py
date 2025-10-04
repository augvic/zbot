from sqlalchemy import Integer, String
from sqlalchemy.orm import declarative_base, mapped_column

database = declarative_base()

class User(database):
    
    __tablename__ = "users"
    
    user = mapped_column(String, primary_key=True, nullable=True)
    name = mapped_column(String, nullable=True)
    email = mapped_column(String, nullable=True)
    password = mapped_column(String, nullable=True)

class Module(database):
    
    __tablename__ = "modules"
    
    module = mapped_column(String, nullable=True, primary_key=True)
    description = mapped_column(String, nullable=True)

class Permission(database):
    
    __tablename__ = "permissions"
    
    id = mapped_column(Integer, primary_key=True)
    user = mapped_column(String, nullable=True)
    module = mapped_column(String, nullable=True)

class Registration(database):
    
    __tablename__ = "registrations"
    
    cnpj = mapped_column(String, primary_key=True, nullable=True)
    opening = mapped_column(String, nullable=True)
    company_name = mapped_column(String, nullable=True)
    trade_name = mapped_column(String, nullable=True)
    legal_nature = mapped_column(String, nullable=True)
    legal_nature_id = mapped_column(String, nullable=True)
    registration_status = mapped_column(String, nullable=True)
    street = mapped_column(String, nullable=True)
    number = mapped_column(String, nullable=True)
    complement = mapped_column(String, nullable=True)
    neighborhood = mapped_column(String, nullable=True)
    pac = mapped_column(String, nullable=True)
    city = mapped_column(String, nullable=True)
    state = mapped_column(String, nullable=True)
    fone = mapped_column(String, nullable=True)
    email = mapped_column(String, nullable=True)
    tax_regime = mapped_column(String, nullable=True)
    comission_receipt = mapped_column(String, nullable=True)
    status = mapped_column(String, nullable=True)
    registration_date_hour = mapped_column(String, nullable=True)
    charge_date_hour = mapped_column(String, nullable=True)
    federal_revenue_consult_date = mapped_column(String, nullable=True)
    doc_resent = mapped_column(String, nullable=True)
    client_type = mapped_column(String, nullable=True)
    suggested_limit = mapped_column(String, nullable=True)
    seller = mapped_column(String, nullable=True)
    cpf = mapped_column(String, nullable=True)
    cpf_person = mapped_column(String, nullable=True)

class Ncea(database):
    
    __tablename__ = "nceas"
    
    id = mapped_column(Integer, primary_key=True)
    cnpj = mapped_column(String, nullable=True)
    ncea = mapped_column(String, nullable=True)
    description = mapped_column(String, nullable=True)

class StateRegistration(database):
    
    __tablename__ = "state_registrations"
    
    id = mapped_column(Integer, primary_key=True)
    cnpj = mapped_column(String, nullable=True)
    state_registration = mapped_column(String, nullable=True)
    status = mapped_column(String, nullable=True)

class SuframaRegistration(database):
    
    __tablename__ = "suframa_registrations"
    
    id = mapped_column(Integer, primary_key=True)
    cnpj = mapped_column(String, nullable=True)
    suframa_registration = mapped_column(String, nullable=True)
    status = mapped_column(String, nullable=True)
