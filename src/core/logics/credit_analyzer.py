from src.core.models import CreditAnalysisResponse

from datetime import datetime
from babel.numbers import format_currency

class CreditAnalyzer:
    
    def _convert_client_data_for_response(self, financial_data: object) -> object:
        try:
            financial_data.margin = format_currency(financial_data.margin, "BRL", locale="pt_BR")
        except:
            pass
        try:
            financial_data.maturity = datetime.strftime(financial_data.maturity, "%d/%m/%Y")
        except:
            pass
        return financial_data
    
    def _mount_response(self, financial_data: object, order: object, status: str, message: str) -> CreditAnalysisResponse:
        return CreditAnalysisResponse(
            order=order.order_site,
            order_value=format_currency(order.total_value, "BRL", locale="pt_BR"),
            client_margin=financial_data.margin,
            client_maturity=financial_data.maturity,
            client_overdue_nfs=financial_data.overdue_nfs,
            status=status,
            message=message
        )
    
    def do_credit_analysis(self, financial_data: object, order: object) -> CreditAnalysisResponse:
        reasons = ""
        status = "Aprovado"
        if financial_data.limit == "Sem limite ativo.":
            reasons += "\n|__ Sem limite de crédito ativo."
            status = "Recusado"
        elif financial_data.maturity < datetime.now().date():
            reasons += f"\n|__ Limite vencido em {datetime.strftime(financial_data.maturity, "%d/%m/%Y")}."
            status = "Recusado"
        if financial_data.margin != "Sem margem disponível." and financial_data.margin < float(order.total_value):
            reasons += f"\n|__ Valor do pedido excede a margem disponível. Valor do pedido: {f"R$ {float(order.total_value):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")} / Margem livre: {f"R$ {financial_data.margin:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")}."
            status = "Recusado"
        if financial_data.overdue_nfs != "Sem vencidos.":
            motivos += f"\n|__ Possui vencidos: {financial_data.overdue_nfs}."
            status = "Recusado"
        if status == "Aprovado":
            message = f"Pedido {order.order_site} liberado."
        else:
            message = f"Pedido {order.order_site} recusado:{reasons}"
        financial_data = self._convert_client_data_for_response(financial_data=financial_data)
        response = self._mount_response(financial_data=financial_data, order=order, status=status, message=message)
        return response
