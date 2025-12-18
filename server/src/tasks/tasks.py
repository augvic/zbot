from .list.create_module_task import CreateModuleTask
from .list.create_order_task import CreateOrderTask
from .list.create_permission_task import CreatePermissionTask
from .list.create_registration_task import CreateRegistrationTask
from .list.create_user_task import CreateUserTask
from .list.delete_module_task import DeleteModuleTask
from .list.delete_permission_task import DeletePermissionTask
from .list.delete_registration_task import DeleteRegistrationTask
from .list.delete_user_task import DeleteUserTask
from .list.get_federal_revenue_data_task import GetFederalRevenueDataTask
from .list.get_financial_data_task import GetFinancialDataTask
from .list.get_modules_task import GetModulesTask
from .list.get_permissions_task import GetPermissionsTask
from .list.get_registration_task import GetRegistrationTask
from .list.get_user_task import GetUserTask
from .list.update_registration_task import UpdateRegistrationTask
from .list.update_user_task import UpdateUserTask
from .list.update_orders_pme_task import UpdateOrdersPmeTask

from src.engines.engines import Engines

class Tasks:
    
    def __init__(self, engines: Engines) -> None:
        self.create_module_task = CreateModuleTask(engines)
        self.create_order_task = CreateOrderTask(engines)
        self.create_permission_task = CreatePermissionTask(engines)
        self.create_registration_task = CreateRegistrationTask(engines)
        self.create_user_task = CreateUserTask(engines)
        self.delete_module_task = DeleteModuleTask(engines)
        self.delete_permission_task = DeletePermissionTask(engines)
        self.delete_registration_task = DeleteRegistrationTask(engines)
        self.delete_user_task = DeleteUserTask(engines)
        self.get_federal_revenue_data_task = GetFederalRevenueDataTask(engines)
        self.get_financial_data_task = GetFinancialDataTask(engines)
        self.get_modules_task = GetModulesTask(engines)
        self.get_permissions_task = GetPermissionsTask(engines)
        self.get_registration_task = GetRegistrationTask(engines)
        self.get_user_task = GetUserTask(engines)
        self.update_registration_task = UpdateRegistrationTask(engines)
        self.update_user_task = UpdateUserTask(engines)
        self.update_orders_pme_task = UpdateOrdersPmeTask(engines)
