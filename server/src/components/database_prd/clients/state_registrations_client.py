from ..models import StateRegistration
from ..models import database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path

class StateRegistrationsClient:
    
    def __init__(self):
        BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), "../../../../storage/.databases"))
        url = f"sqlite:///{BASE_DIR}/production.db"
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
