from sqlalchemy.orm import sessionmaker
from src.models.Veicolo import Veicolo
from src.config.database import engine, Session


class VeicoloDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_veicolo(self, veicolo):
        session = self.Session()
        session.add(veicolo)
        session.commit()
        session.refresh(veicolo)
        session.close()
        return veicolo

    def ottieni_tutti_veicoli(self):
        session = self.Session()
        veicoli = session.query(Veicolo).all()
        session.close()
        return veicoli

    def ottieni_veicolo_per_id(self, veicolo_id):
        session = self.Session()
        veicolo = session.query(Veicolo).filter_by(id=veicolo_id).first()
        session.close()
        return veicolo

    def aggiorna_veicolo(self, veicolo):
        session = self.Session()
        session.merge(veicolo)
        session.commit()
        session.close()

    def elimina_veicolo(self, veicolo_id):
        session = self.Session()
        veicolo = session.query(Veicolo).filter_by(id=veicolo_id).first()
        session.delete(veicolo)
        session.commit()
        session.close()

    def get_veicolo_per_ingresso(self, veicolo_modello, veicolo_targa):
        session = self.Session()
        veicolo = session.query(Veicolo).filter_by(modello=veicolo_modello, azienda=veicolo_targa).first()
        session.close()
        return veicolo