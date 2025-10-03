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

class Partner:
    
    def __init__(self,
        key: str,
        code: str
    ) -> None:
        self.key = key
        self.code = code

class Comission:
    
    def __init__(self,
        key: str,
        code: str,
        percentage: str
    ) -> None:
        self.key = key
        self.code = code
        self.percentage = percentage

class Item:
    
    def __init__(self,
        sku: str,
        quantity: str,
        center: str,
        deposit: str,
        guarantee: str,
        over: str,
        unit_value: float,
        total_value: float,
        is_parent_item: bool
    ) -> None:
        self.sku = sku
        self.quantity = quantity
        self.center = center
        self.deposit = deposit
        self.guarantee = guarantee
        self.over = over
        self.unit_value = unit_value
        self.total_value = total_value
        self.is_parent_item = is_parent_item

class Order:
    
    def __init__(self,
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
        items: list[Item],
        partners: list[Partner],
        comissions: list[Comission]
    ) -> None:
        self.doc_type = doc_type
        self.organization = organization
        self.channel = channel
        self.office = office
        self.team = team
        self.order_name = order_name
        self.issuer = issuer
        self.receiver = receiver
        self.payment_condition = payment_condition
        self.incoterm = incoterm
        self.reason = reason
        self.table = table
        self.expedition = expedition
        self.payment_way = payment_way
        self.additional_data = additional_data
        self.items = items
        self.partners = partners
        self.comissions = comissions
