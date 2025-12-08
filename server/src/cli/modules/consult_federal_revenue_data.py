from src.tasks.get_federal_revenue_data_task import GetFederalRevenueDataTask
from src.engines.date_engine import DateEngine

from src.engines.federal_revenue_api_engine.models import FederalRevenueData

class ConsultFederalRevenueData:
    
    def __init__(self,
        get_federal_revenue_data_task: GetFederalRevenueDataTask,
        date_engine: DateEngine
    ) -> None:
        self.get_federal_revenue_data_task = get_federal_revenue_data_task
        self.date_utility = date_engine
    
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
            f"🟦 Regime Tributário: {data.tax_regime}\n",
            f"🟦 Recebimento Comissão: {data.comission_receipt}\n",
            f"🟦 Inscrições Estaduais:",
            *[f"\n|__ {registration['state_registration']} | {registration['status']}" for registration in data.state_registrations],
            f"\n🟦 Inscrições Suframa:",
            *[f"\n|__ {registration['suframa_registration']} | {registration['status']}" for registration in data.suframa_registrations],
            f"\n🟦 CNAE:",
            *[f"\n|__ {ncea['code']} | {ncea['description']}" for ncea in data.ncea]
        ]
        data_to_print = ""
        for print_element in list_to_print:
            data_to_print += print_element
        print(f"{data_to_print}\n")
    
    def main(self) -> None:
        try:
            print(f"✅ Selecionado o módulo: 1 - Consultar Dados da Receita Federal.\n")
            print(f"⌚ <{self.date_utility.get_today_str_with_time()}>")
            print('↩️ Digite "VOLTAR" para retornar.')
            cnpj = input("🏪 Informe o CNPJ: ")
            if cnpj == "VOLTAR":
                print("")
                return
            response = self.get_federal_revenue_data_task.main(cnpj=cnpj)
            if not response.success:
                print(response.message + "\n")
                return
            if response.data:
                self._print_federal_revenue_data(data=response.data)
        except Exception as error:
            print(f"{error}\n")
