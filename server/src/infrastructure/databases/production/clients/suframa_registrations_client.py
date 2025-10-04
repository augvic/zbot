from src.infrastructure.databases.production.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path

class SuframaRegistrationsClient:
    
    def __init__(self):
        BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), "../../../../storage/.databases"))
        url = f"sqlite:///{BASE_DIR}/production.db"
        self.engine = create_engine(url, echo=True, connect_args={"timeout": 30})
        self.session_construct = sessionmaker(bind=self.engine)
        database.metadata.create_all(self.engine)
    
    def create(self,
        cnpj: str,
        suframa_registration: str,
        status: str
    ) -> None:
        session = self.session_construct()
        to_create = SuframaRegistration(
            cnpj=cnpj,
            suframa_registration=suframa_registration,
            status=status
        )
        session.add(to_create)
        session.commit()
        session.close()
    
    def read(self, cnpj: str) -> list[SuframaRegistration]:
        session = self.session_construct()
        return session.query(SuframaRegistration).filter(SuframaRegistration.cnpj == cnpj).all()
    
    def delete(self, cnpj: str) -> None:
        session = self.session_construct()
        to_delete = session.query(SuframaRegistration).filter(SuframaRegistration.cnpj == cnpj).all()
        for delete in to_delete:
            session.delete(delete)
        session.commit()
        session.close()
