from src.interactions.api.api import Api
from interactions.cli.cli import Cli

from .tasks import Tasks

class Interactions:
    
    def __init__(self, tasks: Tasks) -> None:
        self.api = Api(
            register_route_task=tasks.register_route_task,
            validate_login_task=tasks.validate_login_task,
            verify_if_user_is_in_session_task=tasks.verify_if_user_is_in_session_task,
            logout_task=tasks.logout_task,
            process_request_task=tasks.process_request_task,
            render_template_task=tasks.render_template_task,
            verify_if_have_access_task=tasks.verify_if_have_access_task,
            get_modules_list_task=tasks.get_modules_list_task,
            create_module_task=tasks.create_module_task,
            delete_module_task=tasks.delete_module_task,
            get_permissions_task=tasks.get_permissions_task,
            create_permission_task=tasks.create_permission_task,
            delete_permission_task=tasks.delete_permission_task,
            get_session_modules_task=tasks.get_session_modules_task,
            get_user_task=tasks.get_user_task,
            create_user_task=tasks.create_user_task,
            delete_user_task=tasks.delete_user_task,
            update_user_task=tasks.update_user_task,
            get_session_user_task=tasks.get_session_user_task,
            run_registrations_rpa_task=tasks.run_registrations_rpa_task,
            create_registration_task=tasks.create_registration_task,
            update_registration_task=tasks.update_registration_task,
            get_registration_task=tasks.get_registration_task,
            delete_registration_task=tasks.delete_registration_task,
            run_wsgi_application_task=tasks.run_wsgi_application
        )
        self.cli = Cli(
            get_financial_data_task=tasks.get_financial_data_task,
            get_federal_revenue_data=tasks.get_federal_revenue_data_task,
            date_tasks=tasks.date_tasks,
            convert_df_to_str_task=tasks.convert_df_to_str_task,
        )
