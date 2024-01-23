from datetime import datetime, timedelta
from src.dataManagement.services import OperazioneService
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
from src.models.OperazioneDAO import OperazioneDAO

autotrasportatore_dao = AutotrasportatoreDAO()
operazione_dao = OperazioneDAO()


def visualizzaStorico(filtri):
    try:
        operazioni_filtrate = []

        # ricerca solo delle operazioni il cui stato è chiuso
        operazioniJson = OperazioneService.ottieniOperazioniPerStorico()

        for operazioneJson in operazioniJson:
            corrispondenza = True

            # scomposizone dell'autotrasportatore
            autotrasportatoreJson = operazioneJson["autotrasportatore"]
            autotrasportatoreNomeCognome = f"{autotrasportatoreJson['nome']} {autotrasportatoreJson['cognome']}"
            autotrasportatoreAzienda = autotrasportatoreJson["azienda"]

            # scomposizione del veicolo
            veicoloJson = operazioneJson["veicolo"]
            veicoloTarga = veicoloJson["targa"]

            # scomposizione del intervallo
            opJson = operazioneJson["operazione"]
            dataOp = opJson["dataOperazione"]

            for chiave, valore in filtri.items():
                if valore == "" or valore is None:
                    continue
                if chiave == "autotrasportatore" and autotrasportatoreNomeCognome != valore:
                    corrispondenza = False
                    break
                elif chiave == "azienda" and autotrasportatoreAzienda != valore:
                    corrispondenza = False
                    break
                elif chiave == "targa" and veicoloTarga != valore:
                    corrispondenza = False
                    break
                elif chiave == "dataDa":
                    dataDa = datetime.strptime(valore, "%Y-%m-%dT%H:%M:%S.%fZ").date() + timedelta(days=1)
                    if dataOp < dataDa:
                        corrispondenza = False
                        break
                elif chiave == "dataA":
                    dataA = datetime.strptime(valore, "%Y-%m-%dT%H:%M:%S.%fZ").date() + timedelta(days=1)
                    if dataOp > dataA:
                        corrispondenza = False
                        break

            if corrispondenza:
                operazioni_filtrate.append(operazioneJson)

        return operazioni_filtrate

    except Exception as e:
        print(f"Errore durante il recupero delle operazioni per lo storico: {str(e)}")
        return {"message": "Errore durante l'ottenimento delle operazioni per lo storico"}
