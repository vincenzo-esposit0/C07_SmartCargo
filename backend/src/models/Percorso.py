from sqlalchemy import Column, Integer, String, DateTime, Boolean, func, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Percorso(Base):
    __tablename__ = 'percorso'

    id = Column(Integer, primary_key=True, autoincrement=True)
    puntiLatitudinePercorsi = Column(String(3000), nullable=False)
    puntiLongitudinePercorsi = Column(String(3000), nullable=False)
    puntiLatitudineErrati = Column(String(3000))
    puntiLongitudineErrati = Column(String(3000))

    def __init__(self, puntiLatitudinePercorsi, puntiLongitudinePercorsi, puntiLatitudineErrati=None, puntiLongitudineErrati=None):
        self.puntiLatitudinePercorsi = puntiLatitudinePercorsi
        self.puntiLongitudinePercorsi = puntiLongitudinePercorsi
        self.puntiLatitudineErrati = puntiLatitudineErrati
        self.puntiLongitudineErrati = puntiLongitudineErrati

    def __json__(self):
        return {
            'id': self.id,
            'puntiLatitudineErrati': self.puntiLatitudineErrati,
            'puntiLongitudineErrati': self.puntiLongitudineErrati,
            'puntiLatitudinePercorsi': self.puntiLatitudinePercorsi,
            'puntiLongitudinePercorsi': self.puntiLongitudinePercorsi
        }