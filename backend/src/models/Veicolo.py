from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# E' una funzione per generare una classe base per la definizione della classi di modello, usate
# per rappresentare le tabelle del database come classi Python.
Base = declarative_base()


# Classe di modello che estende Base per indicare che è mappata ad una tabella nel database
class Veicolo(Base):
    __tablename__ = 'veicolo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    targa = Column(String(7), nullable=False)
    descrizione = Column(String(255))
    modello = Column(String(32), nullable=False)

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
