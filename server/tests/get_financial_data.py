from src.components.infra.sap_clients.clients.financial_data_getter import FinancialDataGetter
from datetime import datetime
from pandas import DataFrame, set_option
from tabulate import tabulate

try:
    while True:
        print("==================================================")
        print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>")
        cnpj = input("Informe a raiz do CNPJ: ")
        data_getter = FinancialDataGetter()
        data = data_getter.get_data(cnpj)
        list_to_print = []
        list_to_print.append(f"🟦 Raiz do CNPJ: {data.cnpj_root}.\n")
        if "Sem limite ativo." in [data.limit, data.maturity]:
            list_to_print.append(f"🟦 Vencimento do Limite: Sem limite ativo.\n")
            list_to_print.append(f"🟦 Limite: Sem limite ativo.\n")
        else:
            if isinstance(data.maturity, datetime):
                list_to_print.append(f"🟦 Vencimento do Limite: {datetime.strftime(data.maturity, "%d/%m/%Y")}.\n")
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
        print(data_to_print)
        if isinstance(data.fbl5n_table, DataFrame):
            set_option("display.max_rows", None)
            table = tabulate(data.fbl5n_table.to_dict("records"), headers="keys", tablefmt="github", showindex=False)
            print(f"\n{table}")
except Exception as error:
    print(f"Ocorreu um erro: {error}")
    print("==================================================")
