from sqlalchemy.orm import sessionmaker
from src.models import Merce
from src.config.database import engine, Session


class MerceDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_merce(self, merce):
        session = self.Session()
        session.add(merce)
        session.commit()
        session.refresh(merce)
        session.close()
        return merce

    def ottieni_tutte_merci(self):
        session = self.Session()
        merci = session.query(Merce.Merce).all()
        session.close()
        return merci

    def ottieni_merce_per_id(self, merce_id):
        session = self.Session()
        merce = session.query(Merce.Merce).filter_by(id=merce_id).first()
        session.close()
        return merce

    def aggiorna_merce(self, merce):
        session = self.Session()
        session.merge(merce)
        session.commit()
        session.close()
        return merce

    def elimina_merce(self, merce_id):
        session = self.Session()
        merce = session.query(Merce.Merce).filter_by(id=merce_id).first()
        session.delete(merce)
        session.commit()
        session.close()
