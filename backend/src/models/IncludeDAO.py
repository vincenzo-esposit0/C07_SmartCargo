from sqlalchemy.orm import sessionmaker
from src.models import Include
from src.config.database import engine, Session

class IncludeDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def aggiungi_include(self, operazione_id, merce_id, quantita):
        session = self.Session()
        nuovo_include = Include(operazione_id=operazione_id, merce_id=merce_id, quantita=quantita)
        session.add(nuovo_include)
        session.commit()
        session.close()

    def ottieni_tutti_include(self):
        session = self.Session()
        includes = session.query(Include).all()
        session.close()
        return includes

    def ottieni_include_per_id(self, include_id):
        session = self.Session()
        include = session.query(Include).filter_by(id=include_id).first()
        session.close()
        return include

    def aggiorna_include(self, include_id, operazione_id, merce_id, quantita):
        session = self.Session()
        include = session.query(Include).filter_by(id=include_id).first()
        if include:
            include.operazione_id = operazione_id
            include.merce_id = merce_id
            include.quantita = quantita
            session.commit()
            session.close()

    def elimina_include(self, include_id):
        session = self.Session()
        include = session.query(Include).filter_by(id=include_id).first()
        if include:
            session.delete(include)
            session.commit()
            session.close()
