from src.models.OperazioneDAO import OperazioneDAO

from src.dataManagement.service import MerceService
from src.dataManagement.service import AutotrasportatoreService
from src.dataManagement.service import VeicoloService
from src.dataManagement.service import IncludeService
from src.dataManagement.service import IssueService
from src.dataManagement.service import OperatoreMobileService
from src.dataManagement.service import PercorsoService
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO

operazione_dao = OperazioneDAO()
autotrasportatore_dao = AutotrasportatoreDAO()

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

def ottieniTutteOperazioniConDettagli():
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
                include = IncludeService.ottieniIncludePerIdOperazione(operazione.id)

                # Ottieni le informazioni della merce usando l'ID
                merce = MerceService.ottieniMercePerId(include["merce_id"])

                # Ottieni le informazioni dell'issue usando l'ID dell'operazione così da individuare l'operatore mobile
                issue = IssueService.ottieniIssuePerIdOperazione(operazione.id)

                #Ottieni le informazioni sul percorso usando l'id
                percorso = PercorsoService.ottieniPercorsoPerId(operazione.percorso_id)

                if issue is not None and issue != {}:
                    operatore_mobile = OperatoreMobileService.ottieniOperatoreMobilePerId(issue["operatoreMobile_id"])


                operazioneJson = {
                    "operazione": operazione.__json__(),
                    "autotrasportatore": autotrasportatore,
                    "veicolo": veicolo,
                    "include":  include,
                    "operatore_mobile": operatore_mobile if operatore_mobile else None,
                    "issue": issue if issue else None,
                    "merce": merce,
                    "percorso": percorso
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

def ottieniAlcuneOperazioniConDettagli(operazioni):
    try:
        operazioni = operazioni

        if operazioni:
            operazioniJson = []
            for operazione in operazioni:
                operatore_mobile = None

                # Ottieni le informazioni dell'autotrasportatore usando l'ID
                autotrasportatore = AutotrasportatoreService.ottieniAutotrasportatorePerId(operazione.autotrasportatore_id)

                # Ottieni le informazioni del veicolo usando l'ID
                veicolo = VeicoloService.ottieniVeicoloPerId(operazione.veicolo_id)

                # Ottieni le informazioni dell'include usando l'ID dell'operazione
                include = IncludeService.ottieniIncludePerIdOperazione(operazione.id)

                # Ottieni le informazioni della merce usando l'ID
                merce = MerceService.ottieniMercePerId(include["merce_id"])

                # Ottieni le informazioni dell'issue usando l'ID dell'operazione così da individuare l'operatore mobile
                issue = IssueService.ottieniIssuePerIdOperazione(operazione.id)

                #Ottieni le informazioni sul percorso usando l'id
                percorso = PercorsoService.ottieniPercorsoPerId(operazione.percorso_id)

                if issue is not None and issue != {}:
                    operatore_mobile = OperatoreMobileService.ottieniOperatoreMobilePerId(issue["operatoreMobile_id"])


                operazioneJson = {
                    "operazione": operazione.__json__(),
                    "autotrasportatore": autotrasportatore if autotrasportatore else None,
                    "veicolo": veicolo if veicolo else None,
                    "include":  include,
                    "operatore_mobile": operatore_mobile if operatore_mobile else None,
                    "issue": issue if issue else None,
                    "merce": merce,
                    "percorso": percorso
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

def ottieniOperazioniPerStorico():
    try:
        operazioni = operazione_dao.ottieni_operazioni_per_stato("Chiuso")

        operazioniJson = ottieniAlcuneOperazioniConDettagli(operazioni)
        return operazioniJson

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni per lo storico: {str(e)}")
        return {}

def ottieniOperazioniPerOpAttive():
    try:
        operazioni = operazione_dao.ottieni_operazioni_per_stato("In corso")

        operazioniJson = ottieniAlcuneOperazioniConDettagli(operazioni)
        return operazioniJson

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni per operazioni attive: {str(e)}")
        return {}

def ottieniOperazioniConDettagliPerAutotrasportatore(autotrasportatore_id):
    try:
        operazioni = operazione_dao.ottieni_operazioni_per_idAutotrasportatore(autotrasportatore_id)

        operazioniJson = ottieniAlcuneOperazioniConDettagli(operazioni)
        return operazioniJson

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni: {str(e)}")
        return {}


def ottieniOperazioniConDettagliPerOpMagazzino(operatore_magazzino_id):
    try:
        operazioni = operazione_dao.ottieni_operazioni_per_id_OpMagazzino(operatore_magazzino_id)
        operazioniJson = ottieniAlcuneOperazioniConDettagli(operazioni)
        return operazioniJson

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni: {str(e)}")
        return {}

def ottieniOperazioniConDettagliPerIssue(issue_stato):
    try:
        operazioni = None
        if issue_stato == True:
            operazioni = operazione_dao.ottieni_operazioni_per_stato("In corso / Issue aperta")
        elif issue_stato == False:
            operazioni = operazione_dao.ottieni_operazioni_per_stato("In corso / Regolare")

        operazioniJson = ottieniAlcuneOperazioniConDettagli(operazioni)
        return operazioniJson

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
