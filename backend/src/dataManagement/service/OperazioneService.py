from src.models.OperazioneDAO import OperazioneDAO

from src.dataManagement.service import MerceService
from src.dataManagement.service import AutotrasportatoreService
from src.dataManagement.service import VeicoloService
from src.dataManagement.service import IncludeService
from src.dataManagement.service import IssueService
from src.dataManagement.service import OperatoreMobileService

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

def ottieniOperazionePerId(operazione_id):
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
                autotrasportatore = AutotrasportatoreService.ottieniAutotrasportatorePerId(operazione.autotrasportatore_id)

                # Ottieni le informazioni del veicolo usando l'ID
                veicolo = VeicoloService.ottieniVeicoloPerId(operazione.veicolo_id)

                # Ottieni le informazioni dell'include usando l'ID dell'operazione
                include = IncludeService.ottieniIncludePerId(operazione.id)

                # Ottieni le informazioni della merce usando l'ID
                merce = MerceService.ottieniMercePerId(include.merce_id)

                # Ottieni le informazioni dell'issue usando l'ID dell'operazione così da individuare l'operatore mobile
                issue = IssueService.ottieniIssuePerId(operazione.id)
                if issue and issue.stato == "Aperta":
                    operatore_mobile = OperatoreMobileService.ottieniOperatoreMobilePerId(issue.operatoreMobile_id)

                """
                Crea un dizionario con le informazioni dell'operazione, autotrasportatore, veicolo, quantita merce e 
                operatore mobile se vi è una issue aperta a questa operazione
                """
                operazioneJson = {
                    "operazione": operazione.__json__(),
                    "autotrasportatore": autotrasportatore if autotrasportatore else None,
                    "veicolo": veicolo if veicolo else None,
                    "include": include if include else None,
                    "operatore_mobile": operatore_mobile if operatore_mobile else None,
                    "issue": issue if issue else None,
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