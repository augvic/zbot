from .list.database_engine.database_engine import DatabaseEngine
from .list.federal_revenue_api_engine.federal_revenue_api_engine import FederalRevenueApiEngine
from .list.go_deep_engine.go_deep_engine import GoDeepEngine
from .list.sap_engine.sap_engine import SapEngine
from .list.supplier_engine.supplier_engine import SupplierEngine
from .list.wsgi_engine.wsgi_engine import WsgiEngine
from .list.cli_session_manager_engine import CliSessionManagerEngine
from .list.credit_analyzer_engine import CreditAnalyzerEngine
from .list.dataframe_engine import DataFrameEngine
from .list.date_engine import DateEngine
from .list.environ_engine import EnvironEngine
from .list.event_bus_engine import EventBusEngine
from .list.log_engine import LogEngine
from .list.registrations_docs_engine import RegistrationsDocsEngine
from .list.serializer_engine import SerializerEngine
from .list.thread_engine import ThreadEngine
from .list.time_engine import TimeEngine

class Engines:
    
    def __init__(self) -> None:
        self.database_engine = DatabaseEngine("prd")
        self.federal_revenue_api_engine = FederalRevenueApiEngine()
        self.go_deep_engine = GoDeepEngine()
        self.sap_engine = SapEngine()
        self.supplier_engine = SupplierEngine()
        self.wsgi_engine = WsgiEngine()
        self.cli_session_engine = CliSessionManagerEngine()
        self.credit_analyzer_engine = CreditAnalyzerEngine()
        self.dataframe_engine = DataFrameEngine()
        self.date_engine = DateEngine()
        self.environ_engine = EnvironEngine()
        self.event_bus_engine = EventBusEngine()
        self.log_engine = LogEngine()
        self.registrations_docs_engine = RegistrationsDocsEngine()
        self.serializer_engine = SerializerEngine()
        self.thread_engine = ThreadEngine()
        self.time_engine = TimeEngine()
