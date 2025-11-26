from src.tasks.admin.module.create_module.task import CreateModule
from src.tasks.admin.module.delete_module.task import DeleteModule
from src.tasks.admin.permission.create_permission.task import CreatePermission
from src.tasks.admin.permission.delete_permission.task import DeletePermission
from src.tasks.admin.user.create_user.task import CreateUser
from src.tasks.admin.user.delete_user.task import DeleteUser
from src.tasks.admin.user.get_user.task import GetUser
from src.tasks.admin.user.update_user.task import UpdateUser 
from src.tasks.application.process_request.task import ProcessRequest
from src.tasks.application.get_web_app_task import RenderTemplate
from src.tasks.auth.get_permissions.task import GetPermissions
from src.tasks.auth.get_session_modules.task import GetSessionModules
from src.tasks.auth.get_session_user.task import GetSessionUser
from src.tasks.auth.logout_task import Logout
from src.tasks.auth.validate_login_task import ValidateLogin
from src.tasks.auth.verify_if_have_access.task import VerifyIfHaveAccess
from src.tasks.auth.verify_if_user_is_in_session_task import VerifyIfUserIsInSession
from src.tasks.get_data.get_federal_revenue_data.task import GetFederalRevenueData
from src.tasks.get_data.get_financial_data.task import GetFinancialData
from src.tasks.get_data.get_modules_list.task import GetModulesList
from src.tasks.orders.create_order.task import CreateOrder
from src.tasks.registrations.create_registration.task import CreateRegistration
from src.tasks.registrations.delete_registration.task import DeleteRegistration
from src.tasks.registrations.update_registration.task import UpdateRegistration
from src.tasks.registrations.get_registration.task import GetRegistration
from src.tasks.rpa.run_registrations_rpa.task import RunRegistrationsRpa
from .components import Components

class Tasks:
    
    def __init__(self, components: Components) -> None:
        self.components = components
        self.create_module_task = CreateModule(
            modules_client=self.components.modules_client,
            session_manager=self.components.session_manager,
            log_system=self.components.create_modules_log_system
        )
        self.delete_module_task = DeleteModule(
            modules_client=self.components.modules_client,
            permisssions_client=self.components.permissions_client,
            session_manager=self.components.session_manager,
            log_system=self.components.delete_modules_log_system
        )
        self.create_permission_task = CreatePermission(
            users_client=self.components.users_client,
            permissions_client=self.components.permissions_client,
            session_manager=self.components.session_manager,
            log_system=self.components.create_permission_log_system
        )
        self.delete_permission_task = DeletePermission(
            users_client=self.components.users_client,
            permissions_client=self.components.permissions_client,
            session_manager=self.components.session_manager,
            log_system=self.components.delete_permission_log_system
        )
        self.create_user_task = CreateUser(
            users_client=self.components.users_client,
            session_manager=self.components.session_manager,
            log_system=self.components.create_user_log_system
        )
        self.delete_user_task = DeleteUser(
            users_client=self.components.users_client,
            session_manager=self.components.session_manager,
            log_system=self.components.delete_user_log_system
        )
        self.get_user_task = GetUser(
            users_client=self.components.users_client,
            session_manager=self.components.session_manager,
            serializer=self.components.sqla_serializer,
            log_system=self.components.get_user_log_system
        )
        self.update_user_task = UpdateUser(
            users_client=self.components.users_client,
            session_manager=self.components.session_manager,
            log_system=self.components.update_user_log_system
        )
        self.process_request_task = ProcessRequest(
            request_processor=self.components.request_processor,
            log_system=self.components.process_request_log_system,
            request_manager=self.components.request_manager,
            session_manager=self.components.session_manager
        )
        self.render_template_task = RenderTemplate(
            template_renderer=self.components.template_manager,
            log_system=self.components.render_template_log_system,
            request_manager=self.components.request_manager
        )
        self.get_permissions_task = GetPermissions(
            permissions_client=self.components.permissions_client,
            session_manager=self.components.session_manager,
            serializer=self.components.sqla_serializer,
            log_system=self.components.get_permissions_log_system
        )
        self.get_session_modules_task = GetSessionModules(
            session_manager=self.components.session_manager,
            log_system=self.components.get_session_modules_log_system
        )
        self.get_session_user_task = GetSessionUser(
            session_manager=self.components.session_manager,
            log_system=self.components.get_session_user_log_system
        )
        self.logout_task = Logout(
            session_manager=self.components.session_manager,
            log_system=self.components.logout_log_system,
            request_manager=self.components.request_manager
        )
        self.validate_login_task = ValidateLogin(
            users_client=self.components.users_client,
            permissions_client=self.components.permissions_client,
            modules_client=self.components.modules_client,
            session_manager=self.components.session_manager,
            log_system=self.components.validate_login_log_system
        )
        self.verify_if_have_access_task = VerifyIfHaveAccess(
            session_manager=self.components.session_manager,
            log_system=self.components.verify_if_have_access_log_system
        )
        self.verify_if_user_is_in_session_task = VerifyIfUserIsInSession(
            session_manager=self.components.session_manager,
            log_system=self.components.verify_if_user_is_in_session_log_system,
            request_manager=self.components.request_manager
        )
        self.get_federal_revenue_data_task = GetFederalRevenueData(
            federal_revenue_data_driver=self.components.federal_revenue_api,
            serializer=self.components.dataclass_serializer,
            log_system=self.components.get_federal_revenue_data_log_system,
            session_manager=self.components.session_manager
        )
        self.get_financial_data_task = GetFinancialData(
            financial_data_driver=self.components.financial_data_getter,
            serializer=self.components.dataclass_serializer,
            log_system=self.components.get_financial_data_log_system,
            session_manager=self.components.session_manager
        )
        self.get_modules_list_task = GetModulesList(
            modules_client=self.components.modules_client,
            session_manager=self.components.session_manager,
            serializer=self.components.sqla_serializer,
            log_system=self.components.get_modules_list_log_system
        )
        self.create_order_task = CreateOrder(
            order_creator=self.components.order_creator,
            log_system=self.components.create_order_log_system,
            session_manager=self.components.session_manager
        )
        self.run_registrations_rpa_task = RunRegistrationsRpa(
            time_utility=self.components.time_utility,
            log_system=self.components.run_registrations_rpa_log_system,
            session_manager=self.components.session_manager,
            thread=self.components.application_thread,
            date_utility=self.components.date_utility,
            socketio=self.components.socketio
        )
        self.create_registration_task = CreateRegistration(
            federal_revenue_api=self.components.federal_revenue_api,
            registrations_client=self.components.registrations_client,
            state_registrations_client=self.components.state_registrations_client,
            suframa_registrations_client=self.components.suframa_registrations_client,
            nceas_client=self.components.nceas_client,
            log_system=self.components.create_registration_log_system,
            date_utility=self.components.date_utility,
            docs_handler=self.components.registrations_doc_handler,
            session_manager=self.components.session_manager
        )
        self.update_registration_task = UpdateRegistration(
            registrations_client=self.components.registrations_client,
            session_manager=self.components.session_manager,
            log_system=self.components.update_registration_log_system,
            date_utility=self.components.date_utility
        )
        self.delete_registration_task = DeleteRegistration(
            registrations_client=self.components.registrations_client,
            session_manager=self.components.session_manager,
            log_system=self.components.delete_registration_log_system
        )
        self.get_registration_task = GetRegistration(
            registrations_client=self.components.registrations_client,
            session_manager=self.components.session_manager,
            serializer=self.components.sqla_serializer,
            log_system=self.components.get_registration_log_system
        )
