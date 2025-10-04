from src.logics.models import CreditAnalysisResponse, DataToAnalyse
from datetime import datetime
from babel.numbers import format_currency

class CreditAnalyzer:
    
    def _convert_client_data_for_response(self, data: DataToAnalyse) -> DataToAnalyse:
        try:
            data.margin = format_currency(data.margin, "BRL", locale="pt_BR")
        except:
            pass
        try:
            if isinstance(data.maturity, datetime):
                data.maturity = datetime.strftime(data.maturity, "%d/%m/%Y")
        except:
            pass
        return data
    
    def _mount_response(self, data: DataToAnalyse, status: str, message: str) -> CreditAnalysisResponse:
        return CreditAnalysisResponse(
            order=data.order,
            order_value=format_currency(data.order_value, "BRL", locale="pt_BR"),
            client_margin=data.margin,
            client_maturity=data.maturity,
            client_overdue_nfs=data.overdue_nfs,
            status=status,
            message=message
        )
    
    def do_credit_analysis(self, data: DataToAnalyse) -> CreditAnalysisResponse:
        reasons = ""
        status = "Aprovado"
        if data.limit == "Sem limite ativo.":
            reasons += "\n|__ Sem limite de crédito ativo."
            status = "Recusado"
        elif isinstance(data.maturity, datetime) and data.maturity < datetime.now().date():
            reasons += f"\n|__ Limite vencido em {datetime.strftime(data.maturity, "%d/%m/%Y")}."
            status = "Recusado"
        if isinstance(data.margin, float) and data.margin < float(data.order_value):
            reasons += f"\n|__ Valor do pedido excede a margem disponível. Valor do pedido: {f"R$ {float(data.order_value):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")} / Margem livre: {f"R$ {data.margin:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")}."
            status = "Recusado"
        if data.overdue_nfs != "Sem vencidos.":
            reasons += f"\n|__ Possui vencidos: {data.overdue_nfs}."
            status = "Recusado"
        if status == "Aprovado":
            message = f"Pedido {data.order} liberado."
        else:
            message = f"Pedido {data.order} recusado:{reasons}"
        data = self._convert_client_data_for_response(data=data)
        response = self._mount_response(data=data, status=status, message=message)
        return response
