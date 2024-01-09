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

def ottieniAutotrasportatorePerId(autotrasportatore_id):
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

def AutotrasportatoreByIdQrCode(qrCode_id):
    try:
        autotrasportatore = autotrasportatore_dao.ottieni_Autotrasportatore_By_IdQrCode(qrCode_id)

        if autotrasportatore:
            return autotrasportatore.__json__()
        else:
            return {"message": "Autotrasportatore non trovato"}

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'autotrasportatore: {str(e)}")
        return {}

def AutotrasportatoreByFilter(nome, cognome):
    try:
        autotrasportatore = autotrasportatore_dao.getAutotrasportatoreByFilter(nome, cognome)

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'autotrasportatore: {str(e)}")
        return {}

"""def allAut(nome, cognome):
    try:
        aut_trovati=[]
        results = autotrasportatore_dao.ottieni_tutti_autotrasportatori()

        if results:
            for a in results:
                if a.nome == nome or a.cognome == cognome:
                    aut_trovati.append(a)

        if aut_trovati:
            return aut_trovati
        else:
            print(f"Errore durante l'ottenimento dell'autotrasportatore")

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'autotrasportatore: {str(e)}")
        return {}

    prova = allAut("Marco", "Rossi")
    print(prova)"""