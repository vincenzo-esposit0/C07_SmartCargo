from flask import jsonify


try:
    # Prova ad importare con 'src.'
    from src.models.OperatoreSalaDAO import OperatoreSalaDAO
except ImportError:
    # Se fallisce, prova senza 'src.'
    from models.OperatoreSalaDAO import OperatoreSalaDAO


operatore_sala_dao = OperatoreSalaDAO()


def ottieniTuttiOperatoriSala():
    try:
        operatori_sala = operatore_sala_dao.ottieni_tutti_operatori_sala()

        if operatori_sala:
            # Utilizza una lista per ottenere una lista di JSON
            operatori_salaJson = [operatore_sala.__json__() for operatore_sala in operatori_sala]

            # Restituisce la lista di JSON come risultato
            return operatori_salaJson
        else:
            return {"message": "Operatori Sala non trovati"}

    except Exception as e:
        print(f"Errore durante l'ottenimento degli operatori Sala: {str(e)}")
        return {}


def ottieniOperatoreSalaPerId(operatore_sala_id):
    try:
        if operatore_sala_id is not None and operatore_sala_id > 0:
            operatore_sala = operatore_sala_dao.ottieni_operatore_sala_per_id(operatore_sala_id)

            if operatore_sala:
                return operatore_sala.__json__()
            else:
                return {"message": "Operatore di Sala non trovato"}
        elif operatore_sala_id is None or operatore_sala_id < 0:
            return {"message": "Errore: ID Operatore di Sala non valido"}

    except Exception as e:
        return {"message": "Errore durante l'ottenimento dell'operatore di Sala"}


def eliminaOperatoreSala(operatore_sala_id):
    try:
        operatore_sala = operatore_sala_dao.ottieni_operatore_sala_per_id(operatore_sala_id)

        if operatore_sala:
            operatore_sala_dao.elimina_operatore_sala(operatore_sala)
            return jsonify({"messaggio": f"Operatore sala con ID {operatore_sala_id} eliminato con successo"})
        else:
            return jsonify({"errore": f"Nessun operatore sala trovato con ID {operatore_sala_id}"})

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'operatore sala: {str(e)}")
        return {}
