from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Veicolo(Base):
    __tablename__ = 'veicolo'

    id = Column(Integer, primary_key=True)
    targa = Column(String(7))
    descrizione = Column(String(255))
    modello = Column(String(32))

    def __init__(self, targa, descrizione, modello):
        self.targa = targa
        self.descrizione = descrizione
        self.modello = modello

    def __json__(self):
        return {
            'id': self.id,
            'targa': self.targa,
            'descrizione': self.descrizione,
            'modello': self.modello
        }