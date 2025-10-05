from sqlalchemy.inspection import inspect
from typing import Any

class SqlaSerializer:
    
    def serialize(self, object: Any) -> dict[str, str]:
        return {attribute.key: getattr(object, attribute.key) for attribute in inspect(object).mapper.column_attrs}
    
    def serialize_list(self, objects: list[Any]):
        return [self.serialize(object) for object in objects]
