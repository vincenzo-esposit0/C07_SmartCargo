from flask import jsonify
from src.models.OperatoreIngressoDAO import OperatoreIngressoDAO

operatore_ingresso_dao = OperatoreIngressoDAO()

def ottieniTuttiOperatoriIngresso():
    try:
        operatori_ingresso = operatore_ingresso_dao.ottieni_tutti_operatori_ingresso()

        if operatori_ingresso:
            # Utilizza una lista per ottenere una lista di JSON
            operatori_ingressoJson = [operatore_ingresso.__json__() for operatore_ingresso in operatori_ingresso]

            # Restituisce la lista di JSON come risultato
            return operatori_ingressoJson
        else:
            return {"message": "Operatori Ingresso non trovati"}

    except Exception as e:
        print(f"Errore durante l'ottenimento degli operatori Ingresso: {str(e)}")
        return {}

def ottieniOperatoreIngressoPerId(operatore_ingresso_id):
    try:
        operatore_ingresso = operatore_ingresso_dao.ottieni_operatore_ingresso_per_id(operatore_ingresso_id)

        if operatore_ingresso:
            # Restituisci i dettagli dell'operatore Ingresso come JSON
            return operatore_ingresso.__json__()
        else:
            return {"message": "Operatore Ingresso non trovato"}

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'operatore Ingresso: {str(e)}")
        return {}


def eliminaOperatoreIngresso(operatore_ingresso_id):
    try:
        operatore_ingresso = operatore_ingresso_dao.ottieni_operatore_ingresso_per_id(operatore_ingresso_id)

        if operatore_ingresso:
            operatore_ingresso_dao.elimina_operatore_ingresso(operatore_ingresso)
            return jsonify({"messaggio": f"Operatore di ingresso con ID {operatore_ingresso_id} eliminato con successo"})
        else:
            return jsonify({"errore": f"Nessun operatore di ingresso trovato con ID {operatore_ingresso_id}"})

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'operatore di ingresso: {str(e)}")
        return {}
