from src.components.infra.sap_clients.clients.financial_data_getter import FinancialDataGetter
from src.components.infra.sap_clients.models import FinancialData
from src.components.infra.pos_fr_api.component import PositivoFederalRevenueApi
from src.components.infra.pos_fr_api.models import FederalRevenueData
from pandas import DataFrame, set_option
from sys import exit
from datetime import datetime
from tabulate import tabulate

class Cli:
    
    def __init__(self):
        list_to_print = [
            f"🛠️ zBot (Back Office Tools) client.",
            f"\n|__ 🔍 1 - Consultar Dados da Receita Federal.",
            f"\n|__ 💲 2 - Consultar Dados Financeiros de Cliente.",
            f'\n|__ 🔚 Digite "SAIR" para sair.'
        ]
        data = ""
        for print_element in list_to_print:
            data += print_element
        print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{data}\n")
        self._select_module()
        self.__init__()
    
    def _printdf(self, df: DataFrame) -> None:
        set_option("display.max_rows", None)
        table = tabulate(df.to_dict("records"), headers="keys", tablefmt="github", showindex=False)
        print(f"{table}\n")
    
    def _print_federal_revenue_data(self, data: FederalRevenueData) -> None:
        list_to_print = [
            f"🟦 CNPJ: {data.cnpj}\n",
            f"🟦 Abertura: {data.opening}\n",
            f"🟦 Razão Social: {data.company_name}\n",
            f"🟦 Nome Fantasia: {data.trade_name}\n",
            f"🟦 Natureza Jurídica: {data.legal_nature_id} | {data.legal_nature}\n",
            f"🟦 Situação Cadastral: {data.registration_status}\n",
            f"🟦 Endereço Completo: {data.street}, {data.number} | {data.complement} | {data.neighborhood} | {data.pac} | {data.city} | {data.state}\n",
            f"🟦 Telefone: {data.fone}\n",
            f"🟦 E-mail: {data.email}\n",
            f"🟦 Regime Tributário: {data.tax_regime['regime_tributario']}\n",
            f"🟦 Recebimento Comissão: {data.comission_receipt}\n",
            f"🟦 Inscrições Estaduais:",
            *[f"\n|__ {registration["state_registration"]} | {registration["status"]}" for registration in data.state_registrations],
            f"\n🟦 Inscrições Suframa:",
            *[f"\n|__ {registration["suframa_registration"]} | {registration["status"]}" for registration in data.suframa_registrations],
            f"\n🟦 CNAE:",
            *[f"\n|__ {ncea["code"]} | {ncea["description"]}" for ncea in data.ncea]
        ]
        data_to_print = ""
        for print_element in list_to_print:
            data_to_print += print_element
        print(f"{data_to_print}\n")
    
    def _print_financial_data(self, data: FinancialData) -> None:
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
        print(f"{data_to_print}\n")
        if isinstance(data.fbl5n_table, DataFrame):
            self._printdf(data.fbl5n_table)
    
    def _select_module(self) -> None:
        while True:
            module = input("📍 Selecione o módulo: ")
            try:    
                if module == "SAIR":
                    exit(0)
                if module == "1":
                    print(f"✅ Selecionado o módulo: 1 - Consultar Dados da Receita Federal.\n")
                    print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>")
                    while True:
                        print('↩️ Digite "VOLTAR" para retornar.')
                        cnpj = input("🏪 Informe o CNPJ: ")
                        if cnpj == "VOLTAR":
                            print("")
                            self.__init__()
                        if cnpj == "" or len(cnpj) != 14:
                            print("❗ Informe um CNPJ válido.\n")
                        else:
                            break
                    task = PositivoFederalRevenueApi()
                    data = task.get_data(cnpj=cnpj)
                    self._print_federal_revenue_data(data=data)
                    break
                elif module == "2":
                    print(f"✅ Selecionado o módulo: 2 - Consultar Dados Financeiros de Cliente.\n")
                    print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>")
                    while True:
                        print('↩️ Digite "VOLTAR" para retornar.')
                        cnpj_root = input("Informe a raiz do CNPJ: ")
                        if cnpj_root == "VOLTAR":
                            print("")
                            self.__init__()
                        if cnpj_root == "" or len(cnpj_root) != 8:
                            print("❗ Informe uma raiz de CNPJ válida.\n")
                        else:
                            break
                    task = FinancialDataGetter()
                    data = task.get_data(cnpj_root=cnpj_root)
                    self._print_financial_data(data=data)
                    break
                else:
                    print(f"❗ Selecione um módulo válido.\n")
            except Exception as error:
                print(f"❌ Erro: {error}\n")
                break

Cli()
