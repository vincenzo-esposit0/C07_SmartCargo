from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Include(Base):
    __tablename__ = 'include'

    id = Column(Integer, primary_key=True, autoincrement=True)
    operazione_id = Column(Integer, ForeignKey('operazione.id'), nullable=False)
    merce_id = Column(Integer, ForeignKey('merce.id'), nullable=False)
    quantita = Column(Integer, nullable=False)

    # Dichiarazione della relazione con le tabelle referenziate
    operazione = relationship("Operazione", back_populates="include")
    merce = relationship("Merce", back_populates="include")

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
