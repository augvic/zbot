from ..models.database_models import Permission

from sqlalchemy.orm import sessionmaker

class PermissionsClient:
    
    def __init__(self, session_construct: sessionmaker):
        self.session_construct = session_construct
    
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
            raise Exception(f"❌ Error in (PermissionsClient) engine in (create) method: {error}")
    
    def read_all_from_user(self, user: str) -> list[Permission]:
        try:
            session = self.session_construct()
            return session.query(Permission).filter(Permission.user == user).all()
        except Exception as error:
            raise Exception(f"❌ Error in (PermissionsClient) engine in (read_all_from _user) method: {error}")
    
    def delete_from_user(self, user: str, module: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(Permission).filter(Permission.user == user).filter(Permission.module == module).first()
            session.delete(to_delete)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"❌ Error in (PermissionsClient) engine in (delete_from_user) method: {error}")
    
    def delete_all(self, module: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(Permission).filter(Permission.module == module).all()
            for delete in to_delete:
                session.delete(delete)
            session.commit()
            session.close()
        except Exception as error:
            raise Exception(f"❌ Error in (PermissionsClient) engine in (delete_all) method: {error}")
