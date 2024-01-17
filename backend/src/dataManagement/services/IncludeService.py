from flask import jsonify

from src.models.Include import Include
from src.models.IncludeDAO import IncludeDAO

# Creazione di un'istanza di IncludeDAO
include_dao = IncludeDAO()

def nuovaInclude(includeJson):
    try:
        include = Include(
            operazione_id=includeJson["operazione_id"],
            merce_id=includeJson["merce_id"],
            quantita=includeJson["quantita"]
        )

        include = include_dao.aggiungi_include(include)
        return jsonify(include.__json__())

    except Exception as e:
        print(f"Errore durante l'aggiunta della merce: {str(e)}")
        return {}

def ottieniTutteInclude():
    try:
        includeAll = include_dao.ottieni_tutti_include()

        if includeAll:
            # Utilizza una lista per ottenere una lista di JSON
            includiJson = [include.__json__() for include in includeAll]

            # Restituisce la lista di JSON come risultato
            return includiJson
        else:
            return {"message": "Istanze per include non trovate"}

    except Exception as e:
        print(f"Errore durante l'ottenimento delle istanze per include: {str(e)}")
        return {}

def ottieniIncludePerIdOperazione(op_id):
    try:
        include = include_dao.ottieni_include_per_operazione_id(op_id)

        if include:
            # Restituisci i dettagli della include come JSON
            return include.__json__()
        else:
            return {"message": "Istanza include non trovata"}

    except Exception as e:
        print(f"Errore durante l'ottenimento della include: {str(e)}")
        return {}

def eliminaInclude(include_id):
    try:
        include = include_dao.ottieni_merce_per_id(include_id)

        if include:
            include_dao.elimina_include(include_id)
            return jsonify({"messaggio": f"Include con ID {include_id} eliminata con successo"})
        else:
            return jsonify({"errore": f"Nessuna include trovata con ID {include_id}"})

    except Exception as e:
        print(f"Errore durante l'ottenimento della include: {str(e)}")
        return {}

def aggiornaInclude(include_id, nuoviDatiJson):
    try:
        # Ottieni la merce dal dao
        include_da_aggiornare = include_dao.ottieni_include_per_id(include_id)

        if include_da_aggiornare:
            # Aggiorna la merce con i nuovi dati
            include_da_aggiornare.operazione_id = nuoviDatiJson["operazione_id"]
            include_da_aggiornare.merce_id = nuoviDatiJson["merce_id"]
            include_da_aggiornare.quantita = nuoviDatiJson["quantita"]

            # Esegui l'aggiornamento nel database
            include_aggiornata = include_dao.aggiorna_include(include_da_aggiornare)

            return jsonify({"messaggio": f"Include con ID {include_id} aggiornata con successo"})
        else:
            return jsonify({"errore": f"Nessuna include trovata con ID {include_id}"})


    except Exception as e:
        print(f"Errore durante l'aggiornamento della include: {str(e)}")
        return jsonify({"errore": "Errore durante l'aggiornamento della include"})