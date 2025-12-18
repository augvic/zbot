from .clients.go_deep_browser_client import GoDeepBrowserClient
from .clients.order_client import OrderClient
from .clients.go_deep_pe_session_client import GoDeepPeSessionClient

class GoDeepEngine:
    
    def __init__(self) -> None:
        self.go_deep_browser = GoDeepBrowserClient()
        self.order_interactor = OrderClient(self.go_deep_browser)
        self.go_deep_pe_session_client = GoDeepPeSessionClient()
