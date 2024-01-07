from sqlalchemy import Column, Integer, String, DateTime, Boolean, func, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Percorso(Base):
    __tablename__ = 'percorso'

    id = Column(Integer, primary_key=True, autoincrement=True)
    puntiLatitudinePercorsi = Column(String(3000), nullable=False)
    puntiLongitudinePercorsi = Column(String(3000), nullable=False)
    puntiLatitudineCorretti = Column(String(3000))
    puntiLongitudineCorretti = Column(String(3000))

    def __init__(self, puntiLatitudinePercorsi, puntiLongitudinePercorsi, puntiLatitudineCorretti=None, puntiLongitudineCorretti=None):
        self.puntiLatitudinePercorsi = puntiLatitudinePercorsi
        self.puntiLongitudinePercorsi = puntiLongitudinePercorsi
        self.puntiLatitudineCorretti = puntiLatitudineCorretti
        self.puntiLongitudineCorretti = puntiLongitudineCorretti

    def __json__(self):
        return {
            'id': self.id,
            'puntiLatitudineCorretti': self.puntiLatitudineCorretti,
            'puntiLongitudineCorretti': self.puntiLongitudineCorretti,
            'puntiLatitudinePercorsi': self.puntiLatitudinePercorsi,
            'puntiLongitudinePercorsi': self.puntiLongitudinePercorsi
        }