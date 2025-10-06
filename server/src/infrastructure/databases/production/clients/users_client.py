from src.infrastructure.databases.production.models import User
from src.infrastructure.databases.production.models import database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path

class UsersClient:
    
    def __init__(self):
        BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), "../../../../storage/.databases"))
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
    
    def read(self, user: str) -> User | None:
        session = self.session_construct()
        return session.query(User).filter(User.user == user).first()
    
    def read_all(self) -> list[User]:
        session = self.session_construct()
        return session.query(User).all()
    
    def update(self, user: str, name: str = "", email: str = "", password: str = "") -> None:
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
    
    def delete(self, user: str) -> None:
        session = self.session_construct()
        to_delete = session.query(User).filter(User.user == user).first()
        session.delete(to_delete)
        session.commit()
