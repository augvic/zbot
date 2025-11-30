from ..models.database_models import SuframaRegistration

from sqlalchemy.orm import sessionmaker

class SuframaRegistrationsClient:
    
    def __init__(self, session_construct: sessionmaker):
        self.session_construct = session_construct
    
    def create(self,
        cnpj: str,
        suframa_registration: str,
        status: str
    ) -> None:
        try:
            session = self.session_construct()
            to_create = SuframaRegistration(
                cnpj=cnpj,
                suframa_registration=suframa_registration,
                status=status
            )
            session.add(to_create)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"Error in (SuframaRegistrationsClient) module in (create) method: {error}")
    
    def read_all(self, cnpj: str) -> list[SuframaRegistration]:
        try:
            session = self.session_construct()
            return session.query(SuframaRegistration).filter(SuframaRegistration.cnpj == cnpj).all()
        except Exception as error:
            raise Exception(f"Error in (SuframaRegistrationsClient) module in (read_all) method: {error}")
    
    def delete(self, cnpj: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(SuframaRegistration).filter(SuframaRegistration.cnpj == cnpj).all()
            for delete in to_delete:
                session.delete(delete)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"Error in (SuframaRegistrationsClient) module in (delete) method: {error}")
