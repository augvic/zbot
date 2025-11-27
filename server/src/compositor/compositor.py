from .layers.modules import Modules
from .layers.tasks import Tasks
from .layers.interactions import Interactions

class Compositor:
    
    def __init__(self) -> None:
        self.modules = Modules()
        self.tasks = Tasks(self.modules)
        self.interactions = Interactions(self.tasks)
