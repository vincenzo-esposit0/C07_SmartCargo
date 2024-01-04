from datetime import date

from flask import jsonify

from src.models.QrCode import QrCode
from src.models.QrCodeDAO import QrCodeDAO
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
from src.models.UtenteRegistrato import Autotrasportatore

autotrasportatoreDao = AutotrasportatoreDAO()
qrCodeDao = QrCodeDAO()


def registrazioneAutotrasportatore(autotrasportatoreJson):
    try:
        if autotrasportatoreDao.is_autotrasportatore_registrato(autotrasportatoreJson["email"]):
            print("Autotrasportatore già registrato")
            return {} #jsonify({'message': 'Autotrasportatore già registrato'}), 400

        qrCode = QrCode(
            isValido = True,
            dataCreazione = date.today()
        )
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
        qrCodeDao.aggiungi_qrCode(qrCode)
        result = autotrasportatoreDao.aggiungi_autotrasportatore(autotrasportatore)
        return jsonify(result._json_())

    except Exception as e:
        print(f"Errore durante la registrazione di un autotrasportatore: {str(e)}")
        return {}