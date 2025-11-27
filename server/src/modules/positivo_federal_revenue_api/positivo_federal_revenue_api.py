from datetime import datetime
from requests import get
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from os import getenv
from re import sub
from unicodedata import normalize
from dotenv import load_dotenv
from .models import *
from .errors import RequestError, RequestResponseError
from .types import *

class PositivoFederalRevenueApi:
    
    def _requisition_to_api(self, cnpj: str) -> ResponseData:
        load_dotenv()
        disable_warnings(InsecureRequestWarning)
        url = f"https://comercial.cnpj.ws/cnpj/{cnpj}"
        headers = {
            "x_api_token": getenv("API_KEY")
        }
        try:
            response = get(url=url, headers=headers, verify=False)
        except Exception as error:
            raise RequestError(error)
        if response.status_code == 200:
            return response.json()
        else:
            raise RequestResponseError(response)
    
    def _clean_str(self, string: str) -> str:
        try:
            cleaned_string = normalize("NFKD", string).encode("ASCII", "ignore").decode("ASCII")
            cleaned_string = cleaned_string.upper()
            return cleaned_string
        except:
            return "-"
    
    def _clean_response_data(self, response: ResponseData) -> CleanedResponse:
        try:
            isSimples = response["simples"]["simples"]
        except:
            isSimples = "Não"
        if isSimples == "Sim":
            regime_tributario = "SIMPLES"
        else:
            regime_tributario = [
                {
                    "ano": regime["ano"],
                    "regime_tributario": regime["regime_tributario"]
                }
                for regime in response["estabelecimento"]["regimes_tributarios"]
            ]
            if regime_tributario:
                regime_tributario = max(regime_tributario, key=lambda x: x["ano"])
                regime_tributario = regime_tributario["regime_tributario"]
            else:
                regime_tributario = "LUCRO"
        cnaes_comissao = ["45.12-9", "45.30-7", "45.42-1", "46.11-7", "46.12-5", "46.13-3", "46.14-1", "46.15-0", "46.16-8", "46.17-6", "46.18-4", "46.19-2", "66.19-3"]
        recebimento_comissao = "NÃO OK"
        for cnae in response["estabelecimento"]["atividades_secundarias"]:
            if cnae["classe"] in cnaes_comissao:
                recebimento_comissao = "OK"
        cleaned_response: CleanedResponse = {
            "cnpj": response["estabelecimento"]["cnpj"],
            "data_inicio_atividade": datetime.strptime(response["estabelecimento"]["data_inicio_atividade"], "%Y-%m-%d").strftime("%d/%m/%Y"),
            "razao_social": self._clean_str(response["razao_social"]),
            "nome_fantasia": self._clean_str(response["estabelecimento"]["nome_fantasia"]) if response["estabelecimento"]["nome_fantasia"] else "-",
            "natureza_juridica": self._clean_str(response["natureza_juridica"]["descricao"]),
            "natureza_juridica_id": response["natureza_juridica"]["id"],
            "situacao_cadastral": self._clean_str(response["estabelecimento"]["situacao_cadastral"]),
            "logradouro": self._clean_str(response["estabelecimento"]["logradouro"]),
            "numero": response["estabelecimento"]["numero"] if response["estabelecimento"]["numero"] else "-",
            "complemento": sub(r"\s+", " ", self._clean_str(response["estabelecimento"]["complemento"])) if isinstance(response["estabelecimento"]["complemento"], str) else "-",
            "bairro": self._clean_str(response["estabelecimento"]["bairro"]),
            "cep": f"{response["estabelecimento"]["cep"][:5]}-{response["estabelecimento"]["cep"][5:]}",
            "cidade": self._clean_str(response["estabelecimento"]["cidade"]["nome"]),
            "estado": self._clean_str(response["estabelecimento"]["estado"]["sigla"]),
            "telefone": f"{response["estabelecimento"]["ddd1"]}{response["estabelecimento"]["telefone1"]}",
            "email": self._clean_str(response["estabelecimento"]["email"]) if response["estabelecimento"]["email"] else "-",
            "inscricoes_estaduais": [
                {
                    "state_registration": inscricao['inscricao_estadual'],
                    "status": ('HABILITADA' if inscricao['ativo'] else 'NÃO HABILITADA')
                }
                for inscricao in response["estabelecimento"]["inscricoes_estaduais"]
            ] if response["estabelecimento"]["inscricoes_estaduais"] else [{"state_registration": "ISENTO", "status": "-"}],
            "inscricoes_suframa": [
                {
                    "suframa_registration": inscricao['inscricao_suframa'],
                    "status": ('HABILITADA' if inscricao['ativo'] else 'NÃO HABILITADA')
                }
                for inscricao in response["estabelecimento"]["inscricoes_suframa"]
            ] if response["estabelecimento"]["inscricoes_suframa"] else [{"suframa_registration": "ISENTO", "status": "-"}],
            "regime_tributario": regime_tributario,
            "cnaes": [
                {
                    "code": cnae["classe"],
                    "description": cnae["descricao"]
                }
                for cnae in response["estabelecimento"]["atividades_secundarias"]
            ],
            "recebimento_comissao": recebimento_comissao
        }
        return cleaned_response
    
    def get_data(self, cnpj: str) -> FederalRevenueData:
        try:
            response = self._requisition_to_api(cnpj=cnpj)
            response = self._clean_response_data(response=response)
            return FederalRevenueData(
                cnpj=response["cnpj"],
                opening=response["data_inicio_atividade"],
                company_name=response["razao_social"],
                trade_name=response["nome_fantasia"],
                legal_nature=response["natureza_juridica"],
                legal_nature_id=response["natureza_juridica_id"],
                registration_status=response["situacao_cadastral"],
                street=response["logradouro"],
                number=response["numero"],
                complement=response["complemento"],
                neighborhood=response["bairro"],
                pac=response["cep"],
                city=response["cidade"],
                state=response["estado"],
                fone=response["telefone"],
                email=response["email"],
                state_registrations=response["inscricoes_estaduais"],
                suframa_registrations=response["inscricoes_suframa"],
                tax_regime=response["regime_tributario"],
                ncea=response["cnaes"],
                comission_receipt = response["recebimento_comissao"]
            )
        except Exception as error:
            raise Exception(f"Error in (PositivoFederalRevenueApi) component in (get_data) method: {error}.")
