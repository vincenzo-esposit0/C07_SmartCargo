try:
    from src.models.QrCodeDAO import QrCodeDAO
    from src.config.database import engine, Session
except ImportError:
    from models.QrCodeDAO import QrCodeDAO
    from config.database import engine, Session


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


def ottieniQRCodePerId(qrcode_id):
    try:
        if qrcode_id is not None and qrcode_id > 0:
            qrcode = qrcode_dao.ottieni_qrCode_per_id(qrcode_id)

            if qrcode:
                # Restituisci i dettagli del qrcode come JSON
                return qrcode.__json__()
            else:
                return {"message": "QrCode non trovato"}
        elif qrcode_id is None or qrcode_id < 0:
            return {"message": "Errore: ID QrCode non valido"}

    except Exception as e:
        return {"message": f"Errore durante l'ottenimento del QrCode: {str(e)}"}
