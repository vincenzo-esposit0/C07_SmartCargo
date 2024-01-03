from sqlalchemy.orm import sessionmaker
from src.models import Veicolo
from src.config.database import engine, Session


class VeicoloDAO:
    """Costruttore della classe eseguito automaticamente quando si crea un nuovo oggetto della classe;
    L'attributo self.Session viene utilizzato per creare istanze della sessione quando necessario;"""

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

    def get_veicolo_per_ingresso(self, veicolo_modello, veicolo_targa):
        session = self.Session()
        veicolo = session.query(Veicolo).filter_by(modello=veicolo_modello, azienda=veicolo_targa).first()
        session.close()
        return veicolo