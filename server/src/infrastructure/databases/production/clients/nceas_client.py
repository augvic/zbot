from src.infrastructure.databases.production.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path

class NceasClient:
    
    def __init__(self):
        BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), "../../../../storage/.databases"))
        url = f"sqlite:///{BASE_DIR}/production.db"
        self.engine = create_engine(url, echo=True, connect_args={"timeout": 30})
        self.session_construct = sessionmaker(bind=self.engine)
        database.metadata.create_all(self.engine)
    
    def create(self,
        cnpj: str,
        ncea: str,
        description: str
    ) -> None:
        session = self.session_construct()
        to_create = Ncea(
            cnpj=cnpj,
            ncea=ncea,
            description=description
        )
        session.add(to_create)
        session.commit()
        session.close()
    
    def read(self, cnpj: str) -> list[Ncea]:
        session = self.session_construct()
        return session.query(Ncea).filter(Ncea.cnpj == cnpj).all()
    
    def delete(self, cnpj: str) -> None:
        session = self.session_construct()
        to_delete = session.query(Ncea).filter(Ncea.cnpj == cnpj).all()
        for delete in to_delete:
            session.delete(delete)
        session.commit()
        session.close()
