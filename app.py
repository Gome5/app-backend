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
produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos à base")
comentario_tag = Tag(name="Comentario", description="Adição de um comentário à um produtos cadastrado na base")
categoria_tag = Tag(name="Categoria", description="")
receita_tag = Tag(name="Receita", description="")
despesa_tag = Tag(name="Despesa", description="")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

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

@app.post('/despesa', tags=[despesa_tag],
          responses={})
def add_despesa(form: DespesaSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
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
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionando despesa de descricao: '{despesa.descricao}'")
        return apresenta_despesas(despesa), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar produto '{despesa.descricao}', {error_msg}")
        return {"mesage": error_msg}, 400

@app.get('/despesa', tags=[despesa_tag],
          responses={})
def get_despesas():
    """Faz a busca por todos os Produto cadastrados

    Retorna uma representação da listagem de produtos.
    """
    logger.debug(f"Coletando depesas")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    despesas = session.query(Despesa).all()

    if not despesas:
        # se não há despesas cadastrados
        return {"despesas": []}, 200
    else:
        logger.debug(f"%d rodutos econtrados" % len(despesas))
        # retorna a representação de despesa
        print(despesas)
        return apresenta_despesas(despesas), 200
    

@app.delete('/despesa', tags=[despesa_tag],
          responses={})
def del_despesa(query: DespesaBuscaSchema):
    """Deleta um Produto a partir do nome de produto informado

    Retorna uma mensagem de confirmação da remoção.
    """
    despesa_descricao = unquote(unquote(query.descricao))
    print(despesa_descricao)
    logger.debug(f"Deletando dados sobre produto #{despesa_descricao}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Despesa).filter(Despesa.descricao == despesa_descricao).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado produto #{despesa_descricao}")
        return {"mesage": "Produto removido", "id": despesa_descricao}
    else:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produto #'{despesa_descricao}', {error_msg}")
        return {"mesage": error_msg}, 404

