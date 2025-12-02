from src.modules.model_serializer import DataclassSerializer
from src.modules.sqla_serializer import SqlaSerializer
from src.modules.log_system import LogSystem
from src.modules.registrations_docs_handler import RegistrationsDocsHandler
from src.modules.application_thread import ApplicationThread
from src.modules.date_utility import DateUtility
from src.modules.time_utility import TimeUtility
from src.modules.database_handler.database_handler import DatabaseHandler
from src.modules.go_deep_handler.go_deep_handler import GoDeepHandler
from src.modules.positivo_federal_revenue_api.positivo_federal_revenue_api import PositivoFederalRevenueApi
from src.modules.sap_handler.sap_handler import SapHandler
from src.modules.supplier_handler.supplier_handler import SupplierHandler
from src.modules.request_manager import RequestManager
from src.modules.session_manager import SessionManager
from src.modules.template_manager import TemplateManager
from modules.wsgi_application.wsgi_application import WsgiApplication
from src.modules.credit_analyzer.credit_analyzer import CreditAnalyzer
from src.modules.request_processor.request_processor import RequestProcessor
from src.modules.dataframe_handler import DataFrameHandler

class Modules:
    
    def __init__(self) -> None:
        self.wsgi_application = WsgiApplication()
        self.template_manager = TemplateManager()
        self.dataclass_serializer = DataclassSerializer()
        self.sqla_serializer = SqlaSerializer()
        self.create_module_log_system = LogSystem("create_module")
        self.delete_module_log_system = LogSystem("delete_module")
        self.create_permission_log_system = LogSystem("create_permission")
        self.delete_permission_log_system = LogSystem("delete_permission")
        self.create_user_log_system = LogSystem("create_user")
        self.delete_user_log_system = LogSystem("delete_user")
        self.get_user_log_system = LogSystem("get_user")
        self.update_user_log_system = LogSystem("update_user")
        self.process_request_log_system = LogSystem("process_request")
        self.render_template_log_system = LogSystem("render_template")
        self.get_permissions_log_system = LogSystem("get_permissions")
        self.get_session_modules_log_system = LogSystem("get_session_modules")
        self.get_session_user_log_system = LogSystem("get_session_user")
        self.logout_log_system = LogSystem("logout")
        self.validate_login_log_system = LogSystem("validate_login")
        self.verify_if_have_access_log_system = LogSystem("verify_if_have_access")
        self.verify_if_user_is_in_session_log_system = LogSystem("verify_if_user_is_in_session")
        self.get_federal_revenue_data_log_system = LogSystem("federal_revenue_data")
        self.get_financial_data_log_system = LogSystem("financial_data")
        self.get_modules_list_log_system = LogSystem("modules_list")
        self.create_order_log_system = LogSystem("create_order")
        self.create_registration_log_system = LogSystem("create_registration")
        self.update_registration_log_system = LogSystem("update_registration")
        self.delete_registration_log_system = LogSystem("delete_registration")
        self.get_registration_log_system = LogSystem("get_registration")
        self.run_registrations_rpa_log_system = LogSystem("rpa_registrations")
        self.registrations_doc_handler = RegistrationsDocsHandler()
        self.application_thread = ApplicationThread()
        self.date_utility = DateUtility()
        self.time_utility = TimeUtility()
        self.database_handler = DatabaseHandler("prd")
        self.go_deep_handler = GoDeepHandler()
        self.federal_revenue_api = PositivoFederalRevenueApi()
        self.sap_handler = SapHandler()
        self.supplier_handler = SupplierHandler()
        self.request_manager = RequestManager()
        self.session_manager = SessionManager()
        self.credit_analyzer = CreditAnalyzer()
        self.request_processor = RequestProcessor()
        self.dataframe_handler = DataFrameHandler()
