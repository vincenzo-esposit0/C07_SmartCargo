from src.models.OperatoreMobileDAO import OperatoreMobileDAO

operatore_mobile_dao = OperatoreMobileDAO()

def ottieniTuttiOperatoriMobile():
    try:
        operatori_mobile = operatore_mobile_dao.ottieni_tutti_operatori_mobile()

        if operatori_mobile:
            # Utilizza una lista per ottenere una lista di JSON
            operatori_mobileJson = [operatore_mobile.__json__() for operatore_mobile in operatori_mobile]

            # Restituisce la lista di JSON come risultato
            return operatori_mobileJson
        else:
            return {"message": "Operatori Mobile non trovati"}

    except Exception as e:
        print(f"Errore durante l'ottenimento degli operatori Mobile: {str(e)}")
        return {}

def ottieniOperatoreMobile(operatore_mobile_id):
    try:
        operatore_mobile = operatore_mobile_dao.ottieni_operatore_mobile_per_id(operatore_mobile_id)

        if operatore_mobile:
            # Restituisci i dettagli dell'operatore Mobile come JSON
            return operatore_mobile.__json__()
        else:
            return {"message": "Operatore Mobile non trovato"}

    except Exception as e:
        print(f"Errore durante l'ottenimento dell'operatore Mobile: {str(e)}")
        return {}
