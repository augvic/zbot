from src.threads.threads import Threads
from src.engines.engines import Engines

class UpdateOrdersPme:
    
    def __init__(self, engines: Engines, threads: Threads) -> None:
        self.engines = engines
        self.threads = threads
    
    def main(self) -> None:
        try:
            print(f"✅ Selecionado o módulo: 3 - Atualizar Ordens PME (1148).\n")
            print(f"⌚ <{self.engines.date_engine.get_today_str_with_time()}>")
            if self.threads.update_orders_pme_thread.status == "ATIVO":
                print("Status: 🟢 ATIVO")
                print("|__ ⏹️ Digite (PARAR) para encerrar.")
                print("|__ ↩️ Digite (VOLTAR) para retornar.")
                print("")
            elif self.threads.update_orders_pme_thread.status == "INATIVO":
                print("Status: 🔴 INATIVO")
                print("|__ ▶️ Digite (INICIAR) para ativar.")
                print("|__ ↩️ Digite (VOLTAR) para retornar.")
                print("")
            elif self.threads.update_orders_pme_thread.status == "ERRO":
                print("Status: ⚠️ ERRO")
                print("|__ ❌ Erro interno ao atualizar ordens do PME. Contate o administrador.")
                print("")
                return
            elif self.threads.update_orders_pme_thread.status == "PREPARANDO ENCERRAMENTO":
                print("Status: ⏳ PREPARANDO ENCERRAMENTO")
                print("|__ ▶️ Digite (REINICIAR) para reativar.")
                print("|__ ↩️ Digite (VOLTAR) para retornar.")
                print("")
            elif self.threads.update_orders_pme_thread.status == "SAP":
                print("Status: ⚠️ ERRO")
                print("|__ ❌ Verifique sua conexão com o SAP.")
                print("|__ ▶️ Digite (INICIAR) para ativar.")
                print("|__ ↩️ Digite (VOLTAR) para retornar.")
                print("")
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
                if self.threads.update_orders_pme_thread.status == "ATIVO":
                    print("⚠️ Processo já está ativo.")
                    print("")
                    return
                self.engines.thread_engine.start_single_thread(self.threads.update_orders_pme_thread.main)
            elif response == "PARAR":
                if self.threads.update_orders_pme_thread.status == "INATIVO":
                    print("⚠️ Processo já está parado.")
                    print("")
                    return
                self.threads.update_orders_pme_thread.stop = True
                self.threads.update_orders_pme_thread.status = "PREPARANDO ENCERRAMENTO"
            elif response == "REINICIAR":
                if self.threads.update_orders_pme_thread.status == "ATIVO":
                    print("⚠️ Processo já está ativo.")
                    print("")
                    return
                if self.threads.update_orders_pme_thread.status == "INATIVO":
                    print("⚠️ Processo já está parado.")
                    print("")
                    return
                self.threads.update_orders_pme_thread.stop = False
                self.threads.update_orders_pme_thread.status = "ATIVO"
            else:
                print("❌ Selecione uma opção válida.")
                print("")
                return
        except Exception as error:
            self.engines.log_engine.write_error("cli/update_orders_pme", f"❌ Error in (UpdateOrdersPme) in (main) method: {error}")
            print(f"❌ Erro interno ao atualizar ordens do PME. Contate o administrador.\n")
