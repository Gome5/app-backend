from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model.base import Base

class Despesa(Base):
    __tablename__ = 'despesa'

    id = Column("pk_despesa", Integer, primary_key=True)
    descricao = Column(String(50))
    valor = Column(Float)
    data_entrada = Column(DateTime, default=datetime.now())

    def __init__(self, descricao: str, valor: float, 
             data_entrada: Union[DateTime, None] = None):
        """
        Cria uma receita

        Arguments:
            descricao: descricao do gasto (origem).
            valor: valor da entrada
            data_entrada: data de quando o valor foi inserido à base
        """
        self.descricao = descricao
        self.valor = valor

        # se não for informada, será o data exata da inserção no banco
        if data_entrada:
            self.data_entrada = data_entrada