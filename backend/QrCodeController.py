from src.models.QrCodeDAO import QrCodeDAO

qrcode_dao = QrCodeDAO()

def ottieniTuttiQRCodes():
    try:
        qrcodes = qrcode_dao.ottieni_tutti_qrCode()

        if qrcodes:
            # Utilizza una lista per ottenere una lista di JSON
            qrcodesJson = [qrcode.__json__() for qrcode in qrcodes]

            # Restituisce la lista di JSON come risultato
            return qrcodesJson
        else:
            return {"message": "QRCodes non trovati"}

    except Exception as e:
        print(f"Errore durante l'ottenimento dei QRCodes: {str(e)}")
        return {}

def ottieniQRCode(qrcode_id):
    try:
        qrcode = qrcode_dao.ottieni_qrCode_per_id(qrcode_id)

        if qrcode:
            # Restituisci i dettagli del qrcode come JSON
            return qrcode.__json__()
        else:
            return {"message": "QRCode non trovato"}

    except Exception as e:
        print(f"Errore durante l'ottenimento del QRCode: {str(e)}")
        return {}
