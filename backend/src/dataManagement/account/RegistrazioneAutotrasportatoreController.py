from datetime import date, datetime
from flask import jsonify

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
        return jsonify(result.__json__())

    except Exception as e:
        print(f"Errore durante la registrazione di un autotrasportatore: {str(e)}")
        return {}