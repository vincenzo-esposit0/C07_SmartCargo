from src.models.OperazioneDAO import OperazioneDAO

operazione_dao = OperazioneDAO()

def ottieniOperazioni():
    try:
        operazioni = operazione_dao.ottieni_tutte_operazioni()

        if operazioni:
            # Restituisci i dettagli delle operazioni come JSON
            return operazioni.__json__()
        else:
            return {"message": "Operazioni non trovate"}

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni: {str(e)}")
        return {}
