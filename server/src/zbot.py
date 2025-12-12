from .engines.engines import Engines
from .tasks.tasks import Tasks
from .rpas.rpas import Rpas
from .cli.cli import Cli
from .api.api import Api

class zBot:
    
    def __init__(self) -> None:
        self.engines = Engines()
        self.tasks = Tasks(self.engines)
        self.rpas = Rpas(self.engines)
        self.api = Api(self.engines, self.tasks, self.rpas)
        self.cli = Cli(self.tasks, self.engines)
    
    def main(self) -> None:
        #self.engines.thread_engine.add_thread(self.api.main)
        self.engines.thread_engine.add_thread(self.cli.main)
        self.engines.thread_engine.start_threads()
