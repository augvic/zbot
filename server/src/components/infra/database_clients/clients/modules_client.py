from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path, makedirs
import sys
from ..models.database_models import Module
from ..models.database_models import Base

class ModulesClient:
    
    def __init__(self, db: str):
        try:
            if getattr(sys, "frozen", False):
                base_path = path.dirname(sys.executable) 
            else:
                base_path = path.join(path.dirname(__file__), "..", "..", "..", "..", "..")
            BASE_DIR = path.abspath(path.join(base_path, "storage", ".databases"))
            makedirs(BASE_DIR, exist_ok=True)
            url = f"sqlite:///{BASE_DIR}/{db}.db"
            self.engine = create_engine(url, echo=True, connect_args={"timeout": 30})
            self.session_construct = sessionmaker(bind=self.engine)
            Base.metadata.create_all(self.engine)
        except Exception as error:
            raise Exception(f"Error in (ModulesClient) component in (__init__) method: {error}.")
    
    def create(self, module: str, description: str) -> None:
        try:
            session = self.session_construct()
            to_create = Module(
                module=module,
                description=description
            )
            session.add(to_create)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"Error in (ModulesClient) component in (create) method: {error}.")
    
    def read(self, module: str) -> Module | None:
        try:
            session = self.session_construct()
            return session.query(Module).filter(Module.module == module).first()
        except Exception as error:
            raise Exception(f"Error in (ModulesClient) component in (read) method: {error}.")
    
    def read_all(self) -> list[Module]:
        try:
            session = self.session_construct()
            return session.query(Module).all()
        except Exception as error:
            raise Exception(f"Error in (ModulesClient) component in (read_all) method: {error}.")
    
    def delete(self, module: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(Module).filter(Module.module == module).first()
            session.delete(to_delete)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"Error in (ModulesClient) component in (delete) method: {error}.")
