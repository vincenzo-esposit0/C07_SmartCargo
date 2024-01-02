from backend.src.models.Percorso import Percorso
from backend.src.models.PercorsoDAO import PercorsoDAO

# Creazione di un'istanza di PercorsoDAO
percorso_dao = PercorsoDAO()

# Ottieni tutti i percorsi
print("Tutti i percorsi:")
tutti_percorsi = percorso_dao.ottieni_tutti_percorsi()
for percorso in tutti_percorsi:
    print(f"ID: {percorso.id}, Punti Latitudine Corretti: {percorso.puntiLatitudineCorretti}, Punti Longitudine Corretti: {percorso.puntiLongitudineCorretti}, Punti Latitudine Percorsi: {percorso.puntiLatitudinePercorsi}, Punti Longitudine Percorsi: {percorso.puntiLongitudinePercorsi}")

# Ottieni un percorso con ID 1
print("\nPercorso con ID 1:")
percorso_id = 1
percorso_1 = percorso_dao.ottieni_percorso_per_id(percorso_id)
if percorso_1:
    print(f"ID: {percorso_1.id}, Punti Latitudine Corretti: {percorso_1.puntiLatitudineCorretti}, Punti Longitudine Corretti: {percorso_1.puntiLongitudineCorretti}, Punti Latitudine Percorsi: {percorso_1.puntiLatitudinePercorsi}, Punti Longitudine Percorsi: {percorso_1.puntiLongitudinePercorsi}")
else:
    print(f"Nessun percorso trovato con ID {percorso_id}")

# Inserisci un nuovo percorso
nuovo_percorso = Percorso(puntiLatitudineCorretti=12.345678, puntiLongitudineCorretti=45.678901, puntiLatitudinePercorsi=23.456789, puntiLongitudinePercorsi=56.789012)
percorso_dao.aggiungi_percorso(nuovo_percorso)

# Ottieni tutti i percorsi dopo l'inserimento
print("\nTutti i percorsi dopo l'inserimento:")
tutti_percorsi_dopo = percorso_dao.ottieni_tutti_percorsi()
for percorso in tutti_percorsi_dopo:
    print(f"ID: {percorso.id}, Punti Latitudine Corretti: {percorso.puntiLatitudineCorretti}, Punti Longitudine Corretti: {percorso.puntiLongitudineCorretti}, Punti Latitudine Percorsi: {percorso.puntiLatitudinePercorsi}, Punti Longitudine Percorsi: {percorso.puntiLongitudinePercorsi}")

# Elimina un percorso (ad esempio, con ID 2)
percorso_da_eliminare_id = 2
percorso_dao.elimina_percorso(percorso_da_eliminare_id)

# Ottieni tutti i percorsi dopo l'eliminazione
print("\nTutti i percorsi dopo l'eliminazione:")
tutti_percorsi_dopo_elim = percorso_dao.ottieni_tutti_percorsi()
for percorso in tutti_percorsi_dopo_elim:
    print(f"ID: {percorso.id}, Punti Latitudine Corretti: {percorso.puntiLatitudineCorretti}, Punti Longitudine Corretti: {percorso.puntiLongitudineCorretti}, Punti Latitudine Percorsi: {percorso.puntiLatitudinePercorsi}, Punti Longitudine Percorsi: {percorso.puntiLongitudinePercorsi}")
