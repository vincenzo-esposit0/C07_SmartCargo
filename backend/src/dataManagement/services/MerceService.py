from flask import jsonify

from src.models.Merce import Merce
from src.models.MerceDAO import MerceDAO

# Creazione di un'istanza di MerceDAO
merce_dao = MerceDAO()


def nuovaMerce(merceJson):
    try:
        merce = Merce(
            tipo=merceJson["tipo"],
            descrizione=merceJson["descrizione"]
        )

        merceCreata = merce_dao.aggiungi_merce(merce)
        return jsonify(merceCreata.__json__())

    except Exception as e:
        print(f"Errore durante l'aggiunta della merce: {str(e)}")
        return {}


def ottieniTutteMerci():
    try:
        merci = merce_dao.ottieni_tutte_merci()

        if merci:
            # Utilizza una lista per ottenere una lista di JSON
            merciJson = [merce.__json__() for merce in merci]

            # Restituisce la lista di JSON come risultato
            return merciJson
        else:
            return {"message": "Merci non trovate"}

    except Exception as e:
        print(f"Errore durante l'ottenimento delle merci: {str(e)}")
        return {}


def ottieniMercePerId(merce_id):
    try:
        merce = merce_dao.ottieni_merce_per_id(merce_id)

        if merce:
            # Restituisci i dettagli della merce come JSON
            return merce.__json__()
        else:
            return {"message": "Merce non trovata"}

    except Exception as e:
        print(f"Errore durante l'ottenimento della merce: {str(e)}")
        return {}


def eliminaMerce(merce_id):
    try:
        merce = merce_dao.ottieni_merce_per_id(merce_id)

        if merce:
            merce_dao.elimina_merce(merce)
            return jsonify({"messaggio": f"Merce con ID {merce_id} eliminata con successo"})
        else:
            return jsonify({"errore": f"Nessuna merce trovata con ID {merce_id}"})

    except Exception as e:
        print(f"Errore durante l'ottenimento della merce: {str(e)}")
        return {}


def aggiorna_merce(merce_id, nuovi_dati):
    try:
        # Ottieni la merce dal dao
        merce_da_aggiornare = merce_dao.ottieni_merce_per_id(merce_id)

        if merce_da_aggiornare:
            # Aggiorna la merce con i nuovi dati
            merce_da_aggiornare.tipo = nuovi_dati["tipo"]
            merce_da_aggiornare.descrizione = nuovi_dati["descrizione"]

            # Esegui l'aggiornamento nel database
            merce_dao.aggiorna_merce(merce_da_aggiornare)

            return jsonify({"messaggio": f"Merce con ID {merce_id} aggiornata con successo"})
        else:
            return jsonify({"errore": f"Nessuna merce trovata con ID {merce_id}"})

    except Exception as e:
        print(f"Errore durante l'aggiornamento della merce: {str(e)}")
        return jsonify({"errore": "Errore durante l'aggiornamento della merce"})
