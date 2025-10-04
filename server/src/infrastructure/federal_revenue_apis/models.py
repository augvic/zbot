class FederalRevenueData:
    
    def __init__(self,
        cnpj: str,
        opening: str,
        company_name: str,
        trade_name: str,
        legal_nature: str,
        legal_nature_id: str,
        registration_status: str,
        street: str,
        number: str,
        complement: str,
        neighborhood: str,
        pac: str,
        city: str,
        state: str,
        fone: str,
        email: str,
        state_registrations: list[dict[str, str]],
        suframa_registrations: list[dict[str, str]],
        tax_regime: dict[str, str] | list[dict[str, str]],
        ncea: list[dict[str, str]],
        comission_receipt: str
    ) -> None:
        self.cnpj = cnpj
        self.opening = opening
        self.company_name = company_name
        self.trade_name = trade_name
        self.legal_nature = legal_nature
        self.legal_nature_id = legal_nature_id
        self.registration_status = registration_status
        self.street = street
        self.number = number
        self.complement = complement
        self.neighborhood = neighborhood
        self.pac = pac
        self.city = city
        self.state = state
        self.fone = fone
        self.email = email
        self.state_registrations = state_registrations
        self.suframa_registrations = suframa_registrations
        self.tax_regime = tax_regime
        self.ncea = ncea
        self.comission_receipt = comission_receipt
