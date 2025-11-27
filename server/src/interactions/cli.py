from src.tasks.get_financial_data.get_financial_data import GetFinancialData
from src.tasks.get_federal_revenue_data.get_federal_revenue_data import GetFederalRevenueData
from src.tasks.date_tasks import DateTasks
from src.tasks.convert_df_to_str import ConvertDfToStr
from pandas import DataFrame
from datetime import datetime

class Cli:
    
    def __init__(self,
        get_financial_data_task: GetFinancialData,
        get_federal_revenue_data: GetFederalRevenueData,
        date_tasks: DateTasks,
        convert_df_to_str_task: ConvertDfToStr
    ) -> None:
        self.get_financial_data_task = get_financial_data_task
        self.get_federal_revenue_data = get_federal_revenue_data
        self.date_tasks = date_tasks
        self.convert_df_to_str_task = convert_df_to_str_task
    
    def _printdf(self, df: DataFrame) -> None:
        table = self.convert_df_to_str_task.main(df)
        print(f"{table}\n")
    
    def _print_federal_revenue_data(self, data: dict) -> None:
        list_to_print = [
            f"🟦 CNPJ: {data['cnpj']}\n",
            f"🟦 Abertura: {data['opening']}\n",
            f"🟦 Razão Social: {data['company_name']}\n",
            f"🟦 Nome Fantasia: {data['trade_name']}\n",
            f"🟦 Natureza Jurídica: {data['legal_nature_id']} | {data['legal_nature']}\n",
            f"🟦 Situação Cadastral: {data['registration_status']}\n",
            f"🟦 Endereço Completo: {data['street']}, {data['number']} | {data['complement']} | {data['neighborhood']} | {data['pac']} | {data['city']} | {data['state']}\n",
            f"🟦 Telefone: {data['fone']}\n",
            f"🟦 E-mail: {data['email']}\n",
            f"🟦 Regime Tributário: {data['tax_regime']}\n",
            f"🟦 Recebimento Comissão: {data['comission_receipt']}\n",
            f"🟦 Inscrições Estaduais:",
            *[f"\n|__ {registration['state_registration']} | {registration['status']}" for registration in data['state_registrations']],
            f"\n🟦 Inscrições Suframa:",
            *[f"\n|__ {registration['suframa_registration']} | {registration['status']}" for registration in data['suframa_registrations']],
            f"\n🟦 CNAE:",
            *[f"\n|__ {ncea['code']} | {ncea['description']}" for ncea in data['ncea']]
        ]
        data_to_print = ""
        for print_element in list_to_print:
            data_to_print += print_element
        print(f"{data_to_print}\n")
    
    def _print_financial_data(self, data: dict) -> None:
        list_to_print = []
        list_to_print.append(f"🟦 Raiz do CNPJ: {data["cnpj_root"]}.\n")
        if "Sem limite ativo." in [data["limit"], data["maturity"]]:
            list_to_print.append(f"🟦 Vencimento do Limite: Sem limite ativo.\n")
            list_to_print.append(f"🟦 Limite: Sem limite ativo.\n")
        else:
            if isinstance(data["maturity"], datetime):
                list_to_print.append(f"🟦 Vencimento do Limite: {self.date_tasks.convert_to_string(data["maturity"])}.\n")
            list_to_print.append(f"🟦 Limite: {f"R$ {data["limit"]:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")}.\n")
        if data["in_open"] == "Sem valores em aberto.":
            list_to_print.append(f"🟦 Valor em Aberto: Nenhum.\n")
        else:
            list_to_print.append(f"🟦 Valor em Aberto: {f"R$ {data["in_open"]:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")}.\n")
        if data["margin"] != "Sem margem disponível.":
            list_to_print.append(f"🟦 Margem: {f"R$ {data["margin"]:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")}.\n")
        else:
            list_to_print.append(f"🟦 Margem: Não Disponível.\n")
        if data["overdue_nfs"] == "Sem vencidos.":
            list_to_print.append(f"🟦 Notas Vencidas: Nenhuma.")
        else:
            list_to_print.append(f"🟦 Notas vencidas: {data["overdue_nfs"]}.")
        data_to_print = ""
        for print_element in list_to_print:
            data_to_print += print_element
        print(f"{data_to_print}\n")
        if isinstance(data["fbl5n_table"], DataFrame):
            self._printdf(data["fbl5n_table"])
    
    def _select_module(self) -> str | None:
        module = input("📍 Selecione o módulo: ")
        if module == "SAIR":
            return "break"
        if module == "1":
            print(f"✅ Selecionado o módulo: 1 - Consultar Dados da Receita Federal.\n")
            print(f"⌚ <{self.date_tasks.get_today_str_with_time()}>")
            while True:
                print('↩️ Digite "VOLTAR" para retornar.')
                cnpj = input("🏪 Informe o CNPJ: ")
                if cnpj == "VOLTAR":
                    print("")
                    return
                else:
                    break
            response = self.get_federal_revenue_data.main(cnpj=cnpj)
            if not response.success:
                print(response.message + "\n")
                return
            self._print_federal_revenue_data(data=response.data)
            return
        elif module == "2":
            print(f"✅ Selecionado o módulo: 2 - Consultar Dados Financeiros de Cliente.\n")
            print(f"⌚ <{self.date_tasks.get_today_str_with_time()}>")
            while True:
                print('↩️ Digite "VOLTAR" para retornar.')
                cnpj_root = input("Informe a raiz do CNPJ: ")
                if cnpj_root == "VOLTAR":
                    print("")
                    return
                else:
                    break
            response = self.get_financial_data_task.main(cnpj_root=cnpj_root)
            if not response.success:
                print(response.message + "\n")
            self._print_financial_data(data=response.data)
            return
        else:
            print(f"❗ Selecione um módulo válido.\n")
    
    def main(self) -> None:
        try:
            while True:
                list_to_print = [
                    f"🛠️ zBot (Back Office Tools) client.",
                    f"\n|__ 🔍 1 - Consultar Dados da Receita Federal.",
                    f"\n|__ 💲 2 - Consultar Dados Financeiros de Cliente.",
                    f'\n|__ 🔚 Digite "SAIR" para sair.'
                ]
                data = ""
                for print_element in list_to_print:
                    data += print_element
                print(f"⌚ <{self.date_tasks.get_today_str_with_time()}>\n{data}\n")
                response = self._select_module()
                if response == "break":
                    break
        except Exception as error:
            print(f"❌ Erro: {error}\n")
