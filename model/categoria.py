from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from typing import Union

from  model import Base

class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), unique=True)

    despesa = Column(Integer, ForeignKey("despesa.pk_despesa"), nullable=False)

    def __init__(self, nome:str):
        """
        Cria uma categoria de gasto

        Arguments:
            nome: o nome de uma categoria que é única.
        """
        self.nome = nome