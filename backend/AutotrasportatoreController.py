from datetime import date

from flask import jsonify

from src.models.QrCode import QrCode
from src.models.QrCodeDAO import QrCodeDAO
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
from src.models.UtenteRegistrato import Autotrasportatore

autotrasportatore_dao = AutotrasportatoreDAO()
qrCodeDao = QrCodeDAO()


def registrazioneAutotrasportatore(autotrasportatoreJson):
    try:
        if autotrasportatore_dao.is_autotrasportatore_registrato(autotrasportatoreJson["email"]):
            return jsonify({'message': 'Autotrasportatore già registrato'}), 400

        qrCode = QrCode(
            isValido = True,
            dataCreazione = date.today()
        )

        qrCode = qrCodeDao.aggiungi_qrCode(qrCode)

        autotrasportatore = Autotrasportatore(
            nome = autotrasportatoreJson["nome"],
            cognome= autotrasportatoreJson["cognome"],
            dataNascita= autotrasportatoreJson["dataNascita"],
            codiceFiscale= autotrasportatoreJson["codiceFiscale"],
            email= autotrasportatoreJson["email"],
            password= autotrasportatoreJson["password"],
            indirizzo= autotrasportatoreJson["indirizzo"],
            azienda= autotrasportatoreJson["azienda"],
            qrCode_id= qrCode.id
        )

        result = autotrasportatore_dao.aggiungi_autotrasportatore(autotrasportatore)
        return jsonify(result.__json__())

    except Exception as e:
        print(f"Errore durante la registrazione di un autotrasportatore: {str(e)}")
        return {}

def ottieniTuttiAutotrasportatori():
    try:
        autotrasportatori = autotrasportatore_dao.ottieni_tutti_autotrasportatori()

        if autotrasportatori:
            # Utilizza una lista per ottenere una lista di JSON
            autotrasportatoriJson = [autotrasportatore.__json__() for autotrasportatore in autotrasportatori]

            # Restituisce la lista di JSON come risultato
            return autotrasportatoriJson
        else:
            return {"message": "Autotrasportatori non trovati"}

    except Exception as e:
        print(f"Errore durante l'ottenimento degli autotrasportatori: {str(e)}")
        return {}

def ottieniAutotrasportatore(autotrasportatore_id):
    try:
        autotrasportatore = autotrasportatore_dao.ottieni_autotrasportatore_per_id(autotrasportatore_id)

        if autotrasportatore:
            # Restituisci i dettagli dell'autotrasportatore come JSON
            return autotrasportatore.__json__()
        else:
            return {"message": "Autotrasportatore non trovato"}

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'autotrasportatore: {str(e)}")
        return {}
