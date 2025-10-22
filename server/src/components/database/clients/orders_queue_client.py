from ..models import OrderQueue
from ..models import database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path
import sys

class OrdersQueueClient:
    
    def __init__(self, db: str):
        if getattr(sys, "frozen", False):
            base_path = path.dirname(sys.executable) 
        else:
            base_path = path.join(path.dirname(__file__), "..", "..", "..", "..")
        BASE_DIR = path.abspath(path.join(base_path, "storage", ".databases"))
        url = f"sqlite:///{BASE_DIR}/{db}.db"
        self.engine = create_engine(url, echo=True, connect_args={"timeout": 30})
        self.session_construct = sessionmaker(bind=self.engine)
        database.metadata.create_all(self.engine)
    
    def create(self,
        doc_type: str,
        organization: str,
        channel: str,
        office: str,
        team: str,
        order_name: str,
        issuer: str,
        receiver: str,
        payment_condition: str,
        incoterm: str,
        reason: str,
        table: str,
        expedition: str,
        payment_way: str,
        additional_data: str
    ) -> None:
        session = self.session_construct()
        to_create_index = 1
        while True:
            id_exists = session.query(OrderQueue).filter(OrderQueue.order == f"TC{to_create_index}").first()
            if id_exists:
                to_create_index += 1
            else:
                break
        to_create = OrderQueue(
            order=f"TC{to_create_index}",
            doc_type=doc_type,
            organization=organization,
            channel=channel,
            office=office,
            team=team,
            order_name=order_name,
            issuer=issuer,
            receiver=receiver,
            payment_condition=payment_condition,
            incoterm=incoterm,
            reason=reason,
            table=table,
            expedition=expedition,
            payment_way=payment_way,
            additional_data=additional_data
        )
        session.add(to_create)
        session.commit()
        session.refresh(to_create)
        session.close()
    
    def read(self, order: str) -> OrderQueue | None:
        session = self.session_construct()
        return session.query(OrderQueue).filter(OrderQueue.order == order).first()
    
    def read_all(self) -> list[OrderQueue]:
        session = self.session_construct()
        return session.query(OrderQueue).all()
    
    def update(self,
        order: str,
        doc_type: str = "",
        organization: str = "",
        channel: str = "",
        office: str = "",
        team: str = "",
        order_name: str = "",
        issuer: str = "",
        receiver: str = "",
        payment_condition: str = "",
        incoterm: str = "",
        reason: str = "",
        table: str = "",
        expedition: str = "",
        payment_way: str = "",
        additional_data: str = ""
    ) -> None:
        session = self.session_construct()
        to_update = session.query(OrderQueue).filter(OrderQueue.order == order).first()
        if to_update:
            if doc_type:
                to_update.doc_type = doc_type
            if organization:
                to_update.organization = organization
            if channel:
                to_update.channel = channel
            if office:
                to_update.office = office
            if team:
                to_update.team = team
            if order_name:
                to_update.order_name = order_name
            if issuer:
                to_update.issuer = issuer
            if receiver:
                to_update.receiver = receiver
            if payment_condition:
                to_update.payment_condition = payment_condition
            if incoterm:
                to_update.incoterm = incoterm
            if reason:
                to_update.reason = channel
            if table:
                to_update.table = table
            if expedition:
                to_update.expedition = expedition
            if payment_way:
                to_update.payment_way = payment_way
            if additional_data:
                to_update.additional_data = additional_data
            session.commit()
        session.close()
    
    def delete(self, order: str) -> None:
        session = self.session_construct()
        to_delete = session.query(OrderQueue).filter(OrderQueue.order == order).first()
        session.delete(to_delete)
        session.commit()
