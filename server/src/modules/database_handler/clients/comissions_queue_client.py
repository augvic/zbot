from ..models.database_models import ComissionQueue
from sqlalchemy.orm import sessionmaker

class ComissionsQueueClient:
    
    def __init__(self, session_construct: sessionmaker) -> None:
        self.session_construct = session_construct
    
    def create(self,
        order_ref: str,
        key: str,
        code: str,
        percentage: str
    ) -> None:
        try:
            session = self.session_construct()
            to_create = ComissionQueue(
                order_ref=order_ref,
                key=key,
                code=code,
                percentage=percentage
            )
            session.add(to_create)
            session.commit()
            session.refresh(to_create)
            session.close()
        except Exception as error:
            raise Exception(f"Error in (ComissionsQueueClient) component in (create) method: {error}.")
    
    def read(self, order: str) -> list[ComissionQueue]:
        try:
            session = self.session_construct()
            return session.query(ComissionQueue).filter(ComissionQueue.order_ref == order).all()
        except Exception as error:
            raise Exception(f"Error in (ComissionsQueueClient) component in (read) method: {error}.")
    
    def delete(self, order: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(ComissionQueue).filter(ComissionQueue.order_ref == order).all()
            for delete_element in to_delete:
                session.delete(delete_element)
            session.commit()
        except Exception as error:
            raise Exception(f"Error in (ComissionsQueueClient) component in (delete) method: {error}.")
