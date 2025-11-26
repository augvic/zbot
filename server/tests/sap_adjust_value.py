from src.modules.sap_handler.sap_handler import SapHandler
from src.modules.sap_handler.models import Item

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
sap_handler = SapHandler()
sap_handler.sap_gui.init_force()
sap_handler.order_creator._unit_value_adjustment_loop(item)
