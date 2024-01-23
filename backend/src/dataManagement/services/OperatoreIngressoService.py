from flask import jsonify
# from src.models.OperatoreIngressoDAO import OperatoreIngressoDAO

try:
    # Prova ad importare con 'src.'
    from src.models.OperatoreIngressoDAO import OperatoreIngressoDAO
except ImportError:
    # Se fallisce, prova senza 'src.'
    from models.OperatoreIngressoDAO import OperatoreIngressoDAO


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
        if operatore_ingresso_id is not None and operatore_ingresso_id > 0:
            operatore_ingresso = operatore_ingresso_dao.ottieni_operatore_ingresso_per_id(operatore_ingresso_id)

            if operatore_ingresso:
                # Restituisci i dettagli dell'operatore Ingresso come JSON
                return operatore_ingresso.__json__()
            else:
                return {"message": "Operatore di Ingresso non trovato"}
        elif operatore_ingresso_id is None or operatore_ingresso_id < 0:
            return {"message": "Errore: ID Operatore di Ingresso non valido"}

    except Exception as e:
        return {"message": "Errore durante l'ottenimento dell'operatore di Ingresso"}


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
