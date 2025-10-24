from dataclasses import dataclass, field
from typing import Any
from werkzeug.datastructures import FileStorage

@dataclass
class Response:
    
    success: bool
    message: Any
    data: dict[str, str] = field(default_factory=dict)
    files: dict[str, FileStorage] = field(default_factory=dict)
