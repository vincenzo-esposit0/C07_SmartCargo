from src.models.UtenteRegistrato import Autotrasportatore
from src.config.database import engine
from sqlalchemy.orm import sessionmaker

class AutotrasportatoreDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_autotrasportatore(self, autotrasportatore):
        session = self.Session()
        session.add(autotrasportatore)
        session.commit()
        session.close()

    def ottieni_tutti_autotrasportatori(self):
        session = self.Session()
        autotrasportatori = session.query(Autotrasportatore).all()
        session.close()
        return autotrasportatori

    def ottieni_autotrasportatore_per_id(self, autotrasportatore_id):
        session = self.Session()
        autotrasportatore = session.query(Autotrasportatore).filter_by(id=autotrasportatore_id).first()
        session.close()
        return autotrasportatore

    def aggiorna_autotrasportatore(self, autotrasportatore):
        session = self.Session()
        session.merge(autotrasportatore)
        session.commit()
        session.close()

    def elimina_autotrasportatore(self, autotrasportatore_id):
        session = self.Session()
        autotrasportatore = session.query(Autotrasportatore).filter_by(id=autotrasportatore_id).first()
        session.delete(autotrasportatore)
        session.commit()
        session.close()
