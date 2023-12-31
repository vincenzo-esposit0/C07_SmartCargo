from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Operazione(Base):
    __tablename__ = 'operazione'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(32), nullable=False)
    descrizione = Column(String(255))
    puntoDestinazione = Column(String(32), nullable=False)
    stato = Column(String(32), nullable=False)
    autotrasportatore_id = Column(Integer, nullable=False)
    operatoreIngresso_id = Column(Integer, nullable=False)
    operatoreMagazzino_id = Column(Integer, nullable=False)
    percorso_id = Column(Integer, nullable=False)
    veicolo_id = Column(Integer, nullable=False)

    def __init__(self, tipo, puntoDestinazione, stato, autotrasportatore_id, operatoreIngresso_id,
                 operatoreMagazzino_id, percorso_id, veicolo_id, descrizione=None):
        self.tipo = tipo
        self.descrizione = descrizione
        self.puntoDestinazione = puntoDestinazione
        self.stato = stato
        self.autotrasportatore_id = autotrasportatore_id
        self.operatoreIngresso_id = operatoreIngresso_id
        self.operatoreMagazzino_id = operatoreMagazzino_id
        self.percorso_id = percorso_id
        self.veicolo_id = veicolo_id


    def __json__(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'descrizione': self.descrizione,
            'puntoDestinazione': self.puntoDestinazione,
            'stato': self.stato,
            'autotrasportatore_id': self.autotrasportatore_id,
            'operatoreIngresso_id': self.operatoreIngresso_id,
            'operatoreMagazzino_id': self.operatoreMagazzino_id,
            'percorso_id': self.percorso_id,
            'veicolo_id': self.veicolo_id
        }