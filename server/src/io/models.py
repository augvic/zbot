from werkzeug.datastructures import FileStorage
from dataclasses import dataclass

@dataclass
class LoginData:
    
    user: str
    password: str
