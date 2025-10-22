import requests

url = "http://127.0.0.1:5000/registrations"

files = {
    "article_association_doc": open(r"C:\Users\72776\Downloads\doc.pdf", "rb"),
}

data = {
    "cnpj": "23414622000161",
    "seller": "RAQUEL",
    "email": "jaimesp79@hotmail.com",
    "cpf": "957.992.146-68",
    "cpf_person": "Jaime",
    "tax_regime": "Simples",
    "suggested_limit": "",
    "client_type": "Revenda"
}

response = requests.post(url, data=data, files=files)
