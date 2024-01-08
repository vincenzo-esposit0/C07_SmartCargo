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
        return autotrasportatore

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
        return autotrasportatore

    def elimina_autotrasportatore(self, autotrasportatore_id):
        session = self.Session()
        autotrasportatore = session.query(Autotrasportatore).filter_by(id=autotrasportatore_id).first()
        session.delete(autotrasportatore)
        session.commit()
        session.close()
        return

    def get_autotrasportatore_per_ingresso(self, autotrasportatore_nome, autotrasportatore_cognome, autotrasportatore_azienda):
        session = self.Session()
        autotrasportatore = session.query(Autotrasportatore).filter_by(nome=autotrasportatore_nome, cognome=autotrasportatore_cognome, azienda=autotrasportatore_azienda).first()
        session.close()
        return autotrasportatore

    def is_autotrasportatore_registrato(self, email):
        """
        Verifica se un autotrasportatore è già registrato sulla base dell'email.
        :param email: L'email dell'autotrasportatore da verificare.
        :return: True se l'autotrasportatore è già registrato, False altrimenti.
        """
        session = self.Session()
        autotrasportatore = session.query(Autotrasportatore).filter_by(email=email).first()
        session.close()
        return autotrasportatore is not None
