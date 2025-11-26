from dataclasses import dataclass
from werkzeug.datastructures import FileStorage

@dataclass
class RequestProcessed:
    
    success: bool
    message: str
    data: dict[str, str]
    files: dict[str, FileStorage]
