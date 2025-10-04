from sqlalchemy.inspection import inspect
from sqlalchemy.orm import DeclarativeBase

class Serializer:
    
    @staticmethod
    def serialize(object: DeclarativeBase) -> dict[str, str]:
        return {attribute.key: getattr(object, attribute.key) for attribute in inspect(object).mapper.column_attrs}
    
    @staticmethod
    def serialize_list(objects: list[DeclarativeBase]):
        return [Serializer.serialize(object) for object in objects]
