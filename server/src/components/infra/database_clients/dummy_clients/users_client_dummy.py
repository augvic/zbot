from ..models.dummy_models import UserDummy

class UsersClientDummy:
    
    def __init__(self):
        self.users = {
            "72776": UserDummy(user="72776", name="Augusto", email="", password="AHVH#72776"),
        }
    
    def create(self, user: str, name: str, email: str, password: str) -> None:
        self.users[user] = UserDummy(user=user, name=name, email=email, password=password)
    
    def read(self, user: str) -> UserDummy | None:
        return self.users.get(user)
    
    def read_all(self) -> list[UserDummy]:
        users_list = []
        for user in self.users.values():
            users_list.append(user)
        return users_list
    
    def update(self, user: str, name: str = "", email: str = "", password: str = "") -> None:
        user_dummy = self.users.get(user)
        if user_dummy:
            user_dummy.name = name
            user_dummy.email = email
            user_dummy.password = password
    
    def delete(self, user: str) -> None:
        if user in self.users:
            del self.users[user]
