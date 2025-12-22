from .list.registrations_rpa_thread import RegistrationsRpa
from .list.update_orders_pme_thread import UpdateOrdersPmeThread

from src.engines.engines import Engines

class Threads:
    
    def __init__(self, engines: Engines) -> None:
        self.registrations_rpa_thread = RegistrationsRpa(engines)
        self.update_orders_pme_thread = UpdateOrdersPmeThread(engines)
