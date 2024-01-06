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



def ottieniTutteOperazioniConDettagli():
    global operatore_mobile
    try:
        operazioni = operazione_dao.ottieni_tutte_operazioni()

        if operazioni:
            operazioniJson = []
            for operazione in operazioni:
                operatore_mobile = None

                # Ottieni le informazioni dell'autotrasportatore usando l'ID
                autotrasportatore = autotrasportatore_dao.ottieni_autotrasportatore_per_id(operazione.autotrasportatore_id)

                # Ottieni le informazioni del veicolo usando l'ID
                veicolo = veicolo_dao.ottieni_veicolo_per_id(operazione.veicolo_id)

                # Ottieni le informazioni dell'include usando l'ID dell'operazione
                include = include_dao.ottieni_include_per_operazione_id(operazione.id)

                merce = MerceController.ottieniMerceId(include.merce_id)

                # Ottieni le informazioni dell'issue usando l'ID dell'operazione così da individuare l'operatore mobile
                issue = issue_dao.ottieni_issue_per_operazione_id(operazione.id)
                if issue and issue.stato == "Aperta":
                    operatore_mobile = operatore_mobile_dao.ottieni_operatore_mobile_per_id(issue.operatoreMobile_id)

                """
                Crea un dizionario con le informazioni dell'operazione, autotrasportatore, veicolo, quantita merce e 
                operatore mobile se vi è una issue aperta a questa operazione
                """
                operazioneJson = {
                    "operazione": operazione.__json__(),
                    "autotrasportatore": autotrasportatore.__json__() if autotrasportatore else None,
                    "veicolo": veicolo.__json__() if veicolo else None,
                    "include": include.__json__() if include else None,
                    "operatore_mobile": operatore_mobile.__json__() if operatore_mobile else None,
                    "issue": issue.__json__() if issue else None,
                    "merce": merce
                }

                # Aggiungi il dizionario alla lista di risultati
                operazioniJson.append(operazioneJson)

            # Restituisce la lista di JSON come risultato
            return operazioniJson
        else:
            return {"message": "Operazioni non trovate"}

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni: {str(e)}")
        return {}