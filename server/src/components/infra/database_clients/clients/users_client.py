from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path, makedirs
import sys
from ..models.database_models import User
from ..models.database_models import Base

class UsersClient:
    
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
            raise Exception(f"Error in (UsersClient) component in (__init__) method: {error}.")
    
    def create(self, user: str, name: str, email: str, password: str) -> None:
        try:
            session = self.session_construct()
            to_create = User(
                user=user,
                name=name,
                email=email,
                password=password,
            )
            session.add(to_create)
            session.commit()
            session.refresh(to_create)
            session.close()
        except Exception as error:
            raise Exception(f"Error in (UsersClient) component in (create) method: {error}.")
    
    def read(self, user: str) -> User | None:
        try:
            session = self.session_construct()
            return session.query(User).filter(User.user == user).first()
        except Exception as error:
            raise Exception(f"Error in (UsersClient) component in (read) method: {error}.")
    
    def read_all(self) -> list[User]:
        try:
            session = self.session_construct()
            return session.query(User).all()
        except Exception as error:
            raise Exception(f"Error in (UsersClient) component in (read_all) method: {error}.")
    
    def update(self, user: str, name: str = "", email: str = "", password: str = "") -> None:
        try:
            session = self.session_construct()
            to_update = session.query(User).filter(User.user == user).first()
            if to_update:
                if name:
                    to_update.name = name
                if email:
                    to_update.email = email
                if password:
                    to_update.password = password
                session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"Error in (UsersClient) component in (update) method: {error}.")
    
    def delete(self, user: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(User).filter(User.user == user).first()
            session.delete(to_delete)
            session.commit()
        except Exception as error:
            raise Exception(f"Error in (UsersClient) component in (delete) method: {error}.")
