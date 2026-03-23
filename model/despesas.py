from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model.base import Base
from model.categoria import Categoria

class Despesa(Base):
    __tablename__ = 'despesa'

    id = Column("pk_despesa", Integer, primary_key=True)
    descricao = Column(String(50))
    valor = Column(Float)
    data_entrada = Column(DateTime, default=datetime.now())
    categoria_id = Column(Integer, ForeignKey("categoria.id"), nullable=True)

    # Definição do relacionamento entre a despesa e a categoria.
    # Essa relação é implicita, não está salva na tabela 'despesas',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    categoria = relationship("Categoria")

    def __init__(self, descricao: str, valor: float, categoria: Categoria = None,
             data_entrada: Union[DateTime, None] = None):
        """
        Cria uma receita

        Arguments:
            descricao: descricao do gasto (origem).
            valor: valor da entrada
            categoria: categoria que se adequa o gasto
            data_entrada: data de quando o valor foi inserido à base
        """
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria

        # se não for informada, será o data exata da inserção no banco
        if data_entrada:
            self.data_entrada = data_entrada