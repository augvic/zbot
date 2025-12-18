from src.engines.engines import Engines

from dataclasses import dataclass

@dataclass
class Response:
    
    success: bool
    message: str
    data: str

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

class CreateOrderTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
    
    def main(self,
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
            sap = self.engines.sap_engine.instantiate()
            doc_number = sap.order_client.create(
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
            return Response(success=True, message=f"✅ Sucesso ao criar documento no SAP ({doc_number}).", data=doc_number)
        except Exception as error:
            sap.sap_gui.go_home()
            raise Exception(f"❌ Error in (CreateOrderTask) in (main) method: {error}")
