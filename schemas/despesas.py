from pydantic import BaseModel
from typing import Optional, List
from model.despesas import Despesa

class DespesaSchema(BaseModel):
    """ Define como uma nova despesa a ser inserido deve ser representado
    """
    descricao: str = "Compra no Shopping"
    valor: float = 259.50


class DespesaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base na descrição da despesa.
    """
    descricao: str = "Compra no Shopping"


class ListagemDespesaSchema(BaseModel):
    """ Define como uma listagem de despesas será retornada.
    """
    despesas:List[DespesaSchema]


def apresenta_despesas(despesas: List[Despesa]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for despesa in despesas:
        result.append({
            "descricao": despesa.descricao,
            "valor": despesa.valor,
        })

    return {"despesas": result}


def apresenta_despesa(despesa: Despesa):
    """ Retorna uma representação da despesa seguindo o schema definido em
        DespesaViewSchema.
    """
    return {
        "id": despesa.id,
        "descricao": despesa.descricao,
        "valor": despesa.valor,
    }

class DespesaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    descricao: str

class DespesaViewSchema(BaseModel):
    """ Define como uma despesa será retornado: despesa + categoria.
    """
    id: int = 1
    descricao: str = "Compra no Shopping"
    valor: float = 125.50