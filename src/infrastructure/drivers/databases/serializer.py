from sqlalchemy.inspection import inspect

class Serializer:
    
    @staticmethod
    def serialize(object):
        return {attribute.key: getattr(object, attribute.key) for attribute in inspect(object).mapper.column_attrs}
    
    @staticmethod
    def serialize_list(objects):
        return [Serializer.serialize(object) for object in objects]
