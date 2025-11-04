from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path, makedirs
import sys
from ..models.database_models import Permission
from ..models.database_models import Base

class PermissionsClient:
    
    def __init__(self, db: str):
        try:
            if getattr(sys, "frozen", False):
                base_path = path.dirname(sys.executable) 
            else:
                base_path = path.join(path.dirname(__file__), "..", "..", "..", "..")
            BASE_DIR = path.abspath(path.join(base_path, "storage", ".databases"))
            makedirs(BASE_DIR, exist_ok=True)
            url = f"sqlite:///{BASE_DIR}/{db}.db"
            self.engine = create_engine(url, echo=True, connect_args={"timeout": 30})
            self.session_construct = sessionmaker(bind=self.engine)
            Base.metadata.create_all(self.engine)
        except Exception as error:
            raise Exception(f"Error in (PermissionsClient) component in (__init__) method: {error}.")
    
    def create(self, user: str, module: str) -> None:
        try:
            session = self.session_construct()
            to_create = Permission(
                user=user,
                module=module
            )
            session.add(to_create)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"Error in (PermissionsClient) component in (create) method: {error}.")
    
    def read_all_from_user(self, user: str) -> list[Permission]:
        try:
            session = self.session_construct()
            return session.query(Permission).filter(Permission.user == user).all()
        except Exception as error:
            raise Exception(f"Error in (PermissionsClient) component in (read_all_from _user) method: {error}.")
    
    def delete_from_user(self, user: str, module: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(Permission).filter(Permission.user == user).filter(Permission.module == module).first()
            session.delete(to_delete)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"Error in (PermissionsClient) component in (delete_from_user) method: {error}.")
    
    def delete_all(self, module: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(Permission).filter(Permission.module == module).all()
            for delete in to_delete:
                session.delete(delete)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"Error in (PermissionsClient) component in (delete_all) method: {error}.")
