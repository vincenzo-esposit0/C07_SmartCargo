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

def registrazioneIngresso(ingressoJson):
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