import random

from flask import jsonify

from src.models.IncludeDAO import IncludeDAO
from src.models.VeicoloDAO import VeicoloDAO
from src.models.Include import Include
from src.models.Operazione import Operazione
from src.models.OperazioneDAO import OperazioneDAO
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
from src.models.OperatoreMagazzinoDAO import OperatoreMagazzinoDAO

autotrasportatore_dao = AutotrasportatoreDAO()
operazione_dao = OperazioneDAO()
veicolo_dao = VeicoloDAO()
include_dao = IncludeDAO()
operatoreMagazzino_dao = OperatoreMagazzinoDAO

def registrazioneOperazione(ingressoJson):
    try:
        autotrasportatoreJson = ingressoJson["autotrasportatore"]
        autotrasportatore = autotrasportatore_dao.get_autotrasportatore_per_ingresso(autotrasportatore_nome=autotrasportatoreJson["nome"],
                                                                                     autotrasportatore_cognome=autotrasportatoreJson["cognome"],
                                                                                     autotrasportatore_azienda=autotrasportatoreJson["azienda"])

        merceJson = ingressoJson["merci"]

        veicoloJson = ingressoJson["veicolo"]

        veicolo = veicolo_dao.get_veicolo_per_ingresso(veicolo_modello=veicoloJson["modello"],
                                                       veicolo_targa=veicoloJson["targa"])

        #Recupero tutti gli operatori di magazzino disponibili
        operatoriMagazzino_disponibili = operatoreMagazzino_dao.ottieni_tutti_operatori_magazzino()

        #Scelgo casualmente un operatore di magazzino tra quelli disponibili che viene assegnato all'operazione
        operatoreMagazzinoScelto = random.choice(operatoriMagazzino_disponibili)

        operazione = Operazione(
            tipo=ingressoJson["tipo"],
            puntoDestinazione=ingressoJson["destinazione"],
            stato="In Corso",
            autotrasportatore_id=autotrasportatore.id,
            operatoreIngresso_id=ingressoJson["operatoreIngresso_id"],
            operatoreMagazzino_id=operatoreMagazzinoScelto.id,
            percorso_id=1, #da rivedere
            veicolo_id=veicolo.id
        )
        result = operazione_dao.aggiungi_operazione(operazione)

        include = Include(
            operazione_id=operazione.id,
            merce_id=merceJson["merce_id"],
            quantita=merceJson["quantita"]
        )
        include_dao.aggiungi_include(include)
        return jsonify(result.__json__())

    except Exception as e:
        print(f"Errore durante la registrazione dell'ingresso: {str(e)}")
        return {}

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
    try:
        operazioni = operazione_dao.ottieni_tutte_operazioni()

        if operazioni:
            operazioniJson = []
            for operazione in operazioni:
                # Ottieni le informazioni dell'autotrasportatore usando l'ID
                autotrasportatore = autotrasportatore_dao.ottieni_autotrasportatore_per_id(operazione.autotrasportatore_id)

                # Ottieni le informazioni del veicolo usando l'ID
                veicolo = veicolo_dao.ottieni_veicolo_per_id(operazione.veicolo_id)

                # Crea un dizionario con le informazioni dell'operazione, autotrasportatore e veicolo
                operazioneJson = {
                    "operazione": operazione.__json__(),
                    "autotrasportatore": autotrasportatore.__json__() if autotrasportatore else None,
                    "veicolo": veicolo.__json__() if veicolo else None
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
