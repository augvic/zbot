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
