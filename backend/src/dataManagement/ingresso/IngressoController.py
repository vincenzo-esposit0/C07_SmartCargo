import random
from datetime import date

from flask import jsonify

from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO
from src.models.VeicoloDAO import VeicoloDAO
from src.models.OperatoreMagazzinoDAO import OperatoreMagazzinoDAO
from src.models.Operazione import Operazione
from src.models.OperazioneDAO import OperazioneDAO
from src.models.Include import Include
from src.models.IncludeDAO import IncludeDAO
from src.models.Veicolo import Veicolo

autotrasportatore_dao = AutotrasportatoreDAO()
veicolo_dao = VeicoloDAO()
operatoreMagazzino_dao = OperatoreMagazzinoDAO()
operazione_dao = OperazioneDAO()
include_dao = IncludeDAO()


def registrazioneIngresso(ingressoJson):
    try:
        percorsoId = None

        # scomposizione Json per l'operazione
        operazioneJson = ingressoJson["operazione"]
        tipoOperazioneJson = operazioneJson["tipo"]
        destinazioneOperazioneJson = ingressoJson["destinazione"]

        # scomposizione Json per la merce
        merceJson = ingressoJson["merci"]
        tipoMerceJson = merceJson["tipo"]

        # scomposizione Json per il veicolo
        veicoloJson = ingressoJson["veicolo"]
        modelloJson = veicoloJson["modello"]

        # scomposizione Json per l'autotrasportatore
        autotrasportatoreJson = ingressoJson["autotrasportatore"]

        # ricerca autotrasportatore per i parametri nome, cognome e azienda
        autotrasportatore = autotrasportatore_dao.get_autotrasportatore_per_ingresso(autotrasportatore_nome=autotrasportatoreJson["nome"],
                                                                                     autotrasportatore_cognome=autotrasportatoreJson["cognome"],
                                                                                     autotrasportatore_azienda=autotrasportatoreJson["azienda"])

        # controllo per definire il percorso associato
        if destinazioneOperazioneJson["nome"] == "M1":
            percorsoId = 1
        elif destinazioneOperazioneJson["nome"] == "M2":
            percorsoId = 2
        elif destinazioneOperazioneJson["nome"] == "M3":
            percorsoId = 3

        # Recupero tutti gli operatori di magazzino disponibili
        operatoriMagazzino_disponibili = operatoreMagazzino_dao.ottieni_tutti_operatori_magazzino()

        # Scelgo casualmente un operatore di magazzino tra quelli disponibili che viene assegnato all'operazione
        operatoreMagazzinoScelto = random.choice(operatoriMagazzino_disponibili)

        veicolo = Veicolo(
            targa=veicoloJson["targa"],
            descrizione="Camion",
            modello=modelloJson["modello"]
        )
        veicolo_dao.aggiungi_veicolo(veicolo)

        operazione = Operazione(
            dataOperazione=date.today(),
            tipo=tipoOperazioneJson["nome"],
            puntoDestinazione=destinazioneOperazioneJson["nome"],
            stato="In Corso",
            descrizione=operazioneJson["descrizione"],
            autotrasportatore_id=autotrasportatore.id,
            operatoreIngresso_id=ingressoJson["operatoreIngresso_id"],
            operatoreMagazzino_id=operatoreMagazzinoScelto.id,
            percorso_id=percorsoId,
            veicolo_id=veicolo.id
        )
        result = operazione_dao.aggiungi_operazione(operazione)

        include = Include(
            operazione_id=operazione.id,
            merce_id=tipoMerceJson["id"],
            quantita=merceJson["quantita"]
        )
        include_dao.aggiungi_include(include)
        return jsonify(result.__json__())

    except Exception as e:
        print(f"Errore durante la registrazione dell'ingresso: {str(e)}")
        return {"message": "Errore durante la registrazione dell'ingresso"}

