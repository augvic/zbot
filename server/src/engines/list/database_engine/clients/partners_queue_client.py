from ..models.database_models import PartnerQueue

from sqlalchemy.orm import sessionmaker

class PartnersQueueClient:
    
    def __init__(self, session_construct: sessionmaker):
        self.session_construct = session_construct
    
    def create(self,
        order_ref: str,
        key: str,
        code: str
    ) -> None:
        try:
            session = self.session_construct()
            to_create = PartnerQueue(
                order_ref=order_ref,
                key=key,
                code=code,
            )
            session.add(to_create)
            session.commit()
            session.refresh(to_create)
            session.close()
        except Exception as error:
            raise Exception(f"❌ Error in (PartnersQueueClient) in (create) method: {error}")
    
    def read(self, order: str) -> list[PartnerQueue]:
        try:
            session = self.session_construct()
            return session.query(PartnerQueue).filter(PartnerQueue.order_ref == order).all()
        except Exception as error:
            raise Exception(f"❌ Error in (PartnersQueueClient) in (read) method: {error}")
    
    def delete(self, order: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(PartnerQueue).filter(PartnerQueue.order_ref == order).all()
            for delete_element in to_delete:
                session.delete(delete_element)
            session.commit()
        except Exception as error:
            raise Exception(f"❌ Error in (PartnersQueueClient) in (delete) method: {error}")
