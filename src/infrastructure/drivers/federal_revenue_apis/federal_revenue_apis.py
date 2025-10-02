from .models import *
from .errors import *
from datetime import datetime
from requests import get
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from os import getenv
from re import sub
from unicodedata import normalize
from dotenv import load_dotenv

class PositivoFederalRevenueApi:
    
    def _requisition_to_api(self, cnpj: str) -> dict:
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
        if isinstance(string, str):
            cleaned_string = normalize("NFKD", string).encode("ASCII", "ignore").decode("ASCII")
            cleaned_string = cleaned_string.upper()
            return cleaned_string
        else:
            return string
    
    def _clean_response_data(self, response: dict) -> dict:
        cleaned_response = {}
        cleaned_response["cnpj"] = response["estabelecimento"]["cnpj"]
        cleaned_response["data_inicio_atividade"] = datetime.strptime(response["estabelecimento"]["data_inicio_atividade"], "%Y-%m-%d").strftime("%d/%m/%Y") 
        cleaned_response["razao_social"] = self._clean_str(response["razao_social"])
        cleaned_response["nome_fantasia"] = self._clean_str(response["estabelecimento"]["nome_fantasia"]) if response["estabelecimento"]["nome_fantasia"] else "-"
        cleaned_response["natureza_juridica"] = self._clean_str(response["natureza_juridica"]["descricao"])
        cleaned_response["natureza_juridica_id"] = response["natureza_juridica"]["id"]
        cleaned_response["situacao_cadastral"] = self._clean_str(response["estabelecimento"]["situacao_cadastral"])
        cleaned_response["logradouro"] = self._clean_str(response["estabelecimento"]["logradouro"])
        cleaned_response["numero"] = response["estabelecimento"]["numero"] if response["estabelecimento"]["numero"] else "-"
        cleaned_response["complemento"] = sub(r"\s+", " ", self._clean_str(response["estabelecimento"]["complemento"])) if response["estabelecimento"]["complemento"] else "-"
        cleaned_response["bairro"] = self._clean_str(response["estabelecimento"]["bairro"])
        cleaned_response["cep"] = f"{response["estabelecimento"]["cep"][:5]}-{response["estabelecimento"]["cep"][5:]}"
        cleaned_response["cidade"] = self._clean_str(response["estabelecimento"]["cidade"]["nome"])
        cleaned_response["estado"] = self._clean_str(response["estabelecimento"]["estado"]["sigla"])
        cleaned_response["telefone"] = f"{response["estabelecimento"]["ddd1"]}{response["estabelecimento"]["telefone1"]}"
        cleaned_response["email"] = self._clean_str(response["estabelecimento"]["email"]) if response["estabelecimento"]["email"] else "-"
        cleaned_response["inscricoes_estaduais"] = [
            {
                "state_registration": inscricao['inscricao_estadual'],
                "status": ('HABILITADA' if inscricao['ativo'] else 'NÃO HABILITADA')
            }
            for inscricao in response["estabelecimento"]["inscricoes_estaduais"]
        ] if response["estabelecimento"]["inscricoes_estaduais"] else [{"state_registration": "ISENTO", "status": "-"}]
        cleaned_response["inscricoes_suframa"] = [
            {
                "suframa_registration": inscricao['inscricao_suframa'],
                "status": ('HABILITADA' if inscricao['ativo'] else 'NÃO HABILITADA')
            }
            for inscricao in response["estabelecimento"]["inscricoes_suframa"]
        ] if response["estabelecimento"]["inscricoes_suframa"] else [{"suframa_registration": "ISENTO", "status": "-"}]
        try:
            isSimples = response["simples"]["simples"]
        except:
            isSimples = "Não"
        if isSimples == "Sim":
            cleaned_response["regime_tributario"] = {"regime_tributario": "SIMPLES", "ano": "-"}
        else:
            cleaned_response["regime_tributario"] = [
                {
                    "ano": regime["ano"],
                    "regime_tributario": regime["regime_tributario"]
                }
                for regime in response["estabelecimento"]["regimes_tributarios"]
            ]
            if cleaned_response["regime_tributario"]:
                cleaned_response["regime_tributario"] = max(cleaned_response["regime_tributario"], key=lambda x: x["ano"])
            else:
                cleaned_response["regime_tributario"] = {"regime_tributario": "LUCRO", "ano": "-"}
        cleaned_response["cnaes"] = [
            {
                "code": cnae["classe"],
                "description": cnae["descricao"]
            }
            for cnae in response["estabelecimento"]["atividades_secundarias"]
        ]
        cnaes_comissao = ["45.12-9", "45.30-7", "45.42-1", "46.11-7", "46.12-5", "46.13-3", "46.14-1", "46.15-0", "46.16-8", "46.17-6", "46.18-4", "46.19-2", "66.19-3"]
        cleaned_response["recebimento_comissao"] = "NÃO OK"
        for cnae in cleaned_response["cnaes"]:
            if cnae["code"] in cnaes_comissao:
                cleaned_response["recebimento_comissao"] = "OK"
        return cleaned_response
    
    def get_data(self, cnpj: str) -> FederalRevenueData:
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
