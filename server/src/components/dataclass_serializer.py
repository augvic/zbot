from dataclasses import asdict
from typing import Any

class DataclassSerializer:
    
    def serialize(self, object: Any) -> dict[str, Any]:
        return asdict(object)
    
    def serialize_list(self, objects: list[Any]) -> list[dict[str, Any]]:
        return [self.serialize(object) for object in objects]
