from ..models.database_models import ItemQueue

from sqlalchemy.orm import sessionmaker

class ItemsQueueClient:
    
    def __init__(self, session_construct: sessionmaker):
        self.session_construct = session_construct
    
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
            raise Exception(f"❌ Error in (ItemsQueueClient) engine in (create) method: {error}")
    
    def read(self, order: str) -> list[ItemQueue]:
        try:
            session = self.session_construct()
            return session.query(ItemQueue).filter(ItemQueue.order_ref == order).all()
        except Exception as error:
            raise Exception(f"❌ Error in (ItemsQueueClient) engine in (read) method: {error}")
    
    def delete(self, order: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(ItemQueue).filter(ItemQueue.order_ref == order).all()
            for delete_element in to_delete:
                session.delete(delete_element)
            session.commit()
        except Exception as error:
            raise Exception(f"❌ Error in (ItemsQueueClient) engine in (delete) method: {error}")
