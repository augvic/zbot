from src.modules.sap_handler.sap_handler import SapHandler
from src.modules.sap_handler.models import *
from src.modules.log_system import LogSystem

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str

@dataclass
class PartnerModel:
    
    key: str
    code: str

@dataclass
class ComissionModel:
    
    key: str
    code: str
    percentage: str

@dataclass
class ItemModel:
    
    sku: str
    quantity: str
    center: str
    deposit: str
    guarantee: str
    over: str
    unit_value: float
    total_value: float
    is_parent_item: bool

@dataclass
class OrderModel:
    
    doc_type: str
    organization: str
    channel: str
    office: str
    team: str
    order_name: str
    issuer: str
    receiver: str
    payment_condition: str
    incoterm: str
    reason: str
    table: str
    expedition: str
    payment_way: str
    additional_data: str
    items: list[ItemModel]
    partners: list[PartnerModel]
    comissions: list[ComissionModel]

class CreateOrder:
    
    def __init__(self,
        sap_handler: SapHandler,
        log_system: LogSystem,
    ) -> None:
        self.sap_handler = sap_handler
        self.log_system = log_system
    
    def main(self,
        user: str,
        doc_type: str,
        organization: str,
        channel: str,
        office: str,
        team: str,
        order_name: str,
        issuer: str,
        receiver: str,
        payment_condition: str,
        incoterm: str,
        reason: str,
        table: str,
        expedition: str,
        payment_way: str,
        additional_data: str,
        items: list[dict[str, str | bool | float]],
        partners: list[dict[str, str]],
        comissions:  list[dict[str, str]]
    ) -> Response:
        try:
            doc_number = self.sap_handler.order_creator.create(
                doc_type=doc_type,
                organization=organization,
                channel=channel,
                office=office,
                team=team,
                order_name=order_name,
                issuer=issuer,
                receiver=receiver,
                payment_condition=payment_condition,
                incoterm=incoterm,
                reason=reason,
                table=table,
                expedition=expedition,
                payment_way=payment_way,
                additional_data=additional_data,
                items=[{"sku": item["sku"], "quantity": item["quantity"], "center": item["center"], "deposit": item["deposit"], "guarantee": item["guarantee"], "over": item["over"], "unit_value": item["unit_value"], "total_value": item["total_value"], "is_parent_item": item["is_parent_item"]} for item in items],
                partners=[{"key": partner["key"], "code": partner["code"]} for partner in partners],
                comissions=[{"key": comission["key"], "code": comission["code"], "percentage": comission["percentage"]} for comission in comissions]
            )
            self.log_system.write_text(f"👤 Usuário ({user}): ✅ Sucesso ao criar documento no SAP ({doc_number}).")
            return Response(success=True, message=f"✅ Sucesso ao criar documento no SAP ({doc_number}).")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({user}): ❌ Erro: {error}")
            self.sap_handler.sap_gui.go_home()
            raise Exception("❌ Erro interno ao criar documento no SAP. Contate o administrador.")
