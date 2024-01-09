from src.dataManagement.service import OperazioneService, AutotrasportatoreService, IncludeService, MerceService
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
from backend.src.models.OperazioneDAO import OperazioneDAO

autotrasportatore_dao = AutotrasportatoreDAO()
operazione_dao = OperazioneDAO()

def storicoOperazioniPerAutotrasportatore(storicoJson):
    try:
        autotrasportatotoreJson = storicoJson["autotrasportatore"]
        autotrasportatore = autotrasportatore_dao.ottieni_autotrasportatore_per_nomeCognome(autotrasportatotoreJson["nome"],
                                                                                            autotrasportatotoreJson["cognome"])

        operazioniJson = OperazioneService.ottieniOperazioniConDettagliPerAutotrasportatore(autotrasportatore.id)
        return operazioniJson

    except Exception as e:
        print(f"Errore durante il recupero delle operazioni: {str(e)}")
        return {}

def storicoOperazioniPerIssue(storicoJson):
    try:
        operazioniJson = OperazioneService.ottieniOperazioniConDettagliPerIssue(storicoJson["issueAperte"])
        return operazioniJson

    except Exception as e:
        print(f"Errore durante il recupero delle operazioni: {str(e)}")
        return {}


def ottieni_tutte_Operazioni_e_Merci():
    try:
        operazioni = operazione_dao.ottieni_operazioni_per_stato("In corso / Regolare")

        if operazioni:
            operazioniJson = []
            for operazione in operazioni:

                # Ottieni le informazioni dell'autotrasportatore usando l'ID
                autotrasportatore = AutotrasportatoreService.ottieniAutotrasportatorePerId(operazione.autotrasportatore_id)

                include = IncludeService.ottieniIncludePerIdOperazione(operazione.id)

                # Ottieni le informazioni della merce usando l'ID
                merce = MerceService.ottieniMercePerId(include["merce_id"])

                operazioneJson = {
                    "operazione": operazione.__json__(),
                    "autotrasportatore": autotrasportatore,
                    "merce":  merce,
                }

                operazioniJson.append(operazioneJson)

            # Restituisce la lista di JSON come risultato
            return operazioniJson
        else:
            return {"message": "Operazioni non trovate"}

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni: {str(e)}")
        return {}