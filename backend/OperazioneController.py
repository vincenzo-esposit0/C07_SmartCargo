from src.models.OperazioneDAO import OperazioneDAO

operazione_dao = OperazioneDAO()

def ottieniTutteOperazioni():
    try:
        operazioni = operazione_dao.ottieni_tutte_operazioni()

        if operazioni:
            # Utilizza una lista per ottenere una lista di JSON
            operazioniJson = [operazione.__json__() for operazione in operazioni]

            # Restituisce la lista di JSON come risultato
            return operazioniJson
        else:
            return {"message": "Operazioni non trovate"}

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni: {str(e)}")
        return {}

def ottieniOperazione(operazione_id):
    try:
        operazione = operazione_dao.ottieni_operazione_per_id(operazione_id)

        if operazione:
            # Restituisci i dettagli dell'operazione come JSON
            return operazione.__json__()
        else:
            return {"message": "Operazione non trovata"}

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'operazione: {str(e)}")
        return {}