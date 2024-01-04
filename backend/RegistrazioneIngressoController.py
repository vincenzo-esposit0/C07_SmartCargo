from flask import jsonify

from src.models.IncludeDAO import IncludeDAO
from src.models.VeicoloDAO import VeicoloDAO
from src.models.Include import Include
from src.models.Operazione import Operazione
from src.models.OperazioneDAO import OperazioneDAO
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO

autotrasportatoreDao = AutotrasportatoreDAO()
operazioneDao = OperazioneDAO()
veicoloDao = VeicoloDAO()
includeDao = IncludeDAO()

def registrazioneIngresso(ingressoJson):
    try:
        autotrasportatoreJson = ingressoJson["autotrasportatore"]
        autotrasportatore = autotrasportatoreDao.get_autotrasportatore_per_ingresso(autotrasportatore_nome=autotrasportatoreJson["nome"],
                                                                                    autotrasportatore_cognome=autotrasportatoreJson["cognome"],
                                                                                    autotrasportatore_azienda=autotrasportatoreJson["azienda"])

        merceJson = ingressoJson["merci"]

        veicoloJson = ingressoJson["veicolo"]

        veicolo = veicoloDao.get_veicolo_per_ingresso(veicolo_modello=veicoloJson["modello"],
                                                      veicolo_targa=veicoloJson["targa"])

        operazione = Operazione(
            tipo=ingressoJson["tipo"],
            puntoDestinazione=ingressoJson["destinazione"],
            stato="In Corso",
            autotrasportatore_id=autotrasportatore.id,
            operatoreIngresso_id=ingressoJson["operatoreIngresso_id"],
            operatoreMagazzino_id=1, #è un campo not null in operazione
            percorso_id=1,
            veicolo_id=veicolo.id
        )


        include = Include(
            operazione_id=operazione.id,
            merce_id=merceJson["merce_id"],
            quantita=merceJson["quantita"]
        )
        includeDao.aggiungi_include(include)
        result = operazioneDao.aggiungi_operazione(operazione)
        return jsonify(result.__json__())

    except Exception as e:
        print(f"Errore durante la registrazione dell'ingresso: {str(e)}")
        return {}


