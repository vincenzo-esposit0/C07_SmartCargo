from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Issue(Base):
    __tablename__ = 'issue'

    id = Column(Integer, primary_key=True, autoincrement=True)
    descrizione = Column(String(255))
    timestampApertura = Column(DateTime, nullable=False)
    timestampChiusura = Column(DateTime,default=None, nullable=True)
    stato = Column(String(255), nullable=False)
    tipologiaProblema = Column(String(255), nullable=False)
    posizione = Column(String(255), nullable=False)
    operatoreSala_id = Column(Integer)
    operatoreMobile_id = Column(Integer)
    operazione_id = Column(Integer)

    def __init__(self, descrizione, timestampApertura, timestampChiusura, stato, tipologiaProblema, posizione,
                 operatoreSala_id, operatoreMobile_id, operazione_id):
        self.descrizione = descrizione
        self.timestampApertura = timestampApertura
        self.timestampChiusura = timestampChiusura
        self.stato = stato
        self.tipologiaProblema = tipologiaProblema
        self.posizione = posizione
        self.operatoreSala_id = operatoreSala_id
        self.operatoreMobile_id = operatoreMobile_id
        self.operazione_id = operazione_id

    def __json__(self):
        return {
            'id': self.id,
            'descrizione': self.descrizione,
            'timestampApertura': self.timestampApertura,
            'timestampChiusura': self.timestampChiusura,
            'stato': self.stato,
            'tipologiaProblema': self.tipologiaProblema,
            'posizione': self.posizione,
            'operatoreSala_id': self.operatoreSala_id,
            'operatoreMobile_id': self.operatoreMobile_id,
            'operazione_id': self.operazione_id
        }
