from sqlalchemy.orm import sessionmaker
from src.config.database import engine
from sqlalchemy.orm.exc import NoResultFound
from flask import jsonify

from src.models.UtenteRegistrato import OperatoreSala, OperatoreIngresso, OperatoreMobile, OperatoreMagazzino, Autotrasportatore


def login(email, password):
    Session = sessionmaker(bind=engine)
    session = Session()

    # Cerco l'utente in ciascuna tabella
    try:
        operatore_magazzino = session.query(OperatoreMagazzino).filter_by(email=email, password=password).one()
        result = {"stato": 200, "operatore": "Operatore Magazzino", "profilo": operatore_magazzino.__json__()}
        return jsonify(result)

    except NoResultFound:
        pass

    try:
        operatore_mobile = session.query(OperatoreMobile).filter_by(email=email, password=password).one()
        result = {"stato": 200, "operatore": "Operatore Mobile", "profilo": operatore_mobile.__json__()}
        return jsonify(result)

    except NoResultFound:
        pass

    try:
        operatore_sala = session.query(OperatoreSala).filter_by(email=email, password=password).one()
        result = {"stato": 200, "operatore": "Operatore Sala", "profilo": operatore_sala.__json__()}
        return jsonify(result)

    except NoResultFound:
        pass

    try:
        operatore_ingresso = session.query(OperatoreIngresso).filter_by(email=email, password=password).one()
        result = {"stato": 200, "operatore": "Operatore Ingresso", "profilo": operatore_ingresso.__json__()}
        return jsonify(result)

    except NoResultFound:
        pass

    try:
        autotrasportatore = session.query(Autotrasportatore).filter_by(email=email, password=password).one()
        result = {"stato": 200, "operatore": "Autotrasportatore", "profilo": autotrasportatore.__json__()}
        return jsonify(result)

    except NoResultFound:
        pass

    except NoResultFound:
        return jsonify({"stato": 401, "message": "Credenziali errate! Utente non trovato", "profilo": None})
