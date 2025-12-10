from tasks.create_module_task import CreateModule
from tasks.delete_module_task import DeleteModule
from tasks.create_permission_task import CreatePermission
from tasks.delete_permission_task import DeletePermission
from tasks.create_user_task import CreateUser
from tasks.delete_user_task import DeleteUser
from tasks.get_user_task import GetUser
from tasks.update_user_task import UpdateUser 
from tasks.get_permissions_task import GetPermissions
from tasks.logout_task import Logout
from tasks.login_task import Login
from tasks.get_federal_revenue_data_task import GetFederalRevenueData
from tasks.get_financial_data_task import GetFinancialData
from tasks.get_modules_task import GetModules
from tasks.create_order_task import CreateOrder
from tasks.create_registration_task import CreateRegistration
from tasks.delete_registration_task import DeleteRegistration
from tasks.update_registration_task import UpdateRegistration
from tasks.get_registration_task import GetRegistration
from tasks.registrations_rpa_task import RegistrationsRpa
from src.engines.wsgi_application.wsgi_application import WsgiApplication

from .routes.login_route import Login
from .routes.main_route import Main
from .routes.modules_list import ModulesList
from .routes.permissions import Permissions
from .routes.registrations_rpa import RegistrationsRpa
from .routes.registrations import Registrations
from .routes.session_modules import SessionModules
from .routes.session_user import SessionUser
from .routes.users import Users

class Api:
    
    def __init__(self,
        login_task: Login,
        logout_task: Logout,
        get_modules: GetModules,
        create_module_task: CreateModule,
        delete_module_task: DeleteModule,
        get_permissions_task: GetPermissions,
        create_permission_task: CreatePermission,
        delete_permission_task: DeletePermission,
        get_user_task: GetUser,
        create_user_task: CreateUser,
        delete_user_task: DeleteUser,
        update_user_task: UpdateUser,
        registrations_rpa_task: RegistrationsRpa,
        create_registration_task: CreateRegistration,
        update_registration_task: UpdateRegistration,
        get_registration_task: GetRegistration,
        delete_registration_task: DeleteRegistration,
        wsgi_application: WsgiApplication
    ) -> None:
        self.login_route = Login(
            login_task=login_task,
            verify_if_user_is_in_session_task=verify_if_user_is_in_session_task,
            logout_task=logout_task,
            process_request_task=process_request_task,
            register_route_task=register_route_task
        )
        self.main_route = Main(
            render_template_task=render_template_task,
            register_route_task=register_route_task
        )
        self.modules_list_route = ModulesList(
            verify_if_have_access_task=verify_if_have_access_task,
            get_modules=get_modules,
            create_module_task=create_module_task,
            delete_module_task=delete_module_task,
            process_request_task=process_request_task,
            verify_if_user_is_in_session_task=verify_if_user_is_in_session_task,
            register_route_task=register_route_task
        )
        self.permissions_route = Permissions(
            verify_if_have_access_task=verify_if_have_access_task,
            get_permissions_task=get_permissions_task,
            create_permission_task=create_permission_task,
            delete_permission_task=delete_permission_task,
            verify_if_user_is_in_session_task=verify_if_user_is_in_session_task,
            register_route_task=register_route_task
        )
        self.session_modules_route = SessionModules(
            verify_if_user_is_in_session_task=verify_if_user_is_in_session_task,
            get_session_modules_task=get_session_modules_task,
            register_route_task=register_route_task
        )
        self.users_route = Users(
            verify_if_have_access_task=verify_if_have_access_task,
            get_user_task=get_user_task,
            create_user_task=create_user_task,
            delete_user_task=delete_user_task,
            update_user_task=update_user_task,
            process_request_task=process_request_task,
            verify_if_user_is_in_session_task=verify_if_user_is_in_session_task,
            register_route_task=register_route_task
        )
        self.session_user_route = SessionUser(
            verify_if_user_is_in_session_task=verify_if_user_is_in_session_task,
            get_session_user_task=get_session_user_task,
            register_route_task=register_route_task
        )
        self.registrations_rpa_route = RegistrationsRpa(
            verify_if_have_acess_task=verify_if_have_access_task,
            registrations_rpa_task=registrations_rpa_task,
            verify_if_user_is_in_session_task=verify_if_user_is_in_session_task,
            register_route_task=register_route_task
        )
        self.registrations_route = Registrations(
            verify_if_have_access_task=verify_if_have_access_task,
            create_registration_task=create_registration_task,
            update_registration_task=update_registration_task,
            get_registration_task=get_registration_task,
            delete_registration_task=delete_registration_task,
            process_request_task=process_request_task,
            verify_if_user_is_in_session_task=verify_if_user_is_in_session_task,
            register_route_task=register_route_task
        )
        self.wsgi_application = wsgi_application
    
    def main(self) -> None:
        self.wsgi_application.run()
