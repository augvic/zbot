from src.modules.sap_handler.sap_handler import SapHandler
from src.modules.sap_handler.models import *
from src.modules.session_manager import SessionManager
from src.modules.log_system import LogSystem
from .models import *

class CreateOrder:
    
    def __init__(self,
        sap_handler: SapHandler,
        log_system: LogSystem,
        session_manager: SessionManager
    ) -> None:
        self.sap_handler = sap_handler
        self.log_system = log_system
        self.session_manager = session_manager
    
    def main(self, order_model: OrderModel) -> Response:
        try:
            doc_number = self.sap_handler.order_creator.create(
                Order(
                    doc_type=order_model.doc_type,
                    organization=order_model.organization,
                    channel=order_model.channel,
                    office=order_model.office,
                    team=order_model.team,
                    order_name=order_model.order_name,
                    issuer=order_model.issuer,
                    receiver=order_model.receiver,
                    payment_condition=order_model.payment_condition,
                    incoterm=order_model.incoterm,
                    reason=order_model.reason,
                    table=order_model.table,
                    expedition=order_model.expedition,
                    payment_way=order_model.payment_way,
                    additional_data=order_model.additional_data,
                    items=[Item(sku=item.sku, quantity=item.quantity, center=item.center, deposit=item.deposit, guarantee=item.guarantee, over=item.over, unit_value=item.unit_value, total_value=item.total_value, is_parent_item=item.is_parent_item) for item in order_model.items],
                    partners=[Partner(key=partner.key, code=partner.code) for partner in order_model.partners],
                    comissions=[Comission(key=comission.key, code=comission.code, percentage=comission.percentage) for comission in order_model.comissions]
                )
            )
            self.log_system.write_text(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ✅ Sucesso ao criar documento no SAP ({doc_number}).")
            return Response(success=True, message=f"✅ Sucesso ao criar documento no SAP ({doc_number}).")
        except Exception as error:
            self.log_system.write_error(f"👤 Usuário ({self.session_manager.get_from_session("user")}): ❌ Erro: {error}.")
            self.sap_handler.sap_gui.go_home()
            raise Exception("❌ Erro interno ao criar documento no SAP. Contate o administrador.")
