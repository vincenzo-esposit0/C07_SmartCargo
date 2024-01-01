from backend.src.models.Merce import Merce
from backend.src.models.MerceDAO import MerceDAO

# Creazione di un'istanza di MerceDAO
merce_dao = MerceDAO()

# Ottieni tutte le merci
print("Tutte le merci:")
tutte_merci = merce_dao.ottieni_tutte_merci()
for merce in tutte_merci:
    print(f"ID: {merce.id}, Tipo: {merce.tipo}, Descrizione: {merce.descrizione}")

# Ottieni la merce con ID 3
print("\nMerce con ID 3:")
merce_id = 3
merce_3 = merce_dao.ottieni_merce_per_id(merce_id)
if merce_3:
    print(f"ID: {merce_3.id}, Tipo: {merce_3.tipo}, Descrizione: {merce_3.descrizione}")
else:
    print(f"Nessuna merce trovata con ID {merce_id}")

# Inserisci la nuova merce
nuova_merce = Merce(Tipo='merce', descrizione='Descrizione della merce')
merce_dao.aggiungi_merce(nuova_merce)

# Ottieni tutte le merci dopo l'inserimento
print("\nTutte le merci dopo l'inserimento: ")
tutte_merci_dopo = merce_dao.ottieni_tutte_merci()
for merce in tutte_merci_dopo:
    print(f"ID: {merce.id}, Tipo: {merce.tipo}, Descrizione: {merce.descrizione}")

# Elimina una merce (ad esempio, con ID 2)
merce_da_eliminare_id = 2
merce_dao.elimina_merce(merce_da_eliminare_id)

# Ottieni tutte le merci dopo l'eliminazione
print("\nTutti le merci dopo l'eliminazione:")
tutte_merci_dopo_elim = merce_dao.ottieni_tutte_merci()
for merce in tutte_merci_dopo_elim:
    print(f"ID: {merce.id}, Tipo: {merce.tipo}, Descrizione: {merce.descrizione}")