from sqlalchemy.orm import sessionmaker
from src.config.database import engine, Session
from src.models.Percorso import Percorso

class PercorsoDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_percorso(self, percorso):
        session = self.Session()
        session.add(percorso)
        session.commit()
        session.close()

    def ottieni_tutti_percorsi(self):
        session = self.Session()
        percorsi = session.query(Percorso).all()
        session.close()
        return percorsi

    def ottieni_percorso_per_id(self, percorso_id):
        session = self.Session()
        percorso = session.query(Percorso).filter_by(id=percorso_id).first()
        session.close()
        return percorso

    def aggiorna_percorso(self, percorso):
        session = self.Session()
        session.merge(percorso)
        session.commit()
        session.close()

    def elimina_percorso(self, percorso_id):
        session = self.Session()
        percorso = session.query(Percorso).filter_by(id=percorso_id).first()
        session.delete(percorso)
        session.commit()
        session.close()
