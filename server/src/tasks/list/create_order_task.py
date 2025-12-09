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
        self.runtime = "cli"
    
    def set_runtime(self, runtime: str) -> None:
        self.runtime = runtime
    
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
            if self.runtime == "cli":
                self.session_manager_engine = self.engines.cli_session_engine
            else:
                self.session_manager_engine = self.engines.wsgi_engine.session_manager
            doc_number = self.engines.sap_engine.order_creator.create(
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
            self.engines.log_engine.write_text("tasks/create_order_task", f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Sucesso ao criar documento no SAP ({doc_number}).")
            return Response(success=True, message=f"✅ Sucesso ao criar documento no SAP ({doc_number}).", data=doc_number)
        except Exception as error:
            self.engines.log_engine.write_error("tasks/create_order_task", f"❌ Error in (CreateOrderTask) task in (main) method: {error}")
            self.engines.sap_engine.sap_gui.go_home()
            raise Exception("❌ Erro interno ao criar documento no SAP. Contate o administrador.")
