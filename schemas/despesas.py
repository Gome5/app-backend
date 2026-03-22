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
        feita apenas com base no nome do produto.
    """
    descricao: str = "Teste"


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

class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": produto.quantidade,
        "valor": produto.valor,
        "total_cometarios": len(produto.comentarios),
        "comentarios": [{"texto": c.texto} for c in produto.comentarios]
    }
