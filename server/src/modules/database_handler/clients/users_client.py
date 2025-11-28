from ..models.database_models import User

from sqlalchemy.orm import sessionmaker

class UsersClient:
    
    def __init__(self, session_construct: sessionmaker):
        self.session_construct = session_construct
    
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
