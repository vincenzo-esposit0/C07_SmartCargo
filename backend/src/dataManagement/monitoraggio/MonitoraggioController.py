from backend.src.dataManagement.service import OperazioneService
from backend.src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
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


