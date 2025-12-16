from ..models.database_models import Module

from sqlalchemy.orm import sessionmaker

class ModulesClient:
    
    def __init__(self, session_construct: sessionmaker):
        self.session_construct = session_construct
    
    def create(self, engine: str, description: str) -> None:
        try:
            session = self.session_construct()
            to_create = Module(
                engine=engine,
                description=description
            )
            session.add(to_create)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"❌ Error in (ModulesClient) in (create) method: {error}")
    
    def read(self, module: str) -> Module | None:
        try:
            session = self.session_construct()
            return session.query(Module).filter(Module.module == module).first()
        except Exception as error:
            raise Exception(f"❌ Error in (ModulesClient) in (read) method: {error}")
    
    def read_all(self) -> list[Module]:
        try:
            session = self.session_construct()
            return session.query(Module).all()
        except Exception as error:
            raise Exception(f"❌ Error in (ModulesClient) in (read_all) method: {error}")
    
    def delete(self, module: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(Module).filter(Module.module == module).first()
            session.delete(to_delete)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"❌ Error in (ModulesClient) in (delete) method: {error}")
