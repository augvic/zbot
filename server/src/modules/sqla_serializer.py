from sqlalchemy.inspection import inspect

from typing import Any

class SqlaSerializer:
    
    def serialize(self, object: Any) -> dict[str, str]:
        try:
            return {attribute.key: getattr(object, attribute.key) for attribute in inspect(object).mapper.column_attrs}
        except Exception as error:
            raise Exception(f"Error in (SqlaSerializer) module in (serialize) method: {error}")
    
    def serialize_list(self, objects: list[Any]):
        try:
            return [self.serialize(object) for object in objects]
        except Exception as error:
            raise Exception(f"Error in (SqlaSerializer) module in (serialize_list) method: {error}")
