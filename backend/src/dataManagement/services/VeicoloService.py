from backend.src.models.VeicoloDAO import VeicoloDAO

veicolo_dao = VeicoloDAO()

def ottieniTuttiVeicoli():
    try:
        veicoli = veicolo_dao.ottieni_tutti_veicoli()

        if veicoli:
            # Utilizza una lista per ottenere una lista di JSON
            veicoliJson = [veicolo.__json__() for veicolo in veicoli]

            # Restituisce la lista di JSON come risultato
            return veicoliJson
        else:
            return {"message": "Veicoli non trovati"}

    except Exception as e:
        print(f"Errore durante l'ottenimento dei veicoli: {str(e)}")
        return {}

def ottieniVeicoloPerId(veicolo_id):
    try:
        veicolo = veicolo_dao.ottieni_veicolo_per_id(veicolo_id)

        if veicolo:
            # Restituisce i dettagli del veicolo come JSON
            return veicolo.__json__()
        else:
            return {"message": "Veicolo non trovato"}

    except Exception as e:
        print(f"Errore durante l'ottenimento del veicolo: {str(e)}")
        return {}
