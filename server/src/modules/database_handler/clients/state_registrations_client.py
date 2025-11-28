from ..models.database_models import StateRegistration

from sqlalchemy.orm import sessionmaker

class StateRegistrationsClient:
    
    def __init__(self, session_construct: sessionmaker):
        self.session_construct = session_construct
    
    def create(self,
        cnpj: str,
        state_registration: str,
        status: str
    ) -> None:
        try:
            session = self.session_construct()
            to_create = StateRegistration(
                cnpj=cnpj,
                state_registration=state_registration,
                status=status
            )
            session.add(to_create)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"Error in (StateRegistrationsClient) component in (create) method: {error}.")
    
    def read_all(self, cnpj: str) -> list[StateRegistration]:
        try:
            session = self.session_construct()
            return session.query(StateRegistration).filter(StateRegistration.cnpj == cnpj).all()
        except Exception as error:
            raise Exception(f"Error in (StateRegistrationsClient) component in (read_all) method: {error}.")
    
    def delete(self, cnpj: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(StateRegistration).filter(StateRegistration.cnpj == cnpj).all()
            for delete in to_delete:
                session.delete(delete)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"Error in (StateRegistrationsClient) component in (delete) method: {error}.")
