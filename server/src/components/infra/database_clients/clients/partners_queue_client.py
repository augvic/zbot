from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path, makedirs
import sys
from ..models.database_models import PartnerQueue
from ..models.database_models import Base

class PartnersQueueClient:
    
    def __init__(self, db: str):
        try:
            if getattr(sys, "frozen", False):
                base_path = path.dirname(sys.executable) 
            else:
                base_path = path.join(path.dirname(__file__), "..", "..", "..", "..", "..")
            BASE_DIR = path.abspath(path.join(base_path, "storage", ".databases"))
            makedirs(BASE_DIR, exist_ok=True)
            url = f"sqlite:///{BASE_DIR}/{db}.db"
            self.engine = create_engine(url, echo=True, connect_args={"timeout": 30})
            self.session_construct = sessionmaker(bind=self.engine)
            Base.metadata.create_all(self.engine)
        except Exception as error:
            raise Exception(f"Error in (PartnersQueueClient) component in (__init__) method: {error}.")
    
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
            raise Exception(f"Error in (PartnersQueueClient) component in (create) method: {error}.")
    
    def read(self, order: str) -> list[PartnerQueue]:
        try:
            session = self.session_construct()
            return session.query(PartnerQueue).filter(PartnerQueue.order_ref == order).all()
        except Exception as error:
            raise Exception(f"Error in (PartnersQueueClient) component in (read) method: {error}.")
    
    def delete(self, order: str) -> None:
        try:
            session = self.session_construct()
            to_delete = session.query(PartnerQueue).filter(PartnerQueue.order_ref == order).all()
            for delete_element in to_delete:
                session.delete(delete_element)
            session.commit()
        except Exception as error:
            raise Exception(f"Error in (PartnersQueueClient) component in (delete) method: {error}.")
