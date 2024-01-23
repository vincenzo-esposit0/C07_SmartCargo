from sqlalchemy import Column, Integer, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class QrCode(Base):
    __tablename__ = 'qrCode'

    id = Column(Integer, primary_key=True, autoincrement=True)
    isValido = Column(Boolean, nullable=False)
    dataCreazione = Column(Date, nullable=False)

    def __init__(self, isValido, dataCreazione):
        self.isValido = isValido
        self.dataCreazione = dataCreazione

    def __json__(self):
        return {
            'id': self.id,
            'isValido': self.isValido,
            'dataCreazione': self.dataCreazione
        }
