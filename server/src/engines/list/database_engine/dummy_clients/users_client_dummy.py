from ..models.dummy_models import UserDummy

class UsersClientDummy:
    
    def __init__(self):
        self.users = {
            "72776": UserDummy(user="72776", name="Augusto", email="", password="AHVH#72776"),
        }
    
    def create(self, user: str, name: str, email: str, password: str) -> None:
        try:
            self.users[user] = UserDummy(user=user, name=name, email=email, password=password)
        except Exception as error:
            raise Exception(f"❌ Error in (UsersClientDummy) in (create) method: {error}")
    
    def read(self, user: str) -> UserDummy | None:
        try:
            return self.users.get(user)
        except Exception as error:
            raise Exception(f"❌ Error in (UsersClientDummy) in (read) method: {error}")
    
    def read_all(self) -> list[UserDummy]:
        try:
            users_list = []
            for user in self.users.values():
                users_list.append(user)
            return users_list
        except Exception as error:
            raise Exception(f"❌ Error in (UsersClientDummy) in (read_all) method: {error}")
    
    def update(self, user: str, name: str = "", email: str = "", password: str = "") -> None:
        try:
            user_dummy = self.users.get(user)
            if user_dummy:
                user_dummy.name = name
                user_dummy.email = email
                user_dummy.password = password
        except Exception as error:
            raise Exception(f"❌ Error in (UsersClientDummy) in (update) method: {error}")
    
    def delete(self, user: str) -> None:
        try:
            if user in self.users:
                del self.users[user]
        except Exception as error:
            raise Exception(f"❌ Error in (UsersClientDummy) in (delete) method: {error}")
