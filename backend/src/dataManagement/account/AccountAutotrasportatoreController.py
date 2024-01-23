from datetime import date, datetime
from flask import jsonify

try:
    from backend.src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
    from backend.src.models.QrCode import QrCode
    from backend.src.models.QrCodeDAO import QrCodeDAO
    from backend.src.models.UtenteRegistrato import Autotrasportatore
except ImportError:
    from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
    from src.models.QrCode import QrCode
    from src.models.QrCodeDAO import QrCodeDAO
    from src.models.UtenteRegistrato import Autotrasportatore

autotrasportatore_dao = AutotrasportatoreDAO()
qrcode_dao = QrCodeDAO()

def registrazioneAutotrasportatore(autotrasportatoreJson):
    try:
        if autotrasportatore_dao.is_autotrasportatore_registrato(autotrasportatoreJson["email"]):
            return jsonify({'message': 'Autotrasportatore già registrato'}), 400

        qrCode = QrCode(
            isValido = True,
            dataCreazione = date.today()
        )

        qrCode = qrcode_dao.aggiungi_qrCode(qrCode)

        autotrasportatore = Autotrasportatore(
            nome = autotrasportatoreJson["nome"],
            cognome= autotrasportatoreJson["cognome"],
            dataNascita=datetime.strptime(autotrasportatoreJson["dataNascita"], "%Y-%m-%dT%H:%M:%S"),
            codiceFiscale= autotrasportatoreJson["codiceFiscale"],
            email= autotrasportatoreJson["email"],
            password= autotrasportatoreJson["password"],
            indirizzo= autotrasportatoreJson["indirizzo"],
            azienda= autotrasportatoreJson["azienda"],
            qrCode_id= qrCode.id
        )

        result = autotrasportatore_dao.aggiungi_autotrasportatore(autotrasportatore)

        if result:
            return jsonify({'message': 'Autotrasportatore registrato con successo', 'success': True, 'autotrasportatore': result.__json__()})
        else:
            return jsonify({'message': 'Errore durante la registrazione dell\'autotrasportatore', 'success': False})

    except Exception as e:
        print(f"Errore durante la registrazione di un autotrasportatore: {str(e)}")
        return {"message": "Errore durante la registrazione di un autotrasportatore"}

def modificaAutotrasportatore(autotrasportatoreJson):
    try:
        # Verifica campi obbligatori
        required_fields = ["id", "nome", "cognome", "dataNascita", "codiceFiscale", "email", "password", "indirizzo", "azienda"]
        for field in required_fields:
            if field not in autotrasportatoreJson or not autotrasportatoreJson[field]:
                return {"message": f"Campo obbligatorio mancante o vuoto: {field}"}

        opId = autotrasportatoreJson["id"]

        autotrasportatore = autotrasportatore_dao.ottieni_autotrasportatore_per_id(opId)

        if autotrasportatore:

            autotrasportatore.nome = autotrasportatoreJson["nome"]
            autotrasportatore.cognome= autotrasportatoreJson["cognome"]
            autotrasportatore.dataNascita=datetime.strptime(autotrasportatoreJson["dataNascita"], "%Y-%m-%d").date()
            autotrasportatore.codiceFiscale= autotrasportatoreJson["codiceFiscale"]
            autotrasportatore.email= autotrasportatoreJson["email"]
            autotrasportatore.password= autotrasportatoreJson["password"]
            autotrasportatore.indirizzo= autotrasportatoreJson["indirizzo"]
            autotrasportatore.azienda= autotrasportatoreJson["azienda"]

        result = autotrasportatore_dao.aggiorna_autotrasportatore(autotrasportatore)
        return result.__json__()

    except Exception as e:
        print(f"Errore durante la modifica account di un autotrasportatore: {str(e)}")
        return {"message": "Errore durante la modifica dell'account di un autotrasportatore"}