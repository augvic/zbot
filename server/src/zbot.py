from .engines.engines import Engines

class zBot:
    
    def __init__(self) -> None:
        self.engines = Engines()
        self.tasks = None
        self.api = None
        self.cli = None
    
    def main(self) -> None:
        pass
