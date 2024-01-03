from backend.src.models.Operazione import Operazione
from backend.src.models.OperazioneDAO import OperazioneDAO

# Creazione di un'istanza di OperazioneDAO
operazione_dao = OperazioneDAO()

# Ottieni tutte le operazioni
print("Tutte le operazioni:")
tutte_operazioni = operazione_dao.ottieni_tutte_operazioni()
for operazione in tutte_operazioni:
    print(f"ID: {operazione.id}, Tipo: {operazione.tipo}, Descrizione: {operazione.descrizione}, Punto Destinazione: {operazione.puntoDestinazione}, Stato: {operazione.stato}")

# Ottieni un'operazione con ID 1
print("\nOperazione con ID 1:")
operazione_id = 1
operazione_1 = operazione_dao.ottieni_operazione_per_id(operazione_id)
if operazione_1:
    print(f"ID: {operazione_1.id}, Tipo: {operazione_1.tipo}, Descrizione: {operazione_1.descrizione}, Punto Destinazione: {operazione_1.puntoDestinazione}, Stato: {operazione_1.stato}")
else:
    print(f"Nessuna operazione trovata con ID {operazione_id}")

# Inserisci una nuova operazione
nuova_operazione = Operazione(tipo="Carico", puntoDestinazione="Magazzino A", stato="In corso")
operazione_dao.aggiungi_operazione(nuova_operazione)

# Ottieni tutte le operazioni dopo l'inserimento
print("\nTutte le operazioni dopo l'inserimento:")
tutte_operazioni_dopo = operazione_dao.ottieni_tutte_operazioni()
for operazione in tutte_operazioni_dopo:
    print(f"ID: {operazione.id}, Tipo: {operazione.tipo}, Descrizione: {operazione.descrizione}, Punto Destinazione: {operazione.puntoDestinazione}, Stato: {operazione.stato}")

# Elimina un'operazione (ad esempio, con ID 2)
operazione_da_eliminare_id = 2
operazione_dao.elimina_operazione(operazione_da_eliminare_id)

# Ottieni tutte le operazioni dopo l'eliminazione
print("\nTutte le operazioni dopo l'eliminazione:")
tutte_operazioni_dopo_elim = operazione_dao.ottieni_tutte_operazioni()
for operazione in tutte_operazioni_dopo_elim:
    print(f"ID: {operazione.id}, Tipo: {operazione.tipo}, Descrizione: {operazione.descrizione}, Punto Destinazione: {operazione.puntoDestinazione}, Stato: {operazione.stato}")
