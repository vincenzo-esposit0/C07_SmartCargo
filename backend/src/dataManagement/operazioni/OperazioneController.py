from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
from src.models.OperazioneDAO import OperazioneDAO
from backend.src.dataManagement.service import OperazioneService

def storicoDelleOperazioni(filtriOp):
    try:
        autotrasportatoreNome = filtriOp.get("Nome")
        autotrasportatoreCognome = filtriOp.get("Cognome")
        dataInizio = filtriOp.get("dataInizio")
        dataFine = filtriOp.get("dataFine")
        statoIssue = filtriOp.get("statoIssue")

        results = OperazioneService.getOpByFilter(autotrasportatoreNome, autotrasportatoreCognome, dataInizio, dataFine, statoIssue)

    except Exception as e:
        print(f"Errore durante il recupero delle operazioni: {str(e)}")
        return {}