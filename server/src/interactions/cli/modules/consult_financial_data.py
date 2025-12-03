from src.tasks.get_financial_data_task import GetFinancialDataTask
from src.engines.date_engine import DateEngine
from src.engines.dataframe_engine import DataFrameEngine

from pandas import DataFrame
from datetime import datetime
from src.engines.sap_engine.models import FinancialData

class ConsultFinancialData:
    
    def __init__(self,
        get_financial_data_task: GetFinancialDataTask,
        date_engine: DateEngine,
        dataframe_engine: DataFrameEngine,
    ) -> None:
        self.get_financial_data_task = get_financial_data_task
        self.date_utility = date_engine
        self.dataframe_handler = dataframe_engine
    
    def _print_financial_data(self, data: FinancialData) -> None:
        list_to_print = []
        list_to_print.append(f"🟦 Raiz do CNPJ: {data.cnpj_root}.\n")
        if "Sem limite ativo." in [data.limit, data.maturity]:
            list_to_print.append(f"🟦 Vencimento do Limite: Sem limite ativo.\n")
            list_to_print.append(f"🟦 Limite: Sem limite ativo.\n")
        else:
            if isinstance(data.maturity, datetime):
                list_to_print.append(f"🟦 Vencimento do Limite: {self.date_utility.convert_to_string(data.maturity)}.\n")
            list_to_print.append(f"🟦 Limite: {f"R$ {data.limit:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")}.\n")
        if data.in_open == "Sem valores em aberto.":
            list_to_print.append(f"🟦 Valor em Aberto: Nenhum.\n")
        else:
            list_to_print.append(f"🟦 Valor em Aberto: {f"R$ {data.in_open:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")}.\n")
        if data.margin != "Sem margem disponível.":
            list_to_print.append(f"🟦 Margem: {f"R$ {data.margin:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")}.\n")
        else:
            list_to_print.append(f"🟦 Margem: Não Disponível.\n")
        if data.overdue_nfs == "Sem vencidos.":
            list_to_print.append(f"🟦 Notas Vencidas: Nenhuma.")
        else:
            list_to_print.append(f"🟦 Notas vencidas: {data.overdue_nfs}.")
        data_to_print = ""
        for print_element in list_to_print:
            data_to_print += print_element
        print(f"{data_to_print}\n")
        if isinstance(data.fbl5n_table, DataFrame):
            table = self.dataframe_handler.convert_to_string(data.fbl5n_table)
            print(f"{table}\n")
    
    def main(self) -> None:
        try:
            print(f"✅ Selecionado o módulo: 2 - Consultar Dados Financeiros de Cliente.\n")
            print(f"⌚ <{self.date_utility.get_today_str_with_time()}>")
            print('↩️ Digite "VOLTAR" para retornar.')
            cnpj_root = input("Informe a raiz do CNPJ: ")
            if cnpj_root == "VOLTAR":
                print("")
                return
            response = self.get_financial_data_task.main(cnpj_root=cnpj_root)
            if not response.success:
                print(response.message + "\n")
                return
            if response.data:
                self._print_financial_data(data=response.data)
        except Exception as error:
            print(f"{error}\n")
