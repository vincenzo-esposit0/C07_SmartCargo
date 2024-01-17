from flask import jsonify
from src.models.OperatoreMagazzinoDAO import OperatoreMagazzinoDAO

operatore_magazzino_dao = OperatoreMagazzinoDAO()

def ottieniTuttiOperatoriMagazzino():
    try:
        operatori_magazzino = operatore_magazzino_dao.ottieni_tutti_operatori_magazzino()

        if operatori_magazzino:
            # Utilizza una lista per ottenere una lista di JSON
            operatori_magazzinoJson = [operatore_magazzino.__json__() for operatore_magazzino in operatori_magazzino]

            # Restituisce la lista di JSON come risultato
            return operatori_magazzinoJson
        else:
            return {"message": "Operatori Magazzino non trovati"}

    except Exception as e:
        print(f"Errore durante l'ottenimento degli operatori Magazzino: {str(e)}")
        return {}

def ottieniOperatoreMagazzinoPerId(operatore_magazzino_id):
    try:
        operatore_magazzino = operatore_magazzino_dao.ottieni_operatore_magazzino_per_id(operatore_magazzino_id)

        if operatore_magazzino:
            # Restituisci i dettagli dell'operatore Magazzino come JSON
            return operatore_magazzino.__json__()
        else:
            return {"message": "Operatore Magazzino non trovato"}

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'operatore Magazzino: {str(e)}")
        return {}

def eliminaOperatoreMagazzino(operatore_magazzino_id):
    try:
        operatore_magazzino = operatore_magazzino_dao.ottieni_operatore_magazzino_per_id(operatore_magazzino_id)

        if operatore_magazzino:
            operatore_magazzino_dao.elimina_operatore_magazzino(operatore_magazzino)
            return jsonify({"messaggio": f"Operatore magazzino con ID {operatore_magazzino_id} eliminato con successo"})
        else:
            return jsonify({"errore": f"Nessun operatore magazzino trovato con ID {operatore_magazzino_id}"})

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'operatore magazzino: {str(e)}")
        return {}

