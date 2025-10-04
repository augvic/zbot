from typing import TypedDict

class Cidade(TypedDict):
    
    nome: str
    sigla: str

class Estado(TypedDict):
    
    sigla: str

class Simples(TypedDict):
    
    simples: str

class InscricaoEstadual(TypedDict):
    
    inscricao_estadual: str
    ativo: str

class InscricaoSuframa(TypedDict):
    
    inscricao_suframa: str
    ativo: str

class Estabelecimento(TypedDict):
    
    cnpj: str
    data_inicio_atividade: str
    nome_fantasia: str | None
    situacao_cadastral: str
    logradouro: str
    numero: str | None
    complemento: str | None
    bairro: str
    cep: str
    cidade: Cidade
    estado: Estado
    ddd1: str
    telefone1: str
    email: str | None
    inscricoes_estaduais: list[InscricaoEstadual]
    inscricoes_suframa: list[InscricaoSuframa]
    regimes_tributarios: list[dict[str, str]]
    atividades_secundarias: list[dict[str, str]]

class NaturezaJuridica(TypedDict):
    
    descricao: str
    id: str

class ResponseData(TypedDict):
    
    estabelecimento: Estabelecimento
    razao_social: str
    natureza_juridica: NaturezaJuridica
    simples: Simples

class CleanedResponse(TypedDict):
    
    cnpj: str
    data_inicio_atividade: str
    razao_social: str
    nome_fantasia: str
    situacao_cadastral: str
    natureza_juridica: str
    natureza_juridica_id: str
    regime_tributario: dict[str, str] | list[dict[str, str]]
    cnaes: list[dict[str, str]]
    recebimento_comissao: str
    logradouro: str
    numero: str
    complemento: str
    bairro: str
    cep: str
    cidade: str
    estado: str
    telefone: str
    email: str
    inscricoes_estaduais: list[dict[str, str]]
    inscricoes_suframa: list[dict[str, str]]
