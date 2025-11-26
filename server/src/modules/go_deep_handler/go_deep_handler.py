from .clients.go_deep_browser import GoDeepBrowser
from .clients.order_interactor import OrderInteractor

class GoDeepHandler:
    
    def __init__(self) -> None:
        self.go_deep_browser = GoDeepBrowser()
        self.order_interactor = OrderInteractor(self.go_deep_browser)
