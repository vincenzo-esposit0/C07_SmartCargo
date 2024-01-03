from src.models import Include
from src.models.IncludeDAO import IncludeDAO

# Creazione di un'istanza di IncludeDAO
include_dao = IncludeDAO()

# Ottieni tutti gli Include
print("Tutti gli Include:")
tutti_include = include_dao.ottieni_tutti_include()
for include_item in tutti_include:
    print(f"ID: {include_item.id}, Operazione ID: {include_item.operazione_id}, Merce ID: {include_item.merce_id}, Quantita: {include_item.quantita}")

# Ottieni un Include con ID 3
print("\nInclude con ID 3:")
include_id = 3
include_3 = include_dao.ottieni_include_per_id(include_id)
if include_3:
    print(f"ID: {include_3.id}, Operazione ID: {include_3.operazione_id}, Merce ID: {include_3.merce_id}, Quantita: {include_3.quantita}")
else:
    print(f"Nessun Include trovato con ID {include_id}")

# Inserisci un nuovo Include
nuovo_include = Include(operazione_id=1, merce_id=2, quantita=10)
include_dao.aggiungi_include(nuovo_include)

# Ottieni tutti gli Include dopo l'inserimento
print("\nTutti gli Include dopo l'inserimento:")
tutti_include_dopo = include_dao.ottieni_tutti_include()
for include_item in tutti_include_dopo:
    print(f"ID: {include_item.id}, Operazione ID: {include_item.operazione_id}, Merce ID: {include_item.merce_id}, Quantita: {include_item.quantita}")

# Elimina un Include (ad esempio, con ID 2)
include_da_eliminare_id = 2
include_dao.elimina_include(include_da_eliminare_id)

# Ottieni tutti gli Include dopo l'eliminazione
print("\nTutti gli Include dopo l'eliminazione:")
tutti_include_dopo_elim = include_dao.ottieni_tutti_include()
for include_item in tutti_include_dopo_elim:
    print(f"ID: {include_item.id}, Operazione ID: {include_item.operazione_id}, Merce ID: {include_item.merce_id}, Quantita: {include_item.quantita}")
