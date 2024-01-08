from sqlalchemy.orm import sessionmaker
from src.models.UtenteRegistrato import OperatoreIngresso
from src.config.database import engine, Session

class OperatoreIngressoDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_operatore_ingresso(self, operatore_ingresso):
        session = self.Session()
        session.add(operatore_ingresso)
        session.commit()
        session.refresh(operatore_ingresso)
        session.close()
        return operatore_ingresso

    def ottieni_tutti_operatori_ingresso(self):
        session = self.Session()
        operatori_ingresso = session.query(OperatoreIngresso).all()
        session.close()
        return operatori_ingresso

    def ottieni_operatore_ingresso_per_id(self, operatore_ingresso_id):
        session = self.Session()
        operatore_ingresso = session.query(OperatoreIngresso).filter_by(id=operatore_ingresso_id).first()
        session.close()
        return operatore_ingresso

    def aggiorna_operatore_ingresso(self, operatore_ingresso):
        session = self.Session()
        session.merge(operatore_ingresso)
        session.commit()
        session.close()
        return operatore_ingresso

    def elimina_operatore_ingresso(self, operatore_ingresso_id):
        session = self.Session()
        operatore_ingresso = session.query(OperatoreIngresso).filter_by(id=operatore_ingresso_id).first()
        session.delete(operatore_ingresso)
        session.commit()
        session.close()

    def is_opIngresso_registrato(self, email):

        session = self.Session()
        opIngresso = session.query(OperatoreIngresso).filter_by(email=email).first()
        session.close()
        return opIngresso is not None
