from requests import Session
import json

url = "http://127.0.0.1:5000/"
login_headers = {
    "Content-Type": "application/json"
}
login_body = {
    "user": "72776",
    "password": "AHVH#72776"
}
files = {
    "article_association_doc": open(r"C:\Users\72776\Downloads\doc.pdf", "rb"),
    "bank_doc": "-"
}
new_registration_data = {
    "cnpj": "36761251000136",
    "seller": "RAQUEL",
    "email": "jaimesp79@hotmail.com",
    "cpf": "957.992.146-68",
    "cpf_person": "Jaime",
    "tax_regime": "Simples",
    "suggested_limit": "-",
    "client_type": "Revenda"
}
session = Session()
session.post(f"{url}/login", headers=login_headers, data=json.dumps(login_body))
response = session.post(f"{url}/registrations", data=new_registration_data, files=files)
