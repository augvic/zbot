from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path, makedirs
import sys

from .models.database_models import Base
from .clients.comissions_queue_client import ComissionsQueueClient
from .clients.items_queue_client import ItemsQueueClient
from .clients.modules_client import ModulesClient
from .clients.nceas_client import NceasClient
from .clients.orders_queue_client import OrdersQueueClient
from .clients.partners_queue_client import PartnersQueueClient
from .clients.permissions_client import PermissionsClient
from .clients.registrations_client import RegistrationsClient
from .clients.state_registrations_client import StateRegistrationsClient
from .clients.suframa_registrations_client import SuframaRegistrationsClient
from .clients.users_client import UsersClient
from .dummy_clients.permissions_client_dummy import PermissionsClientDummy
from .dummy_clients.users_client_dummy import UsersClientDummy

class DatabaseEngine:
    
    def __init__(self, db: str) -> None:
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
        self.comissions_queue_client = ComissionsQueueClient(self.session_construct)
        self.items_queue_client = ItemsQueueClient(self.session_construct)
        self.modules_client = ModulesClient(self.session_construct)
        self.nceas_client = NceasClient(self.session_construct)
        self.orders_queue_client = OrdersQueueClient(self.session_construct)
        self.partners_queue_client = PartnersQueueClient(self.session_construct)
        self.permissions_client = PermissionsClient(self.session_construct)
        self.registrations_client = RegistrationsClient(self.session_construct)
        self.state_registrations_client = StateRegistrationsClient(self.session_construct)
        self.suframa_registrations_client = SuframaRegistrationsClient(self.session_construct)
        self.users_client = UsersClient(self.session_construct)
        self.permissions_client_dummy = PermissionsClientDummy()
        self.users_client_dummy = UsersClientDummy()
