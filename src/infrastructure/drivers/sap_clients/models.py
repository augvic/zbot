from pandas import DataFrame

class FinancialData:
    
    def __init__(self,
        cnpj_root: str = None,
        limit: str = None,
        maturity: str = None,
        in_open: str = None,
        margin: str = None,
        overdue_nfs: str = None,
        fbl5n_table: DataFrame = None
    ) -> None:
        self.cnpj_root = cnpj_root
        self.limit = limit
        self.maturity = maturity
        self.in_open = in_open
        self.margin = margin
        self.overdue_nfs = overdue_nfs
        self.fbl5n_table = fbl5n_table
    
    def subtract_margin(self, value: str) -> None:
        if self.margin != "Sem margem disponível.":
            self.margin = float(self.margin) - float(value)
