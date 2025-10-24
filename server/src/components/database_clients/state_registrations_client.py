from ..models import StateRegistration
from ..models import database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path, makedirs
import sys

class StateRegistrationsClient:
    
    def __init__(self, db: str):
        if getattr(sys, "frozen", False):
            base_path = path.dirname(sys.executable) 
        else:
            base_path = path.join(path.dirname(__file__), "..", "..", "..", "..")
        BASE_DIR = path.abspath(path.join(base_path, "storage", ".databases"))
        makedirs(BASE_DIR, exist_ok=True)
        url = f"sqlite:///{BASE_DIR}/{db}.db"
        self.engine = create_engine(url, echo=True, connect_args={"timeout": 30})
        self.session_construct = sessionmaker(bind=self.engine)
        database.metadata.create_all(self.engine)
    
    def create(self,
        cnpj: str,
        state_registration: str,
        status: str
    ) -> None:
        session = self.session_construct()
        to_create = StateRegistration(
            cnpj=cnpj,
            state_registration=state_registration,
            status=status
        )
        session.add(to_create)
        session.commit()
        session.close()
    
    def read_all(self, cnpj: str) -> list[StateRegistration]:
        session = self.session_construct()
        return session.query(StateRegistration).filter(StateRegistration.cnpj == cnpj).all()
    
    def delete(self, cnpj: str) -> None:
        session = self.session_construct()
        to_delete = session.query(StateRegistration).filter(StateRegistration.cnpj == cnpj).all()
        for delete in to_delete:
            session.delete(delete)
        session.commit()
        session.close()
