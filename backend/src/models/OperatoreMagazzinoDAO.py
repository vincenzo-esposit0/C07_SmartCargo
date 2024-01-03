from src.models.UtenteRegistrato import OperatoreMagazzino
from src.config.database import engine
from sqlalchemy.orm import sessionmaker

class OperatoreMagazzinoDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_operatore_magazzino(self, operatore_magazzino):
        session = self.Session()
        session.add(operatore_magazzino)
        session.commit()
        session.close()

    def ottieni_tutti_operatori_magazzino(self):
        session = self.Session()
        operatori_magazzino = session.query(OperatoreMagazzino).all()
        session.close()
        return operatori_magazzino

    def ottieni_operatore_magazzino_per_id(self, operatore_magazzino_id):
        session = self.Session()
        operatore_magazzino = session.query(OperatoreMagazzino).filter_by(id=operatore_magazzino_id).first()
        session.close()
        return operatore_magazzino

    def aggiorna_operatore_magazzino(self, operatore_magazzino):
        session = self.Session()
        session.merge(operatore_magazzino)
        session.commit()
        session.close()

    def elimina_operatore_magazzino(self, operatore_magazzino_id):
        session = self.Session()
        operatore_magazzino = session.query(OperatoreMagazzino).filter_by(id=operatore_magazzino_id).first()
        session.delete(operatore_magazzino)
        session.commit()
        session.close()
