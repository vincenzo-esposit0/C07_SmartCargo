from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Operazione(Base):
    __tablename__ = 'operazione'

    id = Column(Integer, primary_key=True, autoincrement=True)
    dataOperazione = Column(Date, nullable=False)
    tipo = Column(String(32), nullable=False)
    descrizione = Column(String(255))
    puntoDestinazione = Column(String(32), nullable=False)
    stato = Column(String(32), nullable=False)
    autotrasportatore_id = Column(Integer, ForeignKey('autotrasportatore.id'), nullable=False)
    operatoreIngresso_id = Column(Integer, ForeignKey('operatoreIngresso.id'), nullable=False)
    operatoreMagazzino_id = Column(Integer, ForeignKey('operatoreMagazzino.id'), nullable=False)
    percorso_id = Column(Integer, ForeignKey('percorso.id'), nullable=False)
    veicolo_id = Column(Integer, ForeignKey('veicolo.id'), nullable=False)

    def __init__(self, dataOperazione, tipo, puntoDestinazione, stato, autotrasportatore_id, operatoreIngresso_id,
                 operatoreMagazzino_id, percorso_id, veicolo_id, descrizione=None):
        self.dataOperazione = dataOperazione
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
            'dataOperazione': self.dataOperazione,
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
