from src.tasks.tasks import Tasks
from src.engines.engines import Engines

class UpdateOrdersPme:
    
    def __init__(self, engines: Engines, tasks: Tasks) -> None:
        self.engines = engines
        self.tasks = tasks
    
    def main(self) -> None:
        try:
            print(f"✅ Selecionado o módulo: 3 - Atualizar Ordens PME (1148).\n")
            print(f"⌚ <{self.engines.date_engine.get_today_str_with_time()}>")
            if self.tasks.update_orders_pme_task.status == "ATIVO":
                print("Status: 🟢 ATIVO")
                print("|__ ⏹️ Digite (PARAR) para encerrar.")
                print("|__ ↩️ Digite (VOLTAR) para retornar.")
                print("")
            elif self.tasks.update_orders_pme_task.status == "INATIVO":
                print("Status: 🔴 INATIVO")
                print("|__ ▶️ Digite (INICIAR) para ativar.")
                print("|__ ↩️ Digite (VOLTAR) para retornar.")
                print("")
            elif self.tasks.update_orders_pme_task.status == "ERRO":
                print("Status: ⚠️ ERRO")
                print("|__ ❌ Erro interno ao atualizar ordens do PME. Contate o administrador.")
                print("")
                return
            else:
                print("Status: ⚠️ NÃO IDENTIFICADO")
                print("|__ ❌ Erro interno ao atualizar ordens do PME. Contate o administrador.")
                print("")
                return
            response = input("📍 Selecione a opção: ")
            if response == "VOLTAR":
                print("")
                return
            elif response == "INICIAR":
                if self.tasks.update_orders_pme_task.status == "ATIVO":
                    print("⚠️ Processo já está ativo.")
                    print("")
                    return
                self.engines.thread_engine.start_single_thread(self.tasks.update_orders_pme_task.main)
            elif response == "PARAR":
                if self.tasks.update_orders_pme_task.status == "INATIVO":
                    print("⚠️ Processo já está parado.")
                    print("")
                    return
                self.tasks.update_orders_pme_task.stop = True
            else:
                print("❌ Selecione uma opção válida.")
                print("")
                return
        except Exception as error:
            self.engines.log_engine.write_error("cli/update_orders_pme", f"❌ Error in (UpdateOrdersPme) in (main) method: {error}")
            print(f"❌ Erro interno ao atualizar ordens do PME. Contate o administrador.\n")
