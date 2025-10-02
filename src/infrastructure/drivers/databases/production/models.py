from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

database = declarative_base()

class User(database):
    
    __tablename__ = "users"
    
    user = Column(String, nullable=True, primary_key=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    password = Column(String, nullable=True)

class Module(database):
    
    __tablename__ = "modules"
    
    module = Column(String, nullable=True, primary_key=True)
    description = Column(String, nullable=True)

class Permission(database):
    
    __tablename__ = "permissions"
    
    id = Column(Integer, primary_key=True)
    user = Column(String, nullable=True)
    module = Column(String, nullable=True)

class Registration(database):
    
    __tablename__ = "registrations"
    
    cnpj = Column(String, primary_key=True, nullable=True)
    opening = Column(String, nullable=True)
    company_name = Column(String, nullable=True)
    trade_name = Column(String, nullable=True)
    legal_nature = Column(String, nullable=True)
    legal_nature_id = Column(String, nullable=True)
    registration_status = Column(String, nullable=True)
    street = Column(String, nullable=True)
    number = Column(String, nullable=True)
    complement = Column(String, nullable=True)
    neighborhood = Column(String, nullable=True)
    pac = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    fone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    tax_regime = Column(String, nullable=True)
    comission_receipt = Column(String, nullable=True)
    status = Column(String, nullable=True)
    registration_date_hour = Column(String, nullable=True)
    charge_date_hour = Column(String, nullable=True)
    federal_revenue_consult_date = Column(String, nullable=True)
    doc_resent = Column(String, nullable=True)
    client_type = Column(String, nullable=True)
    suggested_limit = Column(String, nullable=True)
    seller = Column(String, nullable=True)
    cpf = Column(String, nullable=True)
    cpf_person = Column(String, nullable=True)

class Ncea(database):
    
    __tablename__ = "nceas"
    
    id = Column(Integer, primary_key=True)
    cnpj = Column(String, nullable=True)
    ncea = Column(String, nullable=True)
    description = Column(String, nullable=True)

class StateRegistration(database):
    
    __tablename__ = "state_registrations"
    
    id = Column(Integer, primary_key=True)
    cnpj = Column(String, nullable=True)
    state_registration = Column(String, nullable=True)
    status = Column(String, nullable=True)

class SuframaRegistration(database):
    
    __tablename__ = "suframa_registrations"
    
    id = Column(Integer, primary_key=True)
    cnpj = Column(String, nullable=True)
    suframa_registration = Column(String, nullable=True)
    status = Column(String, nullable=True)
