from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Include(Base):
    __tablename__ = 'include'

    id = Column(Integer, primary_key=True, autoincrement=True)
    operazione_id = Column(Integer, nullable=False)
    merce_id = Column(Integer, nullable=False)
    quantita = Column(Integer, nullable=False)

    def __init__(self, operazione_id, merce_id, quantita):
        self.operazione_id = operazione_id
        self.merce_id = merce_id
        self.quantita = quantita

    def __json__(self):
        return {
            'id': self.id,
            'operazione_id': self.operazione_id,
            'merce_id': self.merce_id,
            'quantita': self.quantita
        }
