from flask import jsonify

from src.models.IncludeDAO import IncludeDAO
from src.models.VeicoloDAO import VeicoloDAO
from src.models.MerceDAO import MerceDAO
from src.models.Include import Include
from src.models.Operazione import Operazione
from src.models.OperazioneDAO import OperazioneDAO
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO

autotrasportatoreDao = AutotrasportatoreDAO()
operazioneDao = OperazioneDAO()
merceDao = MerceDAO()
veicoloDao = VeicoloDAO()
includeDao = IncludeDAO()

def registrazioneIngresso(ingressoJson):
    try:

        autotrasportatore = autotrasportatoreDao.get_autotrasportatore_per_ingresso(autotrasportatore_nome=ingressoJson["nome"],
                                                                                    autotrasportatore_cognome=ingressoJson["cognome"],
                                                                                    autotrasportatore_azienda=ingressoJson["azienda"])

        merceJson = ingressoJson["merci"]
        #serve solo id
        merce = merceDao.get_merce_per_ingresso(merce_tipo=merceJson["tipo"],
                                                merce_descrizione=ingressoJson["descrizione"])

        veicoloJson = ingressoJson["veicolo"]

        veicolo = veicoloDao.get_veicolo_per_ingresso(veicolo_modello=veicoloJson["modello"],
                                                      veicolo_targa=veicoloJson["targa"])

        operazione = Operazione(
            tipo=ingressoJson["tipo"],
            puntoDestinazione=ingressoJson["puntoDestinazione"],
            stato=ingressoJson["stato"],
            autotrasportatore_id=autotrasportatore.id,
            operatoreIngresso_id=ingressoJson["operatoreIngresso_id"],
            operatoreMagazzino_id=ingressoJson["operatoreMagazzino_id"],
            percorso_id=1,
            veicolo_id=veicolo.id
        )


        include = Include(
            operazione_id=operazione.id,
            merce_id=merce.id,
            quantita=ingressoJson["quantita"]
        )
        includeDao.aggiungi_include(include)
        result = operazioneDao.aggiungi_operazione(operazione)
        return jsonify(result.__json__())

    except Exception as e:
        print(f"Errore durante la registrazione dell'ingresso: {str(e)}")
        return {}


