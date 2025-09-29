from src.backend.infrastructure.drivers.databases.production.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path

class UsersClient:
    
    def __init__(self):
        BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), "../../../../../../.databases"))
        url = f"sqlite:///{BASE_DIR}/production.db"
        self.engine = create_engine(url, echo=True, connect_args={"timeout": 30})
        self.session_construct = sessionmaker(bind=self.engine)
        database.metadata.create_all(self.engine)
    
    def create(self, user: str, name: str, email: str, password: str) -> None:
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
    
    def read(self, user: str) -> User | list[User]:
        session = self.session_construct()
        if user == "all":
            return session.query(User).all()
        else:
            return session.query(User).filter(User.user == user).first()
    
    def update(self, user: str, name: str = None, email: str = None, password: str = None) -> None:
        session = self.session_construct()
        to_update = session.query(User).filter(User.user == user).first()
        if name:
            to_update.name = name
        if email:
            to_update.email = email
        if password:
            to_update.password = password
        session.commit()
        session.refresh(to_update)
        session.close()
    
    def delete(self, user: str) -> None:
        session = self.session_construct()
        to_delete = session.query(User).filter(User.user == user).first()
        session.delete(to_delete)
        session.commit()

if __name__ == "__main__":
    database = UsersClient()
    database.delete("ac\zc")
