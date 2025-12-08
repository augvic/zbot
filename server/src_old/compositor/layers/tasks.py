from src.tasks.create_module.create_module import CreateModule
from src.tasks.delete_module.delete_module import DeleteModule
from src.tasks.create_permission.permission import CreatePermission
from src.tasks.delete_permission.delete_permission import DeletePermission
from src.tasks.create_user.user import CreateUser
from src.tasks.delete_user.delete_user import DeleteUser
from src.tasks.get_user.get_user import GetUser
from src.tasks.update_user.update_user import UpdateUser 
from src.tasks.process_request.process_request import ProcessRequest
from src.tasks.render_template.render_template import RenderTemplate
from src.tasks.get_permissions.get_permissions import GetPermissions
from src.tasks.get_session_modules.get_session_modules import GetSessionModules
from src.tasks.get_session_user.get_session_user import GetSessionUser
from src.tasks.logout.logout import Logout
from src.tasks.validate_login.validate_login import ValidateLogin
from src.tasks.verify_if_have_access.verify_if_have_access import VerifyIfHaveAccess
from tasks.verify_if_user_is_in_session_task import VerifyIfUserIsInSession
from src.tasks.get_federal_revenue_data.federal_revenue_data import GetFederalRevenueData
from src.tasks.get_financial_data.get_financial_data import GetFinancialData
from src.tasks.get_modules_list.get_modules_list import GetModulesList
from src.tasks.create_order.create_order import CreateOrder
from src.tasks.create_registration.create_registration import CreateRegistration
from src.tasks.delete_registration.delete_registration import DeleteRegistration
from src.tasks.update_registration.update_registration import UpdateRegistration
from src.tasks.get_registration.get_registration import GetRegistration
from src.tasks.run_registrations_rpa.run_registrations_rpa import RunRegistrationsRpa
from tasks.register_route_task import RegisterRoute
from src.tasks.internal.wsgi_application_actions import RunWsgiApplication
from tasks.convert_df_to_str_task import ConvertDfToStr
from src.tasks.internal.utilitites import DateTasks

from .modules import Modules

class Tasks:
    
    def __init__(self, modules: Modules) -> None:
        self.create_module_task = CreateModule(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            log_system=modules.create_module_log_system
        )
        self.delete_module_task = DeleteModule(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            log_system=modules.delete_module_log_system
        )
        self.create_permission_task = CreatePermission(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            log_system=modules.create_permission_log_system
        )
        self.delete_permission_task = DeletePermission(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            log_system=modules.delete_permission_log_system
        )
        self.create_user_task = CreateUser(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            log_system=modules.create_user_log_system
        )
        self.delete_user_task = DeleteUser(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            log_system=modules.delete_user_log_system
        )
        self.get_user_task = GetUser(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            serializer=modules.sqla_serializer,
            log_system=modules.get_user_log_system
        )
        self.update_user_task = UpdateUser(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            log_system=modules.update_user_log_system
        )
        self.process_request_task = ProcessRequest(
            request_processor=modules.request_processor,
            log_system=modules.process_request_log_system,
            request_manager=modules.request_manager,
            session_manager=modules.session_manager
        )
        self.render_template_task = RenderTemplate(
            template_renderer=modules.template_manager,
            log_system=modules.render_template_log_system,
            request_manager=modules.request_manager
        )
        self.get_permissions_task = GetPermissions(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            serializer=modules.sqla_serializer,
            log_system=modules.get_permissions_log_system
        )
        self.get_session_modules_task = GetSessionModules(
            session_manager=modules.session_manager,
            log_system=modules.get_session_modules_log_system
        )
        self.get_session_user_task = GetSessionUser(
            session_manager=modules.session_manager,
            log_system=modules.get_session_user_log_system
        )
        self.logout_task = Logout(
            session_manager=modules.session_manager,
            log_system=modules.logout_log_system,
            request_manager=modules.request_manager
        )
        self.validate_login_task = ValidateLogin(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            log_system=modules.validate_login_log_system
        )
        self.verify_if_have_access_task = VerifyIfHaveAccess(
            session_manager=modules.session_manager,
            log_system=modules.verify_if_have_access_log_system
        )
        self.verify_if_user_is_in_session_task = VerifyIfUserIsInSession(
            session_manager=modules.session_manager,
            log_system=modules.verify_if_user_is_in_session_log_system,
            request_manager=modules.request_manager
        )
        self.get_federal_revenue_data_task = GetFederalRevenueData(
            federal_revenue_data_driver=modules.federal_revenue_api,
            serializer=modules.dataclass_serializer,
            log_system=modules.get_federal_revenue_data_log_system,
            session_manager=modules.session_manager
        )
        self.get_financial_data_task = GetFinancialData(
            sap_handler=modules.sap_handler,
            serializer=modules.dataclass_serializer,
            log_system=modules.get_financial_data_log_system,
            session_manager=modules.session_manager
        )
        self.get_modules_list_task = GetModulesList(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            serializer=modules.sqla_serializer,
            log_system=modules.get_modules_list_log_system
        )
        self.create_order_task = CreateOrder(
            sap_handler=modules.sap_handler,
            log_system=modules.create_order_log_system,
            session_manager=modules.session_manager
        )
        self.run_registrations_rpa_task = RunRegistrationsRpa(
            time_utility=modules.time_utility,
            log_system=modules.run_registrations_rpa_log_system,
            session_manager=modules.session_manager,
            thread=modules.application_thread,
            date_utility=modules.date_utility,
            wsgi_application=modules.wsgi_application
        )
        self.create_registration_task = CreateRegistration(
            federal_revenue_api=modules.federal_revenue_api,
            database_handler=modules.database_handler,
            log_system=modules.create_registration_log_system,
            date_utility=modules.date_utility,
            docs_handler=modules.registrations_doc_handler,
            session_manager=modules.session_manager
        )
        self.update_registration_task = UpdateRegistration(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            log_system=modules.update_registration_log_system,
            date_utility=modules.date_utility
        )
        self.delete_registration_task = DeleteRegistration(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            log_system=modules.delete_registration_log_system
        )
        self.get_registration_task = GetRegistration(
            database_handler=modules.database_handler,
            session_manager=modules.session_manager,
            serializer=modules.sqla_serializer,
            log_system=modules.get_registration_log_system
        )
        self.register_route_task = RegisterRoute(
            wsgi_application=modules.wsgi_application
        )
        self.run_wsgi_application = RunWsgiApplication(
            wsgi_application=modules.wsgi_application
        )
        self.convert_df_to_str_task = ConvertDfToStr(
            dataframe_handler=modules.dataframe_handler
        )
        self.date_tasks = DateTasks(
            date_utility=modules.date_utility
        )
