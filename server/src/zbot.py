from .engines.engines import Engines
from .tasks.tasks import Tasks
from .threads.threads import Threads
from .cli.cli import Cli
from .api.api import Api

class zBot:
    
    def __init__(self) -> None:
        self.engines = Engines()
        self.tasks = Tasks(self.engines)
        self.threads = Threads(self.engines)
        self.api = Api(self.engines, self.tasks, self.threads)
        self.cli = Cli(self.tasks, self.engines, self.threads)
    
    def main(self) -> None:
        self.engines.thread_engine.start_single_thread(self.api.main)
        self.cli.main()
