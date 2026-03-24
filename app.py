from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Receita, Despesa
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
receita_tag = Tag(name="Receita", description="Adição, visualização e remoção de receitas à base")
despesa_tag = Tag(name="Despesa", description="Adição, visualização e remoção de despesas à base")
categoria_tag = Tag(name="Categoria", description="Adição, visualização e remoção de categorias à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/despesa', tags=[despesa_tag],
          responses={"200": DespesaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_despesa(form: DespesaSchema):
    """Adiciona uma nova Despesa à base de dados

    Retorna uma representação das despesas e categorias associadas.
    """
    despesa = Despesa(
        descricao=form.descricao,
        valor=form.valor
    )
    try:
        # criando conexão com a base
        session = Session()
        # adicionando despesa
        session.add(despesa)
        # efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionando despesa de descricao: '{despesa.descricao}'")
        return apresenta_despesa(despesa), 200

    except Exception as e:
        # caso um erro fora do previsto
        print(e)
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar despesa '{despesa.descricao}', {error_msg}")
        return {"message": error_msg}, 400

@app.get('/despesas', tags=[despesa_tag],
          responses={"200": ListagemDespesaSchema, "404": ErrorSchema})
def get_despesas():
    """Faz a busca por todas as despesas cadastradas

    Retorna uma representação da listagem de despesas.
    """
    logger.debug(f"Coletando despesas")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    despesas = session.query(Despesa).all()

    if not despesas:
        # se não há despesas cadastrados
        return {"despesas": []}, 200
    else:
        logger.debug(f"%d despesas econtradas" % len(despesas))
        # retorna a representação de despesa
        print(despesas)
        return apresenta_despesas(despesas), 200
    
@app.get('/despesa', tags=[despesa_tag],
         responses={"200": DespesaViewSchema, "404": ErrorSchema})
def get_despesa(query: DespesaBuscaSchema):
    """Faz a busca por uma Despesa a partir da descrição da despesa ou do id

    Retorna uma representação da despesa.
    """
    if not query.descricao and not query.id:
        error_msg = "É necessário informar ao menos um parâmetro de busca :/"
        logger.warning(f"Erro ao deletar despesa, {error_msg}")
        return {"message": error_msg}, 400
    despesa_descricao = unquote(unquote(query.descricao)) if query.descricao else None
    despesa_id = query.id
    print(despesa_descricao)
    logger.debug(f"Coletando dados sobre despesa #{despesa_descricao}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    if despesa_id is not None:
        despesa = session.query(Despesa).filter(Despesa.id == despesa_id).first()
    elif despesa_descricao:
        despesa = session.query(Despesa).filter(Despesa.descricao == despesa_descricao).first()

    if despesa:
        logger.debug(f"Despesa encontrada: '{despesa.descricao}'")
        # retorna a representação de despesa
        return apresenta_despesa(despesa), 200
    else:
        # se a despesa não foi encontrada
        error_msg = "Despesa não encontrada na base :/"
        logger.warning(f"Erro ao buscar despesa #'{despesa_descricao}', {error_msg}")
        return {"message": error_msg}, 404
    

@app.delete('/despesa', tags=[despesa_tag],
          responses={"200": DespesaDelSchema, "404": ErrorSchema})
def del_despesa(query: DespesaBuscaSchema):
    """Deleta uma despesa a partir da descrição ou do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    if not query.descricao and not query.id:
        error_msg = "É necessário informar ao menos um parâmetro de busca :/"
        logger.warning(f"Erro ao deletar despesa, {error_msg}")
        return {"message": error_msg}, 400
    despesa_descricao = unquote(unquote(query.descricao)) if query.descricao else None
    despesa_id = query.id
    print(despesa_descricao)
    logger.debug(f"Deletando dados sobre produto #{despesa_descricao}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    if despesa_id is not None:
        count = session.query(Despesa).filter(Despesa.id == despesa_id).delete()
    elif despesa_descricao:
        count = session.query(Despesa).filter(Despesa.descricao == despesa_descricao).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        if despesa_id is not None:
            logger.debug(f"Deletado despesa #{despesa_id}")
            return {"message": "Despesa removida", "id": despesa_id}
        if despesa_descricao is not None and despesa_id is None:
            logger.debug(f"Deletado despesa #{despesa_descricao}")
            return {"message": "Despesa removida", "descricao": despesa_descricao}
    else:
        # se a despesa não foi encontrada
        error_msg = "Despesa não encontrada na base :/"
        logger.warning(f"Erro ao deletar despesa #'{despesa_descricao}', {error_msg}")
        return {"message": error_msg}, 404

@app.post('/receita', tags=[receita_tag],
          responses={})
def add_receita(form: ReceitaSchema):
    """Adiciona uma nova Receita à base de dados

    Retorna uma representação das receitas.
    """
    receita = Receita(
        descricao=form.descricao,
        valor=form.valor
    )
    try:
        # criando conexão com a base
        session = Session()
        # adicionando receita
        session.add(receita)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionando receita de descricao: '{receita.descricao}'")
        return apresenta_receita(receita), 200

    except Exception as e:
        # caso um erro fora do previsto
        print(e)
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar receita '{receita.descricao}', {error_msg}")
        return {"mesage": error_msg}, 400
    
@app.get('/receita', tags=[receita_tag],
          responses={})
def get_receitas():
    """Faz a busca por todas as receitas cadastradas

    Retorna uma representação da listagem de receitas.
    """
    logger.debug(f"Coletando receitas")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    receitas = session.query(Receita).all()

    if not receitas:
        # se não há receitas cadastrados
        return {"receitas": []}, 200
    else:
        logger.debug(f"%d receitas econtradas" % len(receitas))
        # retorna a representação de receita
        print(receitas)
        return apresenta_receitas(receitas), 200
    
@app.delete('/receita', tags=[receita_tag],
          responses={})
def del_receita(query: ReceitaBuscaSchema):
    """Deleta uma receita a partir da descrição informada

    Retorna uma mensagem de confirmação da remoção.
    """
    receita_descricao = unquote(unquote(query.descricao))
    print(receita_descricao)
    logger.debug(f"Deletando dados sobre a receita #{receita_descricao}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Receita).filter(Receita.descricao == receita_descricao).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletada receita #{receita_descricao}")
        return {"message": "Receita removida", "id": receita_descricao}
    else:
        # se a receita não foi encontrada
        error_msg = "Receita não encontrada na base :/"
        logger.warning(f"Erro ao deletar receita #'{receita_descricao}', {error_msg}")
        return {"message": error_msg}, 404

@app.post('/categoria', tags=[categoria_tag],
          responses={})
def add_categoria():
    """Adiciona de uma nova categoria à um produtos cadastrado na base identificado pelo id

    Retorna uma representação dos produtos e comentários associados.
    """

@app.get('/categoria', tags=[categoria_tag],
          responses={})
def get_categorias():
    """Faz a busca por todos os Produto cadastrados

    Retorna uma representação da listagem de produtos.
    """

@app.delete('/categoria', tags=[categoria_tag],
          responses={})
def delete_categoria():
    """Deleta um Produto a partir do nome de produto informado

    Retorna uma mensagem de confirmação da remoção.
    """
