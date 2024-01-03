from sqlalchemy.orm import sessionmaker
from src.models.UtenteRegistrato import OperatoreSala
from src.config.database import engine

class OperatoreSalaDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_operatore_sala(self, operatore_sala):
        session = self.Session()
        session.add(operatore_sala)
        session.commit()
        session.close()

    def ottieni_tutti_operatori_sala(self):
        session = self.Session()
        operatori_sala = session.query(OperatoreSala).all()
        session.close()
        return operatori_sala

    def ottieni_operatore_sala_per_id(self, operatore_sala_id):
        session = self.Session()
        operatore_sala = session.query(OperatoreSala).filter_by(id=operatore_sala_id).first()
        session.close()
        return operatore_sala

    def aggiorna_operatore_sala(self, operatore_sala):
        session = self.Session()
        session.merge(operatore_sala)
        session.commit()
        session.close()

    def elimina_operatore_sala(self, operatore_sala_id):
        session = self.Session()
        operatore_sala = session.query(OperatoreSala).filter_by(id=operatore_sala_id).first()
        session.delete(operatore_sala)
        session.commit()
        session.close()