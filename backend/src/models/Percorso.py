from sqlalchemy import Column, Integer, String, DateTime, Boolean, func, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Percorso(Base):
    __tablename__ = 'percorso'

    id = Column(Integer, primary_key=True)
    puntiLatitudineCorretti = Column(Numeric(9, 6))
    puntiLongitudineCorretti = Column(Numeric(9, 6))
    puntiLatitudinePercorsi = Column(Numeric(9, 6))
    puntiLongitudinePercorsi = Column(Numeric(9, 6))
    def __init__(self, puntiLatitudineCorretti, puntiLongitudineCorretti, puntiLatitudinePercorsi, puntiLongitudinePercorsi):
        self.puntiLatitudineCorretti = puntiLatitudineCorretti
        self.puntiLongitudineCorretti = puntiLongitudineCorretti
        self.puntiLatitudinePercorsi = puntiLatitudinePercorsi
        self.puntiLongitudinePercorsi = puntiLongitudinePercorsi

    def __json__(self):
        return {
            'id': self.id,
            'puntiLatitudineCorretti': self.puntiLatitudineCorretti,
            'puntiLongitudineCorretti': self.puntiLongitudineCorretti,
            'puntiLatitudinePercorsi': self.puntiLatitudinePercorsi,
            'puntiLongitudinePercorsi': self.puntiLongitudinePercorsi
        }