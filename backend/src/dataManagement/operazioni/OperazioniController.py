from flask import jsonify
from src.models.OperazioneDAO import OperazioneDAO

operazione_dao = OperazioneDAO()


# metodo utilizzato dall'operatore di magazzino per l'aggiornamento dello stato dell operazione


def segnalazione_esito_operazione(operazioneJson):
    try:
        operazione_id = operazioneJson["id"]
        operazione = operazione_dao.ottieni_operazione_per_id(operazione_id)

        if operazione:
            operazione.stato = operazioneJson["stato"]

            operazione_dao.aggiorna_operazione(operazione)

            return jsonify(operazione.__json__())

    except Exception as e:
        print(f"Errore durante l'aggiornamento dello stato dell'operazione: {str(e)}")
        return {"message": "Errore durante l'aggiornamento dello stato dell'operazione"}
