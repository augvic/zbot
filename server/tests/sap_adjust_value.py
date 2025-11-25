from src.components.infra.sap_clients.clients.order_creator import OrderCreator
from src.components.infra.sap_clients.models import Item

# Order: 2000420531
item = Item(
    sku="",
    quantity="28",
    center="",
    deposit="",
    guarantee="",
    over="",
    unit_value=3233.80,
    total_value=90546.42,
    is_parent_item=True
)
order_creator = OrderCreator()
order_creator.init_force()
order_creator._unit_value_adjustment_loop(item)
