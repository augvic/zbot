from src.io.api.login import Login
from src.io.api.main import Main
from src.io.api.modules_list import ModulesList
from src.io.api.permissions import Permissions
from src.io.api.session_modules import SessionModules
from src.io.api.users import Users
from src.io.api.session_user import SessionUser
from src.io.api.registrations_rpa import RegistrationsRpa
from src.io.api.registrations import Registrations
from src.tasks.admin.module.create_module.task import CreateModule
from src.tasks.admin.module.delete_module.task import DeleteModule
from src.tasks.admin.permission.create_permission.task import CreatePermission
from src.tasks.admin.permission.delete_permission.task import DeletePermission
from src.tasks.admin.user.create_user.task import CreateUser
from src.tasks.admin.user.delete_user.task import DeleteUser
from src.tasks.admin.user.get_user.task import GetUser
from src.tasks.admin.user.update_user.task import UpdateUser 
from src.tasks.application.process_request.task import ProcessRequest
from src.tasks.application.render_template.task import RenderTemplate
from src.tasks.auth.get_permissions.task import GetPermissions
from src.tasks.auth.get_session_modules.task import GetSessionModules
from src.tasks.auth.get_session_user.task import GetSessionUser
from src.tasks.auth.logout.task import Logout
from src.tasks.auth.validate_login.task import ValidateLogin
from src.tasks.auth.verify_if_have_access.task import VerifyIfHaveAccess
from src.tasks.auth.verify_if_user_is_in_session.task import VerifyIfUserIsInSession
from src.tasks.get_data.get_federal_revenue_data.task import GetFederalRevenueData
from src.tasks.get_data.get_financial_data.task import GetFinancialData
from src.tasks.get_data.get_modules_list.task import GetModulesList
from src.tasks.post_data.create_order.task import CreateOrder
from src.tasks.post_data.include_new_registration.task import IncludeNewRegistration
from src.tasks.rpa.run_registrations_rpa.task import RunRegistrationsRpa
from src.tasks.application.route_registry import RouteRegistryTask
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

class CompositionRoot:
    
    def __init__(self) -> None:
        self._init_components()
        self._init_tasks()
        self._init_io()
    
    def _init_components(self) -> None:
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
        self.route_registry_log_system = LogSystem("application/route_registry")
        self.logout_log_system = LogSystem("auth/logout")
        self.validate_login_log_system = LogSystem("auth/validate_login")
        self.verify_if_have_access_log_system = LogSystem("auth/verify_if_have_access")
        self.verify_if_user_is_in_session_log_system = LogSystem("auth/verify_if_user_is_in_session")
        self.get_federal_revenue_data_log_system = LogSystem("get_data/federal_revenue_data")
        self.get_financial_data_log_system = LogSystem("get_data/financial_data")
        self.get_modules_list_log_system = LogSystem("get_data/modules_list")
        self.create_order_log_system = LogSystem("post_data/create_order")
        self.include_new_registration_log_system = LogSystem("post_data/include_new_registration")
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
    
    def _init_tasks(self) -> None:
        self.create_module_task = CreateModule(
            modules_client=self.modules_client,
            session_manager=self.session_manager,
            log_system=self.create_modules_log_system
        )
        self.delete_module_task = DeleteModule(
            modules_client=self.modules_client,
            permisssions_client=self.permissions_client,
            session_manager=self.session_manager,
            log_system=self.delete_modules_log_system
        )
        self.create_permission_task = CreatePermission(
            users_client=self.users_client,
            permissions_client=self.permissions_client,
            session_manager=self.session_manager,
            log_system=self.create_permission_log_system
        )
        self.delete_permission_task = DeletePermission(
            users_client=self.users_client,
            permissions_client=self.permissions_client,
            session_manager=self.session_manager,
            log_system=self.delete_permission_log_system
        )
        self.create_user_task = CreateUser(
            users_client=self.users_client,
            session_manager=self.session_manager,
            log_system=self.create_user_log_system
        )
        self.delete_user_task = DeleteUser(
            users_client=self.users_client,
            session_manager=self.session_manager,
            log_system=self.delete_user_log_system
        )
        self.get_user_task = GetUser(
            users_client=self.users_client,
            session_manager=self.session_manager,
            serializer=self.sqla_serializer,
            log_system=self.get_user_log_system
        )
        self.update_user_task = UpdateUser(
            users_client=self.users_client,
            session_manager=self.session_manager,
            log_system=self.update_user_log_system
        )
        self.process_request_task = ProcessRequest(
            request_processor=self.request_processor,
            log_system=self.process_request_log_system,
            request_manager=self.request_manager,
            session_manager=self.session_manager
        )
        self.render_template_task = RenderTemplate(
            template_renderer=self.template_manager,
            log_system=self.render_template_log_system,
            request_manager=self.request_manager
        )
        self.get_permissions_task = GetPermissions(
            permissions_client=self.permissions_client,
            session_manager=self.session_manager,
            serializer=self.sqla_serializer,
            log_system=self.get_permissions_log_system
        )
        self.get_session_modules_task = GetSessionModules(
            session_manager=self.session_manager,
            log_system=self.get_session_modules_log_system
        )
        self.get_session_user_task = GetSessionUser(
            session_manager=self.session_manager,
            log_system=self.get_session_user_log_system
        )
        self.logout_task = Logout(
            session_manager=self.session_manager,
            log_system=self.logout_log_system
        )
        self.validate_login_task = ValidateLogin(
            users_client=self.users_client,
            permissions_client=self.permissions_client,
            modules_client=self.modules_client,
            session_manager=self.session_manager,
            log_system=self.validate_login_log_system
        )
        self.verify_if_have_access_task = VerifyIfHaveAccess(
            session_manager=self.session_manager,
            log_system=self.verify_if_have_access_log_system
        )
        self.verify_if_user_is_in_session_task = VerifyIfUserIsInSession(
            session_manager=self.session_manager,
            log_system=self.verify_if_user_is_in_session_log_system,
            request_manager=self.request_manager
        )
        self.get_federal_revenue_data_task = GetFederalRevenueData(
            federal_revenue_data_driver=self.federal_revenue_api,
            serializer=self.dataclass_serializer,
            log_system=self.get_federal_revenue_data_log_system,
            session_manager=self.session_manager
        )
        self.get_financial_data_task = GetFinancialData(
            financial_data_driver=self.financial_data_getter,
            serializer=self.dataclass_serializer,
            log_system=self.get_financial_data_log_system,
            session_manager=self.session_manager
        )
        self.get_modules_list_task = GetModulesList(
            modules_client=self.modules_client,
            session_manager=self.session_manager,
            serializer=self.sqla_serializer,
            log_system=self.get_modules_list_log_system
        )
        self.create_order_task = CreateOrder(
            order_creator=self.order_creator,
            log_system=self.create_order_log_system,
            session_manager=self.session_manager
        )
        self.include_new_registration_task = IncludeNewRegistration(
            federal_revenue_api=self.federal_revenue_api,
            registrations_client=self.registrations_client,
            state_registrations_client=self.state_registrations_client,
            suframa_registrations_client=self.suframa_registrations_client,
            nceas_client=self.nceas_client,
            log_system=self.include_new_registration_log_system,
            date_utility=self.date_utility,
            docs_handler=self.registrations_doc_handler,
            session_manager=self.session_manager
        )
        self.run_registrations_rpa_task = RunRegistrationsRpa(
            time_utility=self.time_utility,
            log_system=self.run_registrations_rpa_log_system,
            session_manager=self.session_manager,
            thread=self.application_thread,
            date_utility=self.date_utility,
            socketio=self.socketio
        )
        self.route_registry_task = RouteRegistryTask(
            app_component=self.app,
            log_system=self.route_registry_log_system
        )
    
    def _init_io(self) -> None:
        Login(
            validate_login_task=self.validate_login_task,
            verify_if_user_is_in_session_task=self.verify_if_user_is_in_session_task,
            logout_task=self.logout_task,
            process_request_task=self.process_request_task,
            route_registry_task=self.route_registry_task
        ).init()
        Main(
            render_template_task=self.render_template_task,
            route_registry_task=self.route_registry_task
        ).init()
        ModulesList(
            verify_if_have_access_task=self.verify_if_have_access_task,
            get_modules_list_task=self.get_modules_list_task,
            create_module_task=self.create_module_task,
            delete_module_task=self.delete_module_task,
            process_request_task=self.process_request_task,
            route_registry_task=self.route_registry_task
        ).init()
        Permissions(
            verify_if_have_access_task=self.verify_if_have_access_task,
            get_permissions_task=self.get_permissions_task,
            create_permission_task=self.create_permission_task,
            delete_permission_task=self.delete_permission_task,
            route_registry_task=self.route_registry_task
        ).init()
        SessionModules(
            verify_if_user_is_in_session_task=self.verify_if_user_is_in_session_task,
            get_session_modules_task=self.get_session_modules_task,
            route_registry_task=self.route_registry_task
        ).init()
        Users(
            verify_if_have_access_task=self.verify_if_have_access_task,
            get_users_task=self.get_user_task,
            create_user_task=self.create_user_task,
            delete_user_task=self.delete_user_task,
            update_user_task=self.update_user_task,
            process_request_task=self.process_request_task,
            route_registry_task=self.route_registry_task
        ).init()
        SessionUser(
            verify_if_user_is_in_session_task=self.verify_if_user_is_in_session_task,
            get_session_user_task=self.get_session_user_task,
            route_registry_task=self.route_registry_task
        ).init()
        RegistrationsRpa(
            verify_if_have_acess_task=self.verify_if_have_access_task,
            run_registrations_rpa_task=self.run_registrations_rpa_task,
            route_registry_task=self.route_registry_task
        ).init()
        Registrations(
            verify_if_have_access_task=self.verify_if_have_access_task,
            include_new_registration_task=self.include_new_registration_task,
            process_request_task=self.process_request_task,
            route_registry_task=self.route_registry_task
        ).init()
    
    def run(self) -> None:
        self.socketio.run(self.app, host="127.0.0.1", debug=True)

CompositionRoot().run()
