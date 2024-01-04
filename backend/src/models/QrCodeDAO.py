from sqlalchemy.orm import sessionmaker
from src.models import QrCode
from src.config.database import engine, Session


class QrCodeDAO:

    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_qrCode(self, qrCode):
        session = self.Session()
        session.add(qrCode)
        session.commit()
        session.refresh(qrCode)
        session.close()
        return qrCode

    def ottieni_tutti_qrCode(self):
        session = self.Session()
        allQrCode = session.query(QrCode.QrCode).all()
        session.close()
        return allQrCode

    def ottieni_qrCode_per_id(self, qrCode_id):
        session = self.Session()
        qrCode = session.query(QrCode.QrCode).filter_by(id = qrCode_id).first()
        session.close()
        return qrCode

    def aggiorna_qrCode(self, qrCode):
        session = self.Session()
        session.merge(qrCode)
        session.commit()
        session.close()

    def elimina_qrCode(self, qrCode_id):
        session = self.Session()
        qrCode = session.query(QrCode.QrCode).filter_by(id = qrCode_id).first()
        session.delete(qrCode)
        session.commit()
        session.close()
