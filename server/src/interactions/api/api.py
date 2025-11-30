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
from src.tasks.verify_if_user_is_in_session.verify_if_user_is_in_session import VerifyIfUserIsInSession
from src.tasks.get_federal_revenue_data.federal_revenue_data import GetFederalRevenueData
from src.tasks.get_financial_data.get_financial_data import GetFinancialData
from src.tasks.get_modules_list.get_modules_list import GetModulesList
from src.tasks.create_order.create_order import CreateOrder
from src.tasks.create_registration.create_registration import CreateRegistration
from src.tasks.delete_registration.delete_registration import DeleteRegistration
from src.tasks.update_registration.update_registration import UpdateRegistration
from src.tasks.get_registration.get_registration import GetRegistration
from src.tasks.run_registrations_rpa.run_registrations_rpa import RunRegistrationsRpa
from src.tasks.register_route import RegisterRoute
from src.tasks.internal.wsgi_application_actions import RunWsgiApplication

from .routes.login import Login
from .routes.main import Main
from .routes.modules_list import ModulesList
from .routes.permissions import Permissions
from .routes.registrations_rpa import RegistrationsRpa
from .routes.registrations import Registrations
from .routes.session_modules import SessionModules
from .routes.session_user import SessionUser
from .routes.users import Users

class Api:
    
    def __init__(self,
        register_route_task: RegisterRoute,
        validate_login_task: ValidateLogin,
        verify_if_user_is_in_session_task: VerifyIfUserIsInSession,
        logout_task: Logout,
        process_request_task: ProcessRequest,
        render_template_task: RenderTemplate,
        verify_if_have_access_task: VerifyIfHaveAccess,
        get_modules_list_task: GetModulesList,
        create_module_task: CreateModule,
        delete_module_task: DeleteModule,
        get_permissions_task: GetPermissions,
        create_permission_task: CreatePermission,
        delete_permission_task: DeletePermission,
        get_session_modules_task: GetSessionModules,
        get_user_task: GetUser,
        create_user_task: CreateUser,
        delete_user_task: DeleteUser,
        update_user_task: UpdateUser,
        get_session_user_task: GetSessionUser,
        run_registrations_rpa_task: RunRegistrationsRpa,
        create_registration_task: CreateRegistration,
        update_registration_task: UpdateRegistration,
        get_registration_task: GetRegistration,
        delete_registration_task: DeleteRegistration,
        run_wsgi_application_task: RunWsgiApplication
    ) -> None:
        self.run_wsgi_application_task = run_wsgi_application_task
        self.login_route = Login(
            validate_login_task=validate_login_task,
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
            get_modules_list_task=get_modules_list_task,
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
            run_registrations_rpa_task=run_registrations_rpa_task,
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
    
    def main(self) -> None:
        self.run_wsgi_application_task.main()
