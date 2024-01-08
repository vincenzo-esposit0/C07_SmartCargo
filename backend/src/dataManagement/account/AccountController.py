from flask import jsonify
from datetime import date, datetime
from src.models.OperatoreIngressoDAO import OperatoreIngressoDAO
from src.models.OperatoreMagazzinoDAO import OperatoreMagazzinoDAO
from src.models.OperatoreMobileDAO import OperatoreMobileDAO
from src.models.OperatoreSalaDAO import OperatoreSalaDAO

from src.models.UtenteRegistrato import UtenteRegistrato

operatoreIngresso_dao = OperatoreIngressoDAO()
operatoreMagazzino_dao = OperatoreMagazzinoDAO()
operatoreMobile_dao = OperatoreMobileDAO()
operatoreSala_dao = OperatoreSalaDAO()

def registrazioneAccount(accountJson):
    try:
        opRegistrato = None

        if operatoreIngresso_dao.is_opIngresso_registrato(accountJson["email"]):
            return jsonify({'message': 'Utente già registrato'}), 400
        elif operatoreMagazzino_dao.is_opMagazzino_registrato(accountJson["email"]):
            return jsonify({'message': 'Utente già registrato'}), 400
        elif operatoreMobile_dao.is_opMobile_registrato(accountJson["email"]):
            return jsonify({'message': 'Utente già registrato'}), 400
        elif operatoreSala_dao.is_opSala_registrato(accountJson["email"]):
            return jsonify({'message': 'Utente già registrato'}), 400

        utenteRegistrato = UtenteRegistrato(
            nome = accountJson["nome"],
            cognome = accountJson["cognome"],
            dataNascita = datetime.strptime(accountJson["dataNascita"], "%Y-%m-%dT%H:%M:%S"),
            codiceFiscale = accountJson["codiceFiscale"],
            email = accountJson["email"],
            password = accountJson["password"],
            indirizzo = accountJson["indirizzo"]
        )

        if accountJson["tipo"] == "OpIngresso":
            opRegistrato = operatoreIngresso_dao.aggiungi_operatore_ingresso(utenteRegistrato)
        elif accountJson["tipo"] == "OpMagazzino":
            opRegistrato = operatoreMagazzino_dao.aggiungi_operatore_magazzino(utenteRegistrato)
        elif accountJson["tipo"] == "OpMobile":
            opRegistrato = operatoreMobile_dao.aggiungi_operatore_mobile(utenteRegistrato)
        elif accountJson["tipo"] == "OpSala":
            opRegistrato = operatoreSala_dao.aggiungi_operatore_sala(utenteRegistrato)

        return jsonify(opRegistrato.__json__())

    except Exception as e:
        print(f"Errore durante la registrazione di un autotrasportatore: {str(e)}")
        return {}

def modificaAccount(accountJson):
    try:
        opDaModificare = None
        result = None

        opId = accountJson["id"]

        if accountJson["tipo"] == "OpIngresso":
            opDaModificare = operatoreIngresso_dao.ottieni_operatore_ingresso_per_id(opId)
        elif accountJson["tipo"] == "OpMagazzino":
            opDaModificare = operatoreMagazzino_dao.ottieni_operatore_magazzino_per_id(opId)
        elif accountJson["tipo"] == "OpMobile":
            opDaModificare = operatoreMobile_dao.ottieni_operatore_mobile_per_id(opId)
        elif accountJson["tipo"] == "OpSala":
            opDaModificare = operatoreSala_dao.ottieni_operatore_sala_per_id(opId)

        if opDaModificare:

            opDaModificare.nome = accountJson["nome"]
            opDaModificare.cognome = accountJson["cognome"]
            opDaModificare.dataNascita = datetime.strptime(accountJson["dataNascita"], "%Y-%m-%dT%H:%M:%S")
            opDaModificare.codiceFiscale = accountJson["codiceFiscale"]
            opDaModificare.email = accountJson["email"]
            opDaModificare.password = accountJson["password"]
            opDaModificare.indirizzo = accountJson["indirizzo"]

        if accountJson["tipo"] == "OpIngresso":
            result = operatoreIngresso_dao.aggiorna_operatore_ingresso(opDaModificare)
        elif accountJson["tipo"] == "OpMagazzino":
            result = operatoreMagazzino_dao.aggiorna_operatore_magazzino(opDaModificare)
        elif accountJson["tipo"] == "OpMobile":
            result = operatoreMobile_dao.aggiorna_operatore_mobile(opDaModificare)
        elif accountJson["tipo"] == "OpSala":
            result = operatoreSala_dao.aggiorna_operatore_sala(opDaModificare)

        return jsonify(result.__json__())

    except Exception as e:
        print(f"Errore durante la registrazione di un autotrasportatore: {str(e)}")
        return {}