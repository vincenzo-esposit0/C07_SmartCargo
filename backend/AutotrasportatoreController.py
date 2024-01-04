from datetime import date

from src.models.QrCode import QrCode
from src.models.QrCodeDAO import QrCodeDAO
from src.models.UtenteRegistrato import Autotrasportatore
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO

# Creazione di un'istanza di AutotrasportatoreDAO
autotrasportatore_dao = AutotrasportatoreDAO()

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

