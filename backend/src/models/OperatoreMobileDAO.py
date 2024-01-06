from sqlalchemy.orm import sessionmaker
from src.models.UtenteRegistrato import OperatoreMobile
from src.config.database import engine, Session

class OperatoreMobileDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_operatore_mobile(self, operatore_mobile):
        session = self.Session()
        session.add(operatore_mobile)
        session.commit()
        session.refresh(operatore_mobile)
        session.close()
        return operatore_mobile

    def ottieni_tutti_operatori_mobili(self):
        session = self.Session()
        operatori_sala = session.query(OperatoreMobile).all()
        session.close()
        return operatori_sala

    def ottieni_operatore_mobile_per_id(self, operatore_mobile_id):
        session = self.Session()
        operatore_sala = session.query(OperatoreMobile).filter_by(id=operatore_mobile_id).first()
        session.close()
        return operatore_sala

    def aggiorna_operatore_mobile(self, operatore_mobile):
        session = self.Session()
        session.merge(operatore_mobile)
        session.commit()
        session.close()

    def elimina_operatore_sala(self, operatore_mobile_id):
        session = self.Session()
        operatore_sala = session.query(OperatoreMobile).filter_by(id=operatore_mobile_id).first()
        session.delete(operatore_sala)
        session.commit()
        session.close()
