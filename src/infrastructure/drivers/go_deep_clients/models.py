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
        date: str = None,
        doc_type: str = None,
        organization: str = None,
        channel: str = None,
        office: str = None,
        team: str = None,
        order_name: str = None,
        order_site: str = None,
        order_erp: str = None,
        resaler_name: str = None,
        receiver_name: str = None,
        resaler_erp: str = None,
        receiver_erp: str = None,
        receiver_type: str = None,
        payment_condition: str = None,
        incoterm: str = None,
        reason: str = None,
        table: str | None = None,
        expedition: str = None,
        payment_way: str = None,
        additional_data: str | None = None,
        comissions: list[Comission] = None,
        partners: list[Partner] | None = None,
        items: list[Item] = None,
        receiver_cnpj_cpf: str = None,
        receiver_cnpj_root: str = None,
        total_value: str = None,
        status_site: str = None,
        seller: str = None,
        centers: str = None,
        over: str = None,
        comission_percentage: str = None
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
