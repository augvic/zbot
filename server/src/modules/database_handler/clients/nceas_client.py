from ..models.database_models import Ncea

from sqlalchemy.orm import sessionmaker

class NceasClient:
    
    def __init__(self, session_construct: sessionmaker):
        self.session_construct = session_construct
    
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
            raise Exception(f"Error in (NceasClient) module in (create) method: {error}")
    
    def read_all(self, cnpj: str) -> list[Ncea]:
        try:
            session = self.session_construct()
            return session.query(Ncea).filter(Ncea.cnpj == cnpj).all()
        except Exception as error:
            raise Exception(f"Error in (NceasClient) module in (read_all) method: {error}")
    
    def delete(self, cnpj: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(Ncea).filter(Ncea.cnpj == cnpj).all()
            for delete in to_delete:
                session.delete(delete)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"Error in (NceasClient) module in (delete) method: {error}")
