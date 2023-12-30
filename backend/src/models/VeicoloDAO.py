from sqlalchemy.orm import sessionmaker
from backend.src.models import Veicolo
from backend.src.config.database import engine, Session


class VeicoloDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_veicolo(self, veicolo):
        session = self.Session()
        session.add(veicolo)
        session.commit()
        session.close()

    def ottieni_tutti_veicoli(self):
        session = self.Session()
        veicoli = session.query(Veicolo.Veicolo).all()
        session.close()
        return veicoli

    def ottieni_veicolo_per_id(self, veicolo_id):
        session = self.Session()
        veicolo = session.query(Veicolo.Veicolo).filter_by(id=veicolo_id).first()
        session.close()
        return veicolo

    def aggiorna_veicolo(self, veicolo):
        session = self.Session()
        session.merge(veicolo)
        session.commit()
        session.close()

    def elimina_veicolo(self, veicolo_id):
        session = self.Session()
        veicolo = session.query(Veicolo.Veicolo).filter_by(id=veicolo_id).first()
        session.delete(veicolo)
        session.commit()
        session.close()