from src.models.OperazioneDAO import OperazioneDAO

from src.dataManagement.services import MerceService
from src.dataManagement.services import AutotrasportatoreService
from src.dataManagement.services import IncludeService
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO

from src.dataManagement.InterfaceFacade import InterfaceFacade

operazione_dao = OperazioneDAO()
autotrasportatore_dao = AutotrasportatoreDAO()
opDatiFacade = InterfaceFacade()

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
        return {"message": "Errore durante l'ottenimento delle operazioni"}

def ottieniTutteOperazioniConDettagli():
    try:
        operazioni = operazione_dao.ottieni_tutte_operazioni()

        operazioniJson = ottieniAlcuneOperazioniConDettagli(operazioni)
        return operazioniJson

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni per lo storico: {str(e)}")
        return {"message": "Errore durante l'ottenimento delle operazioni per lo storico"}

def ottieniAlcuneOperazioniConDettagli(operazioni):
    try:
        operazioni = operazioni

        if operazioni:
            operazioniJson = []
            for operazione in operazioni:
                autotrasportatore, veicolo, include, operatore_mobile, operatore_sala, issue, merce, percorso = opDatiFacade.ottieniInfoOperazione(operazione)

                operazioneJson = {
                    "operazione": operazione.__json__(),
                    "autotrasportatore": autotrasportatore.__json__() if autotrasportatore else None,
                    "veicolo": veicolo.__json__() if veicolo else None,
                    "include":  include.__json__(),
                    "operatore_mobile": operatore_mobile.__json__() if operatore_mobile else None,
                    "operatore_sala": operatore_sala.__json__() if operatore_sala else None,
                    "issue": issue.__json__() if issue else None,
                    "merce": merce.__json__(),
                    "percorso": percorso.__json__()
                }

                # Aggiungi il dizionario alla lista di risultati
                operazioniJson.append(operazioneJson)

            # Restituisce la lista di JSON come risultato
            return operazioniJson
        else:
            return {"message": "Operazioni non trovate"}

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni: {str(e)}")
        return {"message": "Errore durante l'ottenimento delle operazioni"}

def ottieniOperazioniPerStorico():
    try:
        operazioni = operazione_dao.ottieni_operazioni_per_stato("Chiuso")

        operazioniJson = ottieniAlcuneOperazioniConDettagli(operazioni)
        return operazioniJson

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni per lo storico: {str(e)}")
        return {"message": "Errore durante l'ottenimento delle operazioni per lo storico"}

def ottieniOperazioniPerOpAttive():
    try:
        operazioni = operazione_dao.ottieni_operazioni_per_stato("In corso")

        operazioniJson = ottieniAlcuneOperazioniConDettagli(operazioni)
        return operazioniJson

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni per operazioni attive: {str(e)}")
        return {"message": "Errore durante l'ottenimento delle operazioni attive "}

def ottieniOperazioniConDettagliPerAutotrasportatore(autotrasportatore_id):
    try:
        operazioni = operazione_dao.ottieni_operazioni_per_idAutotrasportatore(autotrasportatore_id)

        operazioniJson = ottieniAlcuneOperazioniConDettagli(operazioni)
        return operazioniJson

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni per l'autotrasportatore: {str(e)}")
        return {"message": "Errore durante l'ottenimento delle operazioni per l'autotrasportatore"}


def ottieniOperazioniConDettagliPerOpMagazzino(operatore_magazzino_id):
    try:
        operazioni = operazione_dao.ottieni_operazioni_per_id_OpMagazzino(operatore_magazzino_id)
        operazioniJson = ottieniAlcuneOperazioniConDettagli(operazioni)
        return operazioniJson

    except Exception as e:
        print(f"Errore durante l'ottenimento delle operazioni: {str(e)}")
        return {"message": "Errore durante l'ottenimento delle operazioni"}

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
        return {"message": "Errore durante l'ottenimento delle operazioni"}

def ottieniOperazionePerId(operazione_id):
    try:
        if operazione_id is not None and operazione_id > 0:
            operazione = operazione_dao.ottieni_operazione_per_id(operazione_id)

            if operazione:
                # Restituisci i dettagli dell'operazione come JSON
                return operazione.__json__()
            else:
                return {"message": "Operazione non trovata"}

        elif operazione_id == None or operazione_id < 0:
            return {"message": "Errore: ID Operazione non valido"}

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'operazione: {str(e)}")
        return {"message": "Errore durante l'ottenimento delle operazione"}

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
        return {"message": "Errore durante l'ottenimento delle operazioni"}