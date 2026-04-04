from pydantic import BaseModel
from typing import Optional, List
from model.receitas import Receita

class ReceitaSchema(BaseModel):
    """ Define como uma nova receita a ser inserida deve ser representada
    """
    descricao: str = "Salário"
    valor: float = 3852.50
    data: Optional[str] = None

class ReceitaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    id: Optional[int] = None
    descricao: Optional[str] = None

class ListagemReceitaSchema(BaseModel):
    """ Define como uma listagem de receitas será retornada.
    """
    receitas:List[ReceitaSchema]

class ReceitaViewSchema(BaseModel):
    """ Define como uma receita será retornada.
    """
    id: int
    descricao: str
    valor: float
    data_entrada: Optional[str] = None

def apresenta_receitas(receitas: List[Receita]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for receita in receitas:
        result.append({
            "id": receita.id,
            "descricao": receita.descricao,
            "valor": receita.valor,
            "data_entrada": receita.data_entrada.strftime("%d/%m/%Y")
        })

    return {"receitas": result}

def apresenta_receita(receita: Receita):
    """ Retorna uma representação da receita seguindo o schema definido em
        ReceitaViewSchema.
    """
    return {
        "id": receita.id,
        "descricao": receita.descricao,
        "valor": receita.valor,
    }

class ReceitaDelSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a mensagem de confirmação
        da remoção de uma receita.
    """
    message: str
    id: Optional[int] = None
    descricao: Optional[str] = None