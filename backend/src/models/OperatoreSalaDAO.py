from sqlalchemy.orm import sessionmaker

try:
    from src.models.UtenteRegistrato import OperatoreSala
    from src.config.database import engine, Session
except ImportError:
    from models.UtenteRegistrato import OperatoreSala
    from config.database import engine, Session


class OperatoreSalaDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_operatore_sala(self, operatore_sala):
        session = self.Session()
        session.add(operatore_sala)
        session.commit()
        session.refresh(operatore_sala)
        session.close()
        return operatore_sala

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
        return operatore_sala

    def elimina_operatore_sala(self, operatore_sala_id):
        session = self.Session()
        operatore_sala = session.query(OperatoreSala).filter_by(id=operatore_sala_id).first()
        session.delete(operatore_sala)
        session.commit()
        session.close()

    def is_opSala_registrato(self, email):
        session = self.Session()
        opSala = session.query(OperatoreSala).filter_by(email=email).first()
        session.close()
        return opSala is not None