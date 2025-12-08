from src.engines.sap_engine.sap_engine import SapEngine
from src.engines.sap_engine.models import *
from src.engines.log_engine import LogEngine
from src.engines.wsgi_engine.wsgi_session_manager_engine import WsgiSessionManagerEngine
from src.engines.cli_session_manager_engine import CliSessionManagerEngine

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
    
    def __init__(self,
        sap_engine: SapEngine,
        log_engine: LogEngine,
        session_manager_engine: WsgiSessionManagerEngine | CliSessionManagerEngine,
        need_authentication: bool
    ) -> None:
        self.sap_engine = sap_engine
        self.log_engine = log_engine
        self.session_manager_engine = session_manager_engine
        self.need_authentication = need_authentication
    
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
            if self.need_authentication:
                if not self.session_manager_engine.is_user_in_session():
                    return Response(success=False, message="❌ Necessário fazer login.", data="")
                if not self.session_manager_engine.have_user_module_access("zCoter"):
                    return Response(success=False, message="❌ Sem acesso.", data="")
            doc_number = self.sap_engine.order_creator.create(
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
            self.log_engine.write_text(f"👤 Usuário ({self.session_manager_engine.get_session_user()}): ✅ Sucesso ao criar documento no SAP ({doc_number}).")
            return Response(success=True, message=f"✅ Sucesso ao criar documento no SAP ({doc_number}).", data=doc_number)
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (CreateOrderTask) task in (main) method: {error}")
            self.sap_engine.sap_gui.go_home()
            raise Exception("❌ Erro interno ao criar documento no SAP. Contate o administrador.")
