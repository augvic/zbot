from ..models import PermissionDummy

class PermissionsClientDummy:
    
    def __init__(self):
        self.permissions = {
            "72776": [
                PermissionDummy(user="72776", module="zAdmin"),
                PermissionDummy(user="72776", module="zRegRpa"),
            ]
        }
    
    def create(self, user: str, module: str) -> None:
        self.permissions[user].append(PermissionDummy(user=user, module=module))
    
    def read_all_from_user(self, user: str) -> list[PermissionDummy]:
        permissions = self.permissions.get(user)
        if permissions:
            return permissions
        else:
            return []
    
    def delete_from_user(self, user: str, module: str) -> None:
        for permission_dummy in self.permissions[user]:
            if permission_dummy.module == module:
                self.permissions[user].remove(permission_dummy)
    
    def delete_all(self, module: str) -> None:
        for user in self.permissions.values():
            for permission in user:
                if permission.module == module:
                    user.remove(permission)
