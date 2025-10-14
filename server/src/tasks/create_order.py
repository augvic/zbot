from datetime import datetime
from src.components.sap_clients.clients.order_creator import OrderCreator
from src.components.sap_clients.models import *

class CreateOrder:
    
    def _setup(self) -> None:
        self.order_creator = OrderCreator()
    
    def execute(self) -> dict[str, str | bool]:
        self._setup()
        try:
            order = Order(
                doc_type="ZCOT",
                organization="3100",
                channel="15",
                office="1105",
                team="058",
                order_name="TESTE",
                issuer="1000791368",
                receiver="1000791368",
                payment_condition="Z011",
                incoterm="CIF",
                reason="900",
                table="",
                expedition="01",
                payment_way="E",
                additional_data="",
                items=[
                    Item(
                        sku="1308507",
                        quantity="70",
                        center="3010",
                        deposit="",
                        guarantee="",
                        over="",
                        unit_value=3000.80,
                        total_value=210056.01,
                        is_parent_item=True
                    ),
                    Item(
                        sku="8000481",
                        quantity="70",
                        center="3010",
                        deposit="",
                        guarantee="",
                        over="",
                        unit_value=935.20,
                        total_value=65464.21,
                        is_parent_item=True
                    ),
                    Item(
                        sku="11129839",
                        quantity="70",
                        center="3010",
                        deposit="",
                        guarantee="",
                        over="",
                        unit_value=42.00,
                        total_value=2940.09,
                        is_parent_item=False
                    ),
                    Item(
                        sku="11092515",
                        quantity="70",
                        center="3010",
                        deposit="",
                        guarantee="",
                        over="",
                        unit_value=21.00,
                        total_value=1469.66,
                        is_parent_item=False
                    )
                ],
                partners=[],
                comissions=[
                    Comission(
                        key="Z2",
                        code="2000006653",
                        percentage="0,32"
                    ),
                    Comission(
                        key="Z5",
                        code="2000005674",
                        percentage="0,32"
                    ),
                    Comission(
                        key="Z6",
                        code="5000002213",
                        percentage="0,50"
                    ),
                    Comission(
                        key="Z7",
                        code="COMPROV",
                        percentage="0,30"
                    )
                ]
            )
            doc_number = self.order_creator.create(order)
            return {"success": True, "message": doc_number}
        except Exception as error:
            print(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n{error}\n")
            self.order_creator.go_home()
            return {"success": False, "message": "Erro ao criar documento no SAP."}

if __name__ == "__main__":
    task = CreateOrder()
    task.execute()
