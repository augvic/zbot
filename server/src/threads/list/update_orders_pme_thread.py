from src.engines.engines import Engines
from src.engines.list.sap_engine.errors import *

class UpdateOrdersPmeThread:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
        self.status = "INATIVO"
        self.stop = False
    
    def main(self) -> None:
        self.status = "ATIVO"
        try:
            while True:
                if self.stop == True:
                    self.stop = False
                    self.status = "INATIVO"
                    break
                self.engines.go_deep_engine.go_deep_pe_session_client.login()
                self.engines.go_deep_engine.go_deep_pe_session_client.export_orders_to_csv()
                sellers_df = self.engines.csv_handler.to_df("sellers.csv")
                orders_df = self.engines.csv_handler.to_df("orders.csv")
                orders_df_columns_used = orders_df[["ERP Codigo Pedido", "Nome do usuário", "Status"]]
                orders_df_filtered = orders_df_columns_used[orders_df_columns_used["ERP Codigo Pedido"].notna() & orders_df_columns_used["Nome do usuário"].isin(sellers_df["Seller Name"]) & orders_df_columns_used["Status"].isin(["Pedido integrado", "Pagamento aprovado", "Em separação"])].copy()
                orders_modified_df = self.engines.csv_handler.to_df("orders_modified.csv")
                orders_modified = orders_modified_df["Orders Modified"].astype(str).to_list()
                for _, order_df_row in orders_df_filtered.iterrows():
                    orders = order_df_row["ERP Codigo Pedido"]
                    orders = str(orders).split("|")
                    for order in orders:
                        order = str(int(float(order)))
                        if order not in orders_modified:
                            seller_df_row = sellers_df[sellers_df["Seller Name"] == order_df_row["Nome do usuário"]].iloc[0]
                            sap = self.engines.sap_engine.instantiate()
                            sap.order_client.update_order_pe(order, seller_df_row["Partner Code"], seller_df_row["Comission Code"])
                            self.engines.csv_handler.save_order_modified(order)
                self.engines.time_engine.sleep(1800)
        except SapGuiErrors:
            self.status = "SAP"
        except Exception as error:
            self.engines.log_engine.write_error("threads/update_orders_pme_thread", f"❌ Error in (UpdateOrdersThread) in (main) method: {error}")
            self.stop = False
            self.status = "ERRO"
