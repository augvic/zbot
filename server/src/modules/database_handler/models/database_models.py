from sqlalchemy import Integer, String, Float, Boolean
from sqlalchemy.orm import mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    
    __tablename__ = "users"
    
    user = mapped_column(String, primary_key=True, nullable=True)
    name = mapped_column(String, nullable=True)
    email = mapped_column(String, nullable=True)
    password = mapped_column(String, nullable=True)

class Module(Base):
    
    __tablename__ = "modules"
    
    module = mapped_column(String, nullable=True, primary_key=True)
    description = mapped_column(String, nullable=True)

class Permission(Base):
    
    __tablename__ = "permissions"
    
    id = mapped_column(Integer, primary_key=True)
    user = mapped_column(String, nullable=True)
    module = mapped_column(String, nullable=True)

class Registration(Base):
    
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
    doc_resent = mapped_column(Boolean, nullable=True)
    client_type = mapped_column(String, nullable=True)
    suggested_limit = mapped_column(Float, nullable=True)
    seller = mapped_column(String, nullable=True)
    cpf = mapped_column(String, nullable=True)
    cpf_person = mapped_column(String, nullable=True)

class Ncea(Base):
    
    __tablename__ = "nceas"
    
    id = mapped_column(Integer, primary_key=True)
    cnpj = mapped_column(String, nullable=True)
    ncea = mapped_column(String, nullable=True)
    description = mapped_column(String, nullable=True)

class StateRegistration(Base):
    
    __tablename__ = "state_registrations"
    
    id = mapped_column(Integer, primary_key=True)
    cnpj = mapped_column(String, nullable=True)
    state_registration = mapped_column(String, nullable=True)
    status = mapped_column(String, nullable=True)

class SuframaRegistration(Base):
    
    __tablename__ = "suframa_registrations"
    
    id = mapped_column(Integer, primary_key=True)
    cnpj = mapped_column(String, nullable=True)
    suframa_registration = mapped_column(String, nullable=True)
    status = mapped_column(String, nullable=True)

class PartnerQueue(Base):
    
    __tablename__ = "partners_queue"
    
    id = mapped_column(Integer, primary_key=True)
    order_ref = mapped_column(String, nullable=True)
    key = mapped_column(String, nullable=True)
    code = mapped_column(String, nullable=True)

class ComissionQueue(Base):
    
    __tablename__ = "comissions_queue"
    
    id = mapped_column(Integer, primary_key=True)
    order_ref = mapped_column(String, nullable=True)
    key = mapped_column(String, nullable=True)
    code = mapped_column(String, nullable=True)
    percentage = mapped_column(String, nullable=True)

class ItemQueue(Base):
    
    __tablename__ = "items_queue"
    
    id = mapped_column(Integer, primary_key=True)
    order_ref = mapped_column(String, nullable=True)
    sku = mapped_column(String, nullable=True)
    quantity = mapped_column(String, nullable=True)
    center = mapped_column(String, nullable=True)
    deposit = mapped_column(String, nullable=True)
    guarantee = mapped_column(String, nullable=True)
    over = mapped_column(String, nullable=True)
    unit_value = mapped_column(String, nullable=True)
    total_value = mapped_column(String, nullable=True)
    is_parent_item = mapped_column(String, nullable=True)

class OrderQueue(Base):
    
    __tablename__ = "orders_queue"
    
    order = mapped_column(String, nullable=True, primary_key=True)
    doc_type = mapped_column(String, nullable=True)
    organization = mapped_column(String, nullable=True)
    channel = mapped_column(String, nullable=True)
    office = mapped_column(String, nullable=True)
    team = mapped_column(String, nullable=True)
    order_name = mapped_column(String, nullable=True)
    issuer = mapped_column(String, nullable=True)
    receiver = mapped_column(String, nullable=True)
    payment_condition = mapped_column(String, nullable=True)
    incoterm = mapped_column(String, nullable=True)
    reason = mapped_column(String, nullable=True)
    table = mapped_column(String, nullable=True)
    expedition = mapped_column(String, nullable=True)
    payment_way = mapped_column(String, nullable=True)
    additional_data = mapped_column(String, nullable=True)
    status = mapped_column(String, nullable=True)
