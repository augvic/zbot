from ..models.dummy_models import PermissionDummy

class PermissionsClientDummy:
    
    def __init__(self):
        self.permissions = {
            "72776": [
                PermissionDummy(user="72776", module="zAdmin"),
                PermissionDummy(user="72776", module="zRegRpa"),
            ]
        }
    
    def create(self, user: str, module: str) -> None:
        try:
            self.permissions[user].append(PermissionDummy(user=user, module=module))
        except Exception as error:
            raise Exception(f"❌ Error in (PermissionsClientDummy) engine in (create) method: {error}")
    
    def read_all_from_user(self, user: str) -> list[PermissionDummy]:
        try:
            permissions = self.permissions.get(user)
            if permissions:
                return permissions
            else:
                return []
        except Exception as error:
            raise Exception(f"❌ Error in (PermissionsClientDummy) engine in (read_all_from_user) method: {error}")
    
    def delete_from_user(self, user: str, module: str) -> None:
        try:
            for permission_dummy in self.permissions[user]:
                if permission_dummy.module == module:
                    self.permissions[user].remove(permission_dummy)
        except Exception as error:
            raise Exception(f"❌ Error in (PermissionsClientDummy) engine in (delete_from_user) method: {error}")
    
    def delete_all(self, module: str) -> None:
        try:
            for user in self.permissions.values():
                for permission in user:
                    if permission.module == module:
                        user.remove(permission)
        except Exception as error:
            raise Exception(f"❌ Error in (PermissionsClientDummy) engine in (delete_all) method: {error}")
