from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path, makedirs
import sys
from ..models.database_models import ItemQueue
from ..models.database_models import Base

class ItemsQueueClient:
    
    def __init__(self, db: str):
        try:
            if getattr(sys, "frozen", False):
                base_path = path.dirname(sys.executable) 
            else:
                base_path = path.join(path.dirname(__file__), "..", "..", "..", "..")
            BASE_DIR = path.abspath(path.join(base_path, "storage", ".databases"))
            makedirs(BASE_DIR, exist_ok=True)
            url = f"sqlite:///{BASE_DIR}/{db}.db"
            self.engine = create_engine(url, echo=True, connect_args={"timeout": 30})
            self.session_construct = sessionmaker(bind=self.engine)
            Base.metadata.create_all(self.engine)
        except Exception as error:
            raise Exception(f"Error on (ItemsQueueClient) component on (__init__) method: {error}")
    
    def create(self,
        order_ref: str,
        sku: str,
        quantity: str,
        center: str,
        deposit: str,
        guarantee: str,
        over: str,
        unit_value: str,
        total_value: str,
        is_parent_item: str
    ) -> None:
        try:
            session = self.session_construct()
            to_create = ItemQueue(
                order_ref=order_ref,
                sku=sku,
                quantity=quantity,
                center=center,
                deposit=deposit,
                guarantee=guarantee,
                over=over,
                unit_value=unit_value,
                total_value=total_value,
                is_parent_item=is_parent_item
            )
            session.add(to_create)
            session.commit()
            session.refresh(to_create)
            session.close()
        except Exception as error:
            raise Exception(f"Error on (ItemsQueueClient) component on (create) method: {error}")
    
    def read(self, order: str) -> list[ItemQueue]:
        try:
            session = self.session_construct()
            return session.query(ItemQueue).filter(ItemQueue.order_ref == order).all()
        except Exception as error:
            raise Exception(f"Error on (ItemsQueueClient) component on (read) method: {error}")
    
    def delete(self, order: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(ItemQueue).filter(ItemQueue.order_ref == order).all()
            for delete_element in to_delete:
                session.delete(delete_element)
            session.commit()
        except Exception as error:
            raise Exception(f"Error on (ItemsQueueClient) component on (delete) method: {error}")
