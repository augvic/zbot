from src.infrastructure.databases.production.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path

class PermissionsClient:
    
    def __init__(self):
        BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), "../../../../storage/.databases"))
        url = f"sqlite:///{BASE_DIR}/production.db"
        self.engine = create_engine(url, echo=True, connect_args={"timeout": 30})
        self.session_construct = sessionmaker(bind=self.engine)
        database.metadata.create_all(self.engine)
    
    def create(self, user: str, module: str) -> None:
        session = self.session_construct()
        to_create = Permission(
            user=user,
            module=module
        )
        session.add(to_create)
        session.commit()
        session.close()
    
    def read(self, user: str) -> list[Permission]:
        session = self.session_construct()
        return session.query(Permission).filter(Permission.user == user).all()
    
    def delete(self, user: str, module: str) -> None:
        session = self.session_construct()
        to_delete = session.query(Permission).filter(Permission.user == user).filter(Permission.module == module).first()
        session.delete(to_delete)
        session.commit()
        session.close()
