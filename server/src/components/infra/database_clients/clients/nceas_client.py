from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path, makedirs
import sys
from ..models.database_models import Ncea
from ..models.database_models import Base

class NceasClient:
    
    def __init__(self, db: str):
        try:
            if getattr(sys, "frozen", False):
                base_path = path.dirname(sys.executable) 
            else:
                base_path = path.join(path.dirname(__file__), "..", "..", "..", "..")
            BASE_DIR = path.abspath(path.join(base_path, "storage", ".databases"))
            makedirs(BASE_DIR, exist_ok=True)
            url = f"sqlite:///{BASE_DIR}/{db}.db"
            self.engine = create_engine(url, echo=True, connect_args={"timeout": 30})
            self.session_construct = sessionmaker(bind=self.engine)
            Base.metadata.create_all(self.engine)
        except Exception as error:
            raise Exception(f"Error in (NceasClient) component in (__init__) method: {error}.")
    
    def create(self,
        cnpj: str,
        ncea: str,
        description: str
    ) -> None:
        try:
            session = self.session_construct()
            to_create = Ncea(
                cnpj=cnpj,
                ncea=ncea,
                description=description
            )
            session.add(to_create)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"Error in (NceasClient) component in (create) method: {error}.")
    
    def read_all(self, cnpj: str) -> list[Ncea]:
        try:
            session = self.session_construct()
            return session.query(Ncea).filter(Ncea.cnpj == cnpj).all()
        except Exception as error:
            raise Exception(f"Error in (NceasClient) component in (read_all) method: {error}.")
    
    def delete(self, cnpj: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(Ncea).filter(Ncea.cnpj == cnpj).all()
            for delete in to_delete:
                session.delete(delete)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"Error in (NceasClient) component in (delete) method: {error}.")
