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
        feita com base na descrição ou do id da despesa.
    """
    id: Optional[int] = None
    descricao: Optional[str] = None

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
            "id": despesa.id,
            "descricao": despesa.descricao,
            "valor": despesa.valor,
            "data_entrada": despesa.data_entrada.strftime("%d/%m/%Y")
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
    descrição: Optional[str] = None
    id: Optional[int] = None

class DespesaViewSchema(BaseModel):
    """ Define como uma despesa será retornado: despesa.
    """
    id: int = 1
    descricao: str = "Compra no Shopping"
    valor: float = 125.50