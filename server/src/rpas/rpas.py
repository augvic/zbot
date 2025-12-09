from .list.registrations_rpa import RegistrationsRpa

from src.engines.engines import Engines

class Rpas:
    
    def __init__(self, engines: Engines) -> None:
        self.registrations_rpa = RegistrationsRpa(engines)
