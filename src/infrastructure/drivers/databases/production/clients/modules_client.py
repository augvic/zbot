from src.infrastructure.drivers.databases.production.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path

class ModulesClient:
    
    def __init__(self):
        BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), "../../../../../storage/.databases"))
        url = f"sqlite:///{BASE_DIR}/production.db"
        self.engine = create_engine(url, echo=True, connect_args={"timeout": 30})
        self.session_construct = sessionmaker(bind=self.engine)
        database.metadata.create_all(self.engine)
    
    def create(self, module: str, description: str) -> None:
        session = self.session_construct()
        to_create = Module(
            module=module,
            description=description
        )
        session.add(to_create)
        session.commit()
        session.refresh(to_create)
        session.close()
    
    def read(self, module: str) -> Module | list[Module]:
        session = self.session_construct()
        if module == "all":
            return session.query(Module).all()
        else:
            return session.query(Module).filter(Module.module == module).first()
    
    def update(self, module: str, description: str = None) -> None:
        session = self.session_construct()
        to_update = session.query(Module).filter(Module.module == module).first()
        if description:
            to_update.description = description
        session.commit()
        session.refresh(to_update)
        session.close()
    
    def delete(self, module: str) -> None:
        session = self.session_construct()
        to_delete = session.query(Module).filter(Module.module == module).first()
        session.delete(to_delete)
        session.commit()

if __name__ == "__main__":
    database = ModulesClient()
    database.delete("zadmin")
    database.create("zAdmin", "Gerencie a aplicação.")
