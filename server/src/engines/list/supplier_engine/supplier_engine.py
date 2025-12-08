from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from requests import Session
from os import path, getenv
from datetime import datetime, timedelta
from dotenv import load_dotenv
import math
import sys
import pandas

from .models import Response

from typing import Any

class SupplierEngine:
    
    def __init__(self) -> None:
        disable_warnings(InsecureRequestWarning)
        load_dotenv()
        self.session = Session()
        self.pandas = pandas
        self.path = path
        self.sys = sys
        self.datetime = datetime
        self.timedelta = timedelta
        self.logged_in = False
    
    def _create_installments_list(self, installments: list[str], value: float) -> list[dict[str, str | int | float]]:
        installments_list = []
        date = self.datetime.now().date()
        length = len(installments)
        installment_value = round(value / length, 2)
        difference = math.ceil(((installment_value * length) - value) * 100) / 100
        for index in range(1, length + 1):
            date = date + self.timedelta(days=30)
            if date.day == 31:
                date.replace(day=30)
            if index == length:
                if difference > 0:
                    installment_value = installment_value - difference
                else:
                    installment_value = installment_value + abs(difference)
            installments_list.append({
                "numeroParcela": index,
                "dataVencimento": date.strftime("%Y-%m-%d"),
                "valorParcela": installment_value
            })
        return installments_list
    
    def _get_info_from_csv(self, installment_count: int, column_searched: str) -> Any:
        if getattr(self.sys, "frozen", False):
            base_path = self.path.join(self.path.dirname(self.sys.executable), "storage")
        else:
            base_path = self.path.join(self.path.dirname(__file__), "..", "..", "..", "..", "storage", ".csv")
        csv_path = self.path.abspath(self.path.join(base_path, "supplier.csv"))
        table = self.pandas.read_csv(csv_path, sep=";", encoding="utf-8")
        return table[table["Parcelas"] == installment_count][column_searched].to_list()
    
    def _get_transfer(self, installment_count: int) -> int:
        average_list = self._get_info_from_csv(installment_count, "Repasse")
        for element in average_list:
            average = int(element)
        return average
    
    def _get_fee(self, installment_count: int) -> str:
        fee_list = self._get_info_from_csv(installment_count, "Taxa")
        for element in fee_list:
            fee = str(element)
        return fee
    
    def login(self) -> None:
        try:
            response_login_1 = self.session.post("https://ppd-back.suppliercloudapis.com/ppd/oauth/login",
                json={
                    "app": ["ApiPpd"],
                    "codigoGrupo": "O019",
                    "codigoTokenMFA": "",
                    "email": getenv("SUPPLIER_EMAIL"),
                    "idMFARequest": "",
                    "manterConectado": False,
                    "password": getenv("SUPPLIER_PASSWORD"),
                    "termoUso": False
                },
                verify=False
            )
            response_login_dict_1 = response_login_1.json()
            id_mfa_request = response_login_dict_1.get("idMFARequest")
            self.session.post("https://ppd-back.suppliercloudapis.com/ppd/oauth/mfa",
                json={
                    "canalEnvioToken": "EMAIL",
                    "idMFARequest": id_mfa_request
                },
                verify=False
            )
            mfa_token = input("Informe o token: ")
            response_login_2 = self.session.post("https://ppd-back.suppliercloudapis.com/ppd/oauth/login",
                json={
                    "app": ["ApiPpd"],
                    "codigoGrupo": "O019",
                    "codigoTokenMFA": mfa_token,
                    "email": getenv("SUPPLIER_EMAIL"),
                    "idMFARequest": id_mfa_request,
                    "manterConectado": True,
                    "password": "",
                    "termoUso": False
                },
                verify=False
            )
            response_login_dict_2 = response_login_2.json()
            self.access_token = response_login_dict_2.get("access_token")
            self.logged_in = True
        except Exception as error:
            raise Exception(f"Error on (SupplierEngine) module on (login) method: {error}")
    
    def order_pre_autorization(self,
        cnpj_client: str,
        cnpj_positivo: str,
        order: str,
        payment_deadline: str,
        value: float
    ) -> Response:
        try:
            if not self.logged_in:
                raise Exception("Necessário logar na Supplier primeiro.")
            installments = payment_deadline.split("/")
            response = self.session.post("https://ppd-back.suppliercloudapis.com/ppd/preautorizacoes/O019",
                headers={
                    "Access_token": self.access_token
                },
                json={
                    "cnpjCpf": cnpj_client,
                    "cnpjParceiro": cnpj_positivo,
                    "codigoPreAutorizacao": "",
                    "dataPrimeiroVencimento": "",
                    "numeroPedido": order,
                    "numeroparcelas": len(installments),
                    "operacaoComJuros": False,
                    "parcelas": self._create_installments_list(installments, value),
                    "prazoRecebimentoParceiro": self._get_transfer(len(installments)),
                    "taxas": [{"tipoTaxa": "ANTECIPACAO", "valorTaxa": self._get_fee(len(installments))}],
                    "tipoRecebimentoParceiro": "3",
                    "tipoTransacao": "0",
                    "valorPreAutorizacao": value
                },
                verify=False
            )
            response_dict = response.json()
            if response_dict["mensagemRetorno"] == "Solicitação Efetuada com sucesso!":
                return Response(success=True, message=f"Valor: {response_dict["preAutorizacao"]["valorPreAutorizado"]}. Tempo de vigência: {self.datetime.strptime(response_dict["preAutorizacao"]["dataVigenciaPreAutorizacao"], "%Y-%m-%d").strftime("%d/%m/%Y")}.")
            elif response_dict["mensagemRetorno"] == "Não foram encontradas condições comerciais para os parâmetros informados.":
                return Response(success=False, message=f"Corpo da requisição é inválido.")
            else:
                return Response(success=False, message=f"Erro desconhecido: {response_dict}.")
        except Exception as error:
            raise Exception(f"❌ Error in (SupplierEngine) engine in (order_pre_authorization) method: {error}")