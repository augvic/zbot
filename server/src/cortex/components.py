from src.components.adapter.dataclass_serializer import DataclassSerializer
from src.components.adapter.sqla_serializer import SqlaSerializer
from src.components.file_system.log_system import LogSystem
from src.components.file_system.registrations_docs_handler import RegistrationsDocsHandler
from src.components.gear.application_thread import ApplicationThread
from src.components.gear.date_utility import DateUtility
from src.components.gear.time_utility import TimeUtility
from src.components.infra.database_clients.clients.comissions_queue_client import ComissionsQueueClient
from src.components.infra.database_clients.clients.items_queue_client import ItemsQueueClient
from src.components.infra.database_clients.clients.modules_client import ModulesClient
from src.components.infra.database_clients.clients.nceas_client import NceasClient
from src.components.infra.database_clients.clients.orders_queue_client import OrdersQueueClient
from src.components.infra.database_clients.clients.partners_queue_client import PartnersQueueClient
from src.components.infra.database_clients.clients.permissions_client import PermissionsClient
from src.components.infra.database_clients.clients.registrations_client import RegistrationsClient
from src.components.infra.database_clients.clients.state_registrations_client import StateRegistrationsClient
from src.components.infra.database_clients.clients.suframa_registrations_client import SuframaRegistrationsClient
from src.components.infra.database_clients.clients.users_client import UsersClient
from src.components.infra.database_clients.dummy_clients.permissions_client_dummy import PermissionsClientDummy
from src.components.infra.database_clients.dummy_clients.users_client_dummy import UsersClientDummy
from src.components.infra.go_deep_clients.clients.order_interactor import OrderInteractor
from src.components.infra.go_deep_clients.clients.registrations_interactor import RegistrationsInteractor
from src.components.infra.pos_fr_api.component import PositivoFederalRevenueApi
from src.components.infra.sap_clients.clients.financial_data_getter import FinancialDataGetter
from src.components.infra.sap_clients.clients.order_creator import OrderCreator
from src.components.infra.supplier_client.client import SupplierHandler
from src.components.infra.request_manager import RequestManager
from src.components.infra.session_manager import SessionManager
from src.components.infra.socketio_application import SocketIoApplication
from src.components.infra.template_manager import TemplateManager
from src.components.infra.wsgi_application import WsgiApplication
from src.components.logic.credit_analyzer.component import CreditAnalyzer
from src.components.logic.request_processor.component import RequestProcessor

class Components:
    
    def __init__(self) -> None:
        self.app = WsgiApplication()
        self.socketio = SocketIoApplication(self.app)
        self.template_manager = TemplateManager()
        self.dataclass_serializer = DataclassSerializer()
        self.sqla_serializer = SqlaSerializer()
        self.create_modules_log_system = LogSystem("admin/modules/create_module")
        self.delete_modules_log_system = LogSystem("admin/modules/delete_module")
        self.create_permission_log_system = LogSystem("admin/permission/create_permission")
        self.delete_permission_log_system = LogSystem("admin/permission/delete_permission")
        self.create_user_log_system = LogSystem("admin/user/create_user")
        self.delete_user_log_system = LogSystem("admin/user/delete_user")
        self.get_user_log_system = LogSystem("admin/user/get_user")
        self.update_user_log_system = LogSystem("admin/user/update_user")
        self.process_request_log_system = LogSystem("application/process_request")
        self.render_template_log_system = LogSystem("application/render_template")
        self.get_permissions_log_system = LogSystem("auth/get_permissions")
        self.get_session_modules_log_system = LogSystem("auth/get_session_modules")
        self.get_session_user_log_system = LogSystem("auth/get_session_user")
        self.logout_log_system = LogSystem("auth/logout")
        self.validate_login_log_system = LogSystem("auth/validate_login")
        self.verify_if_have_access_log_system = LogSystem("auth/verify_if_have_access")
        self.verify_if_user_is_in_session_log_system = LogSystem("auth/verify_if_user_is_in_session")
        self.get_federal_revenue_data_log_system = LogSystem("get_data/federal_revenue_data")
        self.get_financial_data_log_system = LogSystem("get_data/financial_data")
        self.get_modules_list_log_system = LogSystem("get_data/modules_list")
        self.create_order_log_system = LogSystem("orders/create_order")
        self.create_registration_log_system = LogSystem("registrations/create_registration")
        self.update_registration_log_system = LogSystem("registrations/update_registration")
        self.delete_registration_log_system = LogSystem("registrations/delete_registration")
        self.get_registration_log_system = LogSystem("registrations/get_registration")
        self.run_registrations_rpa_log_system = LogSystem("rpa/registrations")
        self.registrations_doc_handler = RegistrationsDocsHandler()
        self.application_thread = ApplicationThread()
        self.date_utility = DateUtility()
        self.time_utility = TimeUtility()
        self.comissions_queue_client = ComissionsQueueClient("prd")
        self.items_queue_client = ItemsQueueClient("prd")
        self.modules_client = ModulesClient("prd")
        self.nceas_client = NceasClient("prd")
        self.orders_queue_client = OrdersQueueClient("prd")
        self.partners_queue_client = PartnersQueueClient("prd")
        self.permissions_client = PermissionsClient("prd")
        self.registrations_client = RegistrationsClient("prd")
        self.state_registrations_client = StateRegistrationsClient("prd")
        self.suframa_registrations_client = SuframaRegistrationsClient("prd")
        self.users_client = UsersClient("prd")
        self.permissions_client_dummy = PermissionsClientDummy()
        self.users_client_dummy = UsersClientDummy()
        self.order_interactor = OrderInteractor()
        self.registrations_interactor = RegistrationsInteractor()
        self.federal_revenue_api = PositivoFederalRevenueApi()
        self.financial_data_getter = FinancialDataGetter()
        self.order_creator = OrderCreator()
        self.supplier_handler = SupplierHandler()
        self.request_manager = RequestManager()
        self.session_manager = SessionManager()
        self.credit_analyzer = CreditAnalyzer()
        self.request_processor = RequestProcessor()
