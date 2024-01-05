from sqlalchemy import Column, Integer, String, DateTime, Boolean, func, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Merce(Base):
    __tablename__ = 'merce'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(32), nullable=False)
    descrizione = Column(String(255))

    def __init__(self, tipo, descrizione):
        self.tipo = tipo
        self.descrizione = descrizione

    def __json__(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'descrizione': self.descrizione
        }