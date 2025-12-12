from src.tasks.tasks import Tasks
from src.engines.engines import Engines

from .modules.consult_federal_revenue_data import ConsultFederalRevenueData
from .modules.consult_financial_data import ConsultFinancialData

class Cli:
    
    def __init__(self, tasks: Tasks, engines: Engines) -> None:
        self.tasks = tasks
        self.engines = engines
        self.consult_federal_revenue_data = ConsultFederalRevenueData(self.engines, self.tasks)
        self.consult_financial_data = ConsultFinancialData(self.engines, self.tasks)
    
    def main(self) -> None:
        self.engines.cli_session_engine.save_in_session("user", self.engines.environ_engine.get_os_user())
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
                print(f"⌚ <{self.engines.date_engine.get_today_str_with_time()}>\n{data}\n")
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
