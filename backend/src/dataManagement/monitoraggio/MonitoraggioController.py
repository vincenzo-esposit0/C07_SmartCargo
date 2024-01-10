from datetime import datetime, timedelta

from flask import jsonify
from src.dataManagement.service import OperazioneService, AutotrasportatoreService, IncludeService, MerceService
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
from src.models.OperazioneDAO import OperazioneDAO

autotrasportatore_dao = AutotrasportatoreDAO()
operazione_dao = OperazioneDAO()

def trova_operazioni_per_filtri(filtri):
    try:
        operazioni_filtrate = []

        #va messo il metodo giusto una volta aggiunte operazioni chiuse nel db
        operazioniJson = OperazioneService.ottieniTutteOperazioniConDettagli()

        for operazioneJson in operazioniJson:
            corrispondenza = True

            #scomposizone dell'autotrasportatore
            autotrasportatoreJson = operazioneJson["autotrasportatore"]
            autotrasportatoreNomeCognome = f"{autotrasportatoreJson['nome']} {autotrasportatoreJson['cognome']}"
            autotrasportatoreAzienda = autotrasportatoreJson["azienda"]

            #scomposizione del veicolo
            veicoloJson = operazioneJson["veicolo"]
            veicoloTarga = veicoloJson["targa"]

            #scomposizione del intervallo
            opJson = operazioneJson["operazione"]
            dataOp = opJson["dataOperazione"]

            for chiave, valore in filtri.items():
                if valore == "" or valore == None:
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


def aggiorna_stato_operazione(operazioneJson):
    try:
        operazione_id = operazioneJson["id"]
        operazione = operazione_dao.ottieni_operazione_per_id(operazione_id)

        if operazione:
            operazione.stato = operazioneJson["stato"]

            operazione_dao.aggiorna_operazione(operazione)

            return jsonify(operazione.__json__())

    except Exception as e:
        print(f"Errore durante l'aggiornamento dello stato dell'operazione: {str(e)}")
        return {}