class Comission:
    
    def __init__(self,
        key: str,
        code: str,
        percentage: str,
    ) -> None:
        self.key = key
        self.code = code
        self.percentage = percentage

class Item:
    
    def __init__(self,
        sku: str,
        center: str,
        unit_value: str,
    ) -> None:
        self.sku = sku
        self.center = center
        self.unit_value = unit_value

class Partner:
    
    def __init__(self,
        key: str,
        code: str
    ) -> None:
        self.key = key
        self.code = code

class Order:
    
    def __init__(self,
        date: str = "",
        doc_type: str = "",
        organization: list[str] = [],
        channel: str = "",
        office: str = "",
        team: str = "",
        order_name: str = "",
        order_site: str = "",
        order_erp: str = "",
        resaler_name: str = "",
        receiver_name: str = "",
        resaler_erp: str = "",
        receiver_erp: str = "",
        receiver_type: str = "",
        payment_condition: str = "",
        incoterm: str = "",
        reason: str = "",
        table: str = "",
        expedition: list[str] = [],
        payment_way: str = "",
        additional_data: str | None = "",
        comissions: list[Comission] = [],
        partners: list[Partner] = [],
        items: list[Item] = [],
        receiver_cnpj_cpf: str = "",
        receiver_cnpj_root: str = "",
        total_value: str = "",
        status_site: str = "",
        seller: str = "",
        centers: list[str] = [],
        over: str = "",
        comission_percentage: str = ""
    ) -> None:
        self.date = date
        self.doc_type = doc_type
        self.organization = organization
        self.channel = channel
        self.office = office
        self.team = team
        self.order_name = order_name
        self.order_site = order_site
        self.order_erp = order_erp
        self.resaler_name = resaler_name
        self.receiver_name = receiver_name
        self.resaler_erp = resaler_erp
        self.receiver_erp = receiver_erp
        self.receiver_type = receiver_type
        self.payment_condition = payment_condition
        self.incoterm = incoterm
        self.reason = reason
        self.table = table
        self.expedition = expedition
        self.payment_way = payment_way
        self.additional_data = additional_data
        self.comissions = comissions
        self.partners = partners
        self.items = items
        self.receiver_cnpj_cpf = receiver_cnpj_cpf
        self.receiver_cnpj_root = receiver_cnpj_root
        self.total_value = total_value
        self.status_site = status_site
        self.seller = seller
        self.centers = centers
        self.over = over
        self.comission_percentage = comission_percentage
