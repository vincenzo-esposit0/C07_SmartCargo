from backend.src.models.Veicolo import Veicolo
from backend.src.models.VeicoloDAO import VeicoloDAO

# Creazione di un'istanza di VeicoloDAO
veicolo_dao = VeicoloDAO()

# Ottieni tutti i veicoli
print("Tutti i veicoli:")
tutti_veicoli = veicolo_dao.ottieni_tutti_veicoli()
for veicolo in tutti_veicoli:
    print(f"ID: {veicolo.id}, Targa: {veicolo.targa}, Modello: {veicolo.modello}, Descrizione: {veicolo.descrizione}")

# Ottieni un veicolo con ID 3
print("\nVeicolo con ID 3:")
veicolo_id = 3
veicolo_3 = veicolo_dao.ottieni_veicolo_per_id(veicolo_id)
if veicolo_3:
    print(f"ID: {veicolo_3.id}, Targa: {veicolo_3.targa}, Modello: {veicolo_3.modello}, Descrizione: {veicolo_3.descrizione}")
else:
    print(f"Nessun veicolo trovato con ID {veicolo_id}")

# Inserisci un nuovo veicolo
nuovo_veicolo = Veicolo(targa='XYZ123', modello='Nuovo Modello', descrizione='Descrizione del nuovo veicolo')
veicolo_dao.aggiungi_veicolo(nuovo_veicolo)

# Ottieni tutti i veicoli dopo l'inserimento
print("\nTutti i veicoli dopo l'inserimento:")
tutti_veicoli_dopo = veicolo_dao.ottieni_tutti_veicoli()
for veicolo in tutti_veicoli_dopo:
    print(f"ID: {veicolo.id}, Targa: {veicolo.targa}, Modello: {veicolo.modello}, Descrizione: {veicolo.descrizione}")

# Elimina un veicolo (ad esempio, con ID 2)
veicolo_da_eliminare_id = 2
veicolo_dao.elimina_veicolo(veicolo_da_eliminare_id)

# Ottieni tutti i veicoli dopo l'eliminazione
print("\nTutti i veicoli dopo l'eliminazione:")
tutti_veicoli_dopo_elim = veicolo_dao.ottieni_tutti_veicoli()
for veicolo in tutti_veicoli_dopo_elim:
    print(f"ID: {veicolo.id}, Targa: {veicolo.targa}, Modello: {veicolo.modello}, Descrizione: {veicolo.descrizione}")