from dataclasses import asdict
from sqlalchemy.inspection import inspect

from typing import Any

class SerializerEngine:
    
    def serialize_dataclass(self, object: Any) -> dict[str, Any]:
        try:
            return asdict(object)
        except Exception as error:
            raise Exception(f"❌ Error in (SerializerEngine) engine in (serialize) method: {error}")
    
    def serialize_dataclass_list(self, objects: list[Any]) -> list[dict[str, Any]]:
        try:
            return [self.serialize_dataclass(object) for object in objects]
        except Exception as error:
            raise Exception(f"❌ Error in (SerializerEngine) engine in (serialize_list) method: {error}")
        
    def serialize_sqla(self, object: Any) -> dict[str, str]:
        try:
            return {attribute.key: getattr(object, attribute.key) for attribute in inspect(object).mapper.column_attrs}
        except Exception as error:
            raise Exception(f"❌ Error in (SqlaSerializer) in (serialize) method: {error}")
    
    def serialize_sqla_list(self, objects: list[Any]):
        try:
            return [self.serialize_sqla(object) for object in objects]
        except Exception as error:
            raise Exception(f"❌ Error in (SqlaSerializer) in (serialize_list) method: {error}")
