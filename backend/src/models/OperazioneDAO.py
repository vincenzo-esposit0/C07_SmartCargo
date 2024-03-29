from sqlalchemy.orm import sessionmaker
from src.config.database import engine
from src.models.Operazione import Operazione


class OperazioneDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_operazione(self, operazione):
        session = self.Session()
        session.add(operazione)
        session.commit()
        session.refresh(operazione)
        session.close()
        return operazione

    def ottieni_tutte_operazioni(self):
        session = self.Session()
        operazioni = session.query(Operazione).all()
        session.close()
        return operazioni

    def ottieni_operazione_per_id(self, operazione_id):
        session = self.Session()
        operazione = session.query(Operazione).filter_by(id=operazione_id).first()
        session.close()
        return operazione

    def aggiorna_operazione(self, operazione):
        session = self.Session()
        session.merge(operazione)
        session.commit()
        session.close()

    def elimina_operazione(self, operazione_id):
        session = self.Session()
        operazione = session.query(Operazione).filter_by(id=operazione_id).first()
        session.delete(operazione)
        session.commit()
        session.close()

    def ottieni_operazioni_per_idAutotrasportatore(self, autotrasportatore_id):
        session = self.Session()
        operazione = session.query(Operazione).filter_by(autotrasportatore_id=autotrasportatore_id).all()
        session.close()
        return operazione

    def ottieni_operazioni_per_id_OpMagazzino(self, operatore_magazzino_id):
        session = self.Session()
        operazioni = session.query(Operazione).filter_by(operatoreMagazzino_id=operatore_magazzino_id).all()
        session.close()
        return operazioni

    def ottieni_operazioni_per_stato(self, stato):
        session = self.Session()
        operazione = session.query(Operazione).filter_by(stato=stato).all()
        session.close()
        return operazione
