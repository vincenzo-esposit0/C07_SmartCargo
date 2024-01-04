from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Operazione(Base):
    __tablename__ = 'operazione'

    id = Column(Integer, primary_key=True)
    tipo = Column(String(32), nullable=False)
    descrizione = Column(String(255))
    puntoDestinazione = Column(String(32), nullable=False)
    stato = Column(String(32), nullable=False)
    autotrasportatore_id = Column(Integer, ForeignKey('autotrasportatore.id'), nullable=False)
    operatoreIngresso_id = Column(Integer, ForeignKey('operatoreIngresso.id'), nullable=False)
    operatoreMagazzino_id = Column(Integer, ForeignKey('operatoreMagazzino.id'), nullable=False)
    percorso_id = Column(Integer, ForeignKey('percorso.id'), nullable=False)
    veicolo_id = Column(Integer, ForeignKey('veicolo.id'), nullable=False)

    autotrasportatore = relationship('Autotrasportatore', foreign_keys=[autotrasportatore_id], backref='operazioni_autotrasportatore')
    operatoreIngresso = relationship('OperatoreIngresso', foreign_keys=[operatoreIngresso_id], backref='operazioni_operatore_ingresso')
    operatoreMagazzino = relationship('OperatoreMagazzino', foreign_keys=[operatoreMagazzino_id], backref='operazioni_operatore_magazzino')
    percorso = relationship('Percorso', backref='operazioni')
    veicolo = relationship('Veicolo', backref='operazioni')

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
