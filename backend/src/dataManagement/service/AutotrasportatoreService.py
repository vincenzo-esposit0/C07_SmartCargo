from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO

autotrasportatore_dao = AutotrasportatoreDAO()

def ottieniTuttiAutotrasportatori():
    try:
        autotrasportatori = autotrasportatore_dao.ottieni_tutti_autotrasportatori()

        if autotrasportatori:
            # Utilizza una lista per ottenere una lista di JSON
            autotrasportatoriJson = [autotrasportatore.__json__() for autotrasportatore in autotrasportatori]

            # Restituisce la lista di JSON come risultato
            return autotrasportatoriJson
        else:
            return {"message": "Autotrasportatori non trovati"}

    except Exception as e:
        print(f"Errore durante l'ottenimento degli autotrasportatori: {str(e)}")
        return {}

def ottieniAutotrasportatore(autotrasportatore_id):
    try:
        autotrasportatore = autotrasportatore_dao.ottieni_autotrasportatore_per_id(autotrasportatore_id)

        if autotrasportatore:
            # Restituisci i dettagli dell'autotrasportatore come JSON
            return autotrasportatore.__json__()
        else:
            return {"message": "Autotrasportatore non trovato"}

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'autotrasportatore: {str(e)}")
        return {}