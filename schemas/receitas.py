from pydantic import BaseModel
from typing import Optional, List
from model.receitas import Receita

class ReceitaSchema(BaseModel):
    """ Define como uma nova receita a ser inserida deve ser representada
    """
    descricao: str = "Salário"
    valor: float = 3852.50

class ReceitaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    descricao: str = "Teste"

class ListagemReceitaSchema(BaseModel):
    """ Define como uma listagem de receitas será retornada.
    """
    receitas:List[ReceitaSchema]

def apresenta_receitas(receitas: List[Receita]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for receita in receitas:
        result.append({
            "descricao": receita.descricao,
            "valor": receita.valor,
        })

    return {"receitas": result}