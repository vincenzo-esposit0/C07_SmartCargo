from flask import jsonify

from src.models.Percorso import Percorso
from src.models.PercorsoDAO import PercorsoDAO

# Creazione di un'istanza di PercorsoDAO
percorso_dao = PercorsoDAO()

def nuovoPercorso(percorsoJson):
    try:
        percorso = Percorso(
            puntiLatitudinePercorsi=percorsoJson["puntiLatitudinePercorsi"],
            puntiLongitudinePercorsi=percorsoJson["puntiLongitudinePercorsi"],
            puntiLatitudineCorretti=percorsoJson.get("puntiLatitudineCorretti"),
            puntiLongitudineCorretti=percorsoJson.get("puntiLongitudineCorretti")
        )

        percorsoCreato = percorso_dao.aggiungi_percorso(percorso)
        return jsonify(percorsoCreato.__json__())

    except Exception as e:
        print(f"Errore durante l'aggiunta del percorso: {str(e)}")
        return {}

def ottieniTuttiPercorsi():
    try:
        percorsi = percorso_dao.ottieni_tutti_percorsi()

        if percorsi:
            percorsiJson = [percorso.__json__() for percorso in percorsi]
            return percorsiJson
        else:
            return {"message": "Percorsi non trovati"}

    except Exception as e:
        print(f"Errore durante l'ottenimento dei percorsi: {str(e)}")
        return {}

def ottieniPercorsoPerId(percorso_id):
    try:
        percorso = percorso_dao.ottieni_percorso_per_id(percorso_id)

        if percorso:
            return percorso.__json__()
        else:
            return {"message": "Percorso non trovato"}

    except Exception as e:
        print(f"Errore durante l'ottenimento del percorso: {str(e)}")
        return {}

def eliminaPercorso(percorso_id):
    try:
        percorso = percorso_dao.ottieni_percorso_per_id(percorso_id)

        if percorso:
            percorso_dao.elimina_percorso(percorso)
            return jsonify({"messaggio": f"Percorso con ID {percorso_id} eliminato con successo"})
        else:
            return jsonify({"errore": f"Nessun percorso trovato con ID {percorso_id}"})

    except Exception as e:
        print(f"Errore durante l'eliminazione del percorso: {str(e)}")
        return {}

def aggiorna_percorso(percorso_id, nuovi_dati):
    try:
        percorso_da_aggiornare = percorso_dao.ottieni_percorso_per_id(percorso_id)

        if percorso_da_aggiornare:
            percorso_da_aggiornare.puntiLatitudinePercorsi = nuovi_dati["puntiLatitudinePercorsi"]
            percorso_da_aggiornare.puntiLongitudinePercorsi = nuovi_dati["puntiLongitudinePercorsi"]
            percorso_da_aggiornare.puntiLatitudineCorretti = nuovi_dati.get("puntiLatitudineCorretti")
            percorso_da_aggiornare.puntiLongitudineCorretti = nuovi_dati.get("puntiLongitudineCorretti")

            percorso_aggiornato = percorso_dao.aggiorna_percorso(percorso_da_aggiornare)

            return jsonify({"messaggio": f"Percorso con ID {percorso_id} aggiornato con successo"})
        else:
            return jsonify({"errore": f"Nessun percorso trovato con ID {percorso_id}"})


    except Exception as e:
        print(f"Errore durante l'aggiornamento del percorso: {str(e)}")
        return jsonify({"errore": "Errore durante l'aggiornamento del percorso"})

def aggiornaPercorsoByAlgoritmo(percorsoId, latString, lonString):
    try:
        percorsoDaAggiornare = percorso_dao.ottieni_percorso_per_id(percorsoId)

        if percorsoDaAggiornare:
            percorsoDaAggiornare.puntiLatitudineCorretti = latString
            percorsoDaAggiornare.puntiLongitudineCorretti = lonString

            percorsoAggiornato = percorso_dao.aggiorna_percorso(percorsoDaAggiornare)

            return {"messaggio": f"Percorso con ID {percorsoId} aggiornato con successo"}
        else:
            return {"errore": f"Nessun percorso trovato con ID {percorsoId}"}

    except Exception as e:
        print(f"Errore durante l'aggiornamento del percorso: {str(e)}")
        return {"errore": "Errore durante l'aggiornamento del percorso"}