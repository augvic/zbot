from src.io.api.login import Login
from src.io.api.main import Main
from src.io.api.modules_list import ModulesList
from src.io.api.permissions import Permissions
from src.io.api.session_modules import SessionModules
from src.io.api.users import Users
from src.io.api.session_user import SessionUser
from src.io.api.registrations_rpa import RegistrationsRpa
from src.io.api.registrations import Registrations
from .tasks import Tasks

class IO:
    
    def __init__(self, tasks: Tasks) -> None:
        self.tasks = tasks
        self.login_route = Login(
            validate_login_task=self.tasks.validate_login_task,
            verify_if_user_is_in_session_task=self.tasks.verify_if_user_is_in_session_task,
            logout_task=self.tasks.logout_task,
            process_request_task=self.tasks.process_request_task
        )
        self.main_route = Main(
            render_template_task=self.tasks.render_template_task
        )
        self.modules_list_route = ModulesList(
            verify_if_have_access_task=self.tasks.verify_if_have_access_task,
            get_modules_list_task=self.tasks.get_modules_list_task,
            create_module_task=self.tasks.create_module_task,
            delete_module_task=self.tasks.delete_module_task,
            process_request_task=self.tasks.process_request_task,
            verify_if_user_is_in_session_task=self.tasks.verify_if_user_is_in_session_task,
        )
        self.permissions_route = Permissions(
            verify_if_have_access_task=self.tasks.verify_if_have_access_task,
            get_permissions_task=self.tasks.get_permissions_task,
            create_permission_task=self.tasks.create_permission_task,
            delete_permission_task=self.tasks.delete_permission_task,
            verify_if_user_is_in_session_task=self.tasks.verify_if_user_is_in_session_task,
        )
        self.session_modules_route = SessionModules(
            verify_if_user_is_in_session_task=self.tasks.verify_if_user_is_in_session_task,
            get_session_modules_task=self.tasks.get_session_modules_task
        )
        self.users_route = Users(
            verify_if_have_access_task=self.tasks.verify_if_have_access_task,
            get_users_task=self.tasks.get_user_task,
            create_user_task=self.tasks.create_user_task,
            delete_user_task=self.tasks.delete_user_task,
            update_user_task=self.tasks.update_user_task,
            process_request_task=self.tasks.process_request_task,
            verify_if_user_is_in_session_task=self.tasks.verify_if_user_is_in_session_task,
        )
        self.session_user_route = SessionUser(
            verify_if_user_is_in_session_task=self.tasks.verify_if_user_is_in_session_task,
            get_session_user_task=self.tasks.get_session_user_task
        )
        self.registrations_rpa_route = RegistrationsRpa(
            verify_if_have_acess_task=self.tasks.verify_if_have_access_task,
            run_registrations_rpa_task=self.tasks.run_registrations_rpa_task,
            verify_if_user_is_in_session_task=self.tasks.verify_if_user_is_in_session_task,
        )
        self.registrations_route = Registrations(
            verify_if_have_access_task=self.tasks.verify_if_have_access_task,
            create_registration_task=self.tasks.create_registration_task,
            update_registration_task=self.tasks.update_registration_task,
            get_registration_task=self.tasks.get_registration_task,
            delete_registration_task=self.tasks.delete_registration_task,
            process_request_task=self.tasks.process_request_task,
            verify_if_user_is_in_session_task=self.tasks.verify_if_user_is_in_session_task,
        )
