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

        operatore_magazzino = session.query(OperatoreMagazzino).filter_by(email=email, password=password).first()
        operatore_mobile = session.query(OperatoreMobile).filter_by(email=email, password=password).first()
        operatore_sala = session.query(OperatoreSala).filter_by(email=email, password=password).first()
        operatore_ingresso = session.query(OperatoreIngresso).filter_by(email=email, password=password).first()
        autotrasportatore = session.query(Autotrasportatore).filter_by(email=email, password=password).first()

        if operatore_magazzino:
            result = {"stato": 200, "operatore": "Operatore Magazzino", "profilo": operatore_magazzino.__json__()}
            return jsonify(result)
        elif operatore_mobile:
            result = {"stato": 200, "operatore": "Operatore Mobile", "profilo": operatore_mobile.__json__()}
            return jsonify(result)
        elif operatore_sala:
            result = {"stato": 200, "operatore": "Operatore Sala", "profilo": operatore_sala.__json__()}
            return jsonify(result)
        elif operatore_ingresso:
            result = {"stato": 200, "operatore": "Operatore Ingresso", "profilo": operatore_ingresso.__json__()}
            return jsonify(result)
        elif autotrasportatore:
            result = {"stato": 200, "operatore": "Autotrasportatore", "profilo": autotrasportatore.__json__()}
            return jsonify(result)
        else:
            return jsonify({"stato": 401, "message": "Credenziali errate! Utente non trovato", "profilo": None})

    except Exception as e:
        print(f"Errore durante il login: {str(e)}")
        return jsonify({"message": "Errore durante il login"})
