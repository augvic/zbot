from src.infrastructure.databases.production.models import Registration
from src.infrastructure.databases.production.models import database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path

class RegistrationsClient:
    
    def __init__(self):
        BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), "../../../../storage/.databases"))
        url = f"sqlite:///{BASE_DIR}/production.db"
        self.engine = create_engine(url, echo=True, connect_args={"timeout": 30})
        self.session_construct = sessionmaker(bind=self.engine)
        database.metadata.create_all(self.engine)
    
    def create(self,
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
        tax_regime: str,
        comission_receipt: str,
        status: str,
        registration_date_hour: str,
        charge_date_hour: str,
        federal_revenue_consult_date: str,
        doc_resent: str,
        client_type: str,
        suggested_limit: str,
        seller: str,
        cpf: str,
        cpf_person: str,
    ) -> None:
        session = self.session_construct()
        to_create = Registration(
            cnpj=cnpj,
            opening=opening,
            company_name=company_name,
            trade_name=trade_name,
            legal_nature=legal_nature,
            legal_nature_id=legal_nature_id,
            registration_status=registration_status,
            street=street,
            number=number,
            complement=complement,
            neighborhood=neighborhood,
            pac=pac,
            city=city,
            state=state,
            fone=fone,
            email=email,
            tax_regime=tax_regime,
            comission_receipt=comission_receipt,
            status=status,
            registration_date_hour=registration_date_hour,
            charge_date_hour=charge_date_hour,
            federal_revenue_consult_date=federal_revenue_consult_date,
            doc_resent=doc_resent,
            client_type=client_type,
            suggested_limit=suggested_limit,
            seller=seller,
            cpf=cpf,
            cpf_person=cpf_person
        )
        session.add(to_create)
        session.commit()
        session.close()
    
    def read(self, cnpj: str) -> Registration | None:
        session = self.session_construct()
        return session.query(Registration).filter(Registration.cnpj == cnpj).first()
        
    def read_all(self) -> list[Registration]:
        session = self.session_construct()
        return session.query(Registration).all()
    
    def update(self,
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
        tax_regime: str,
        comission_receipt: str,
        status: str,
        registration_date_hour: str,
        charge_date_hour: str,
        federal_revenue_consult_date: str,
        doc_resent: str,
        client_type: str,
        suggested_limit: str,
        seller: str,
        cpf: str,
        cpf_person: str
    ) -> None:
        session = self.session_construct()
        to_update = session.query(Registration).filter(Registration.cnpj == cnpj).first()
        if to_update:
            if opening:
                to_update.opening = opening
            if company_name:
                to_update.company_name = company_name
            if trade_name:
                to_update.trade_name = trade_name
            if legal_nature:
                to_update.legal_nature = legal_nature
            if legal_nature_id:
                to_update.legal_nature_id = legal_nature_id
            if registration_status:
                to_update.registration_status = registration_status
            if street:
                to_update.street = street
            if number:
                to_update.number = number
            if complement:
                to_update.complement = complement
            if neighborhood:
                to_update.neighborhood = neighborhood
            if pac:
                to_update.pac = pac
            if city:
                to_update.city = city
            if state:
                to_update.state = state
            if fone:
                to_update.fone = fone
            if email:
                to_update.email = email
            if tax_regime:
                to_update.tax_regime = tax_regime
            if comission_receipt:
                to_update.comission_receipt = comission_receipt
            if status:
                to_update.status = status
            if registration_date_hour:
                to_update.registration_date_hour = registration_date_hour
            if charge_date_hour:
                to_update.charge_date_hour = charge_date_hour
            if federal_revenue_consult_date:
                to_update.federal_revenue_consult_date = federal_revenue_consult_date
            if doc_resent:
                to_update.doc_resent = doc_resent
            if client_type:
                to_update.opening = client_type
            if suggested_limit:
                to_update.suggested_limit = suggested_limit
            if seller:
                to_update.seller = seller
            if cpf:
                to_update.cpf = cpf
            if cpf_person:
                to_update.cpf_person = cpf_person
            session.commit()
        session.close()
    
    def delete(self, cnpj: str) -> None:
        session = self.session_construct()
        to_delete = session.query(Registration).filter(Registration.cnpj == cnpj).first()
        session.delete(to_delete)
        session.commit()
        session.close()
