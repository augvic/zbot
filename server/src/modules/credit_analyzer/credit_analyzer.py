from datetime import datetime
from babel.numbers import format_currency

from .models import CreditAnalysisResponse

class CreditAnalyzer:
    
    def _convert_client_data_for_response(self) -> None:
        try:
            self.margin = format_currency(self.margin, "BRL", locale="pt_BR")
        except:
            pass
        try:
            if isinstance(self.maturity, datetime):
                self.maturity = datetime.strftime(self.maturity, "%d/%m/%Y")
        except:
            pass
    
    def _mount_response(self, status: str, message: str) -> CreditAnalysisResponse:
        return CreditAnalysisResponse(
            order=self.order,
            order_value=format_currency(self.order_value, "BRL", locale="pt_BR"),
            client_margin=self.margin,
            client_maturity=self.maturity,
            client_overdue_nfs=self.overdue_nfs,
            status=status,
            message=message
        )
    
    def analyze(self,
        order: str,
        order_value: float,
        limit: str,
        margin: float | str,
        maturity: datetime | str,
        overdue_nfs: str,
    ) -> CreditAnalysisResponse:
        try:
            self.order = order
            self.order_value = order_value
            self.limit = limit
            self.margin = margin
            self.maturity = maturity
            self.overdue_nfs = overdue_nfs
            reasons = ""
            status = "Aprovado"
            if self.limit == "Sem limite ativo.":
                reasons += "\n|__ Sem limite de crédito ativo."
                status = "Recusado"
            elif isinstance(self.maturity, datetime) and self.maturity < datetime.now().date():
                reasons += f"\n|__ Limite vencido em {datetime.strftime(self.maturity, "%d/%m/%Y")}."
                status = "Recusado"
            if isinstance(self.margin, float) and self.margin < float(self.order_value):
                reasons += f"\n|__ Valor do pedido excede a margem disponível. Valor do pedido: {f"R$ {float(self.order_value):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")} / Margem livre: {f"R$ {self.margin:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")}."
                status = "Recusado"
            if self.overdue_nfs != "Sem vencidos.":
                reasons += f"\n|__ Possui vencidos: {self.overdue_nfs}."
                status = "Recusado"
            if status == "Aprovado":
                message = f"Pedido {self.order} liberado."
            else:
                message = f"Pedido {self.order} recusado:{reasons}"
            self._convert_client_data_for_response()
            response = self._mount_response(status=status, message=message)
            return response
        except Exception as error:
            raise Exception(f"Error in (CreditAnalyzer) component in (analyze) method: {error}.")
