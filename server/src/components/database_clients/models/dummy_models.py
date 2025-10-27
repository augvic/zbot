from dataclasses import dataclass

@dataclass
class UserDummy:
    
    user: str
    name: str
    email: str
    password: str

@dataclass
class PermissionDummy:
    
    user: str
    module: str
