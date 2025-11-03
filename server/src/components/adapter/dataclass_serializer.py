from dataclasses import asdict
from typing import Any

class DataclassSerializer:
    
    def serialize(self, object: Any) -> dict[str, Any]:
        try:
            return asdict(object)
        except Exception as error:
            raise Exception(f"Error on (DataclassSerializer) component on (serialize) method: {error}")
    
    def serialize_list(self, objects: list[Any]) -> list[dict[str, Any]]:
        try:
            return [self.serialize(object) for object in objects]
        except Exception as error:
            raise Exception(f"Error on DataclassSerializer component on (serialize_list) method: {error}")
