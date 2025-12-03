from src.tasks.get_financial_data_task import GetFinancialDataTask
from src.tasks.get_federal_revenue_data_task import GetFederalRevenueDataTask
from src.engines.date_engine import DateEngine
from src.engines.dataframe_engine import DataFrameEngine
from src.engines.environ_engine import EnvironEngine
from src.engines.cli_session_manager_engine import CliSessionManagerEngine

from .modules.consult_federal_revenue_data import ConsultFederalRevenueData
from .modules.consult_financial_data import ConsultFinancialData

class Cli:
    
    def __init__(self,
        get_financial_data_task: GetFinancialDataTask,
        get_federal_revenue_data_task: GetFederalRevenueDataTask,
        date_engine: DateEngine,
        dataframe_engine: DataFrameEngine,
        environ_engine: EnvironEngine,
        cli_session_manager_engine: CliSessionManagerEngine
    ) -> None:
        self.get_financial_data_task = get_financial_data_task
        self.get_federal_revenue_data_task = get_federal_revenue_data_task
        self.date_utility = date_engine
        self.dataframe_handler = dataframe_engine
        self.os_environ = environ_engine
        self.cli_session_manager_engine = cli_session_manager_engine
        self.consult_federal_revenue_data = ConsultFederalRevenueData(
            get_federal_revenue_data_task=get_federal_revenue_data_task,
            date_engine=date_engine
        )
        self.consult_financial_data = ConsultFinancialData(
            get_financial_data_task=get_financial_data_task,
            date_engine=date_engine,
            dataframe_engine=dataframe_engine
        )
    
    def main(self) -> None:
        try:
            while True:
                list_to_print = [
                    f"🛠️ zBot (Back Office Tools) client.",
                    f"\n|__ 🔍 1 - Consultar Dados da Receita Federal.",
                    f"\n|__ 💲 2 - Consultar Dados Financeiros de Cliente.",
                    f"\n|__ 🔚 Digite (SAIR) para sair."
                ]
                data = ""
                for print_element in list_to_print:
                    data += print_element
                print(f"⌚ <{self.date_utility.get_today_str_with_time()}>\n{data}\n")
                module = input("📍 Selecione o módulo: ")
                if module == "SAIR":
                    break
                if module == "1":
                    self.consult_federal_revenue_data.main()
                elif module == "2":
                    self.consult_financial_data.main()
                else:
                    print(f"❗ Selecione um módulo válido.\n")
        except Exception as error:
            print(f"❌ Erro: {error}\n")
