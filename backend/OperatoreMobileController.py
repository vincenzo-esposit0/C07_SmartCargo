from src.models.UtenteRegistrato import OperatoreMobile
from src.models.OperatoreMobileDAO import OperatoreMobileDAO

# Creazione di un'istanza di OperatoreMobileDAO
operatore_mobile_dao = OperatoreMobileDAO()

# Ottieni tutti gli operatori mobili
print("Tutti gli operatori mobili:")
tutti_operatori_mobili = operatore_mobile_dao.ottieni_tutti_operatori_mobili()
for operatore_mobile in tutti_operatori_mobili:
    print(f"ID: {operatore_mobile.id}, Nome: {operatore_mobile.nome}, Cognome: {operatore_mobile.cognome}")

# Ottieni l'operatore mobile con ID 1
print("\nOperatore mobile con ID 1:")
operatore_mobile_id = 1
operatore_mobile_1 = operatore_mobile_dao.ottieni_operatore_mobile_per_id(operatore_mobile_id)
if operatore_mobile_1:
    print(f"ID: {operatore_mobile_1.id}, Nome: {operatore_mobile_1.nome}, Cognome: {operatore_mobile_1.cognome}")
else:
    print(f"Nessun operatore mobiletrovato con ID {operatore_mobile_id}")

# Inserisci il nuovo operatore di sala
nuovo_operatore_mobile = OperatoreMobile(nome='Nuovo', cognome='Operatore', dataNascita='1990-01-01',
                                     codiceFiscale='ABC12345', email='nuovo@operatore.it',
                                     password='password', indirizzo='Indirizzo')
operatore_mobile_dao.aggiungi_operatore_mobile(nuovo_operatore_mobile)

# Ottieni tutti gli operatori mobili dopo l'inserimento
print("\nTutti gli operatori mobili dopo l'inserimento:")
tutti_operatori_mobili_dopo = operatore_mobile_dao.ottieni_tutti_operatori_mobili()
for operatore_mobile in tutti_operatori_mobili_dopo:
    print(f"ID: {operatore_mobile.id}, Nome: {operatore_mobile.nome}, Cognome: {operatore_mobile.cognome}")

# Elimina un operatore mobile(ad esempio, con ID 2)
operatore_mobile_da_eliminare_id = 21
operatore_mobile_dao.elimina_operatore_sala(operatore_mobile_da_eliminare_id)

# Ottieni tutti gli operatori mobili dopo l'eliminazione
print("\nTutti gli operatori mobili dopo l'eliminazione:")
tutti_operatori_mobili_dopo_elim = operatore_mobile_dao.ottieni_tutti_operatori_mobili()
for operatore_mobile in tutti_operatori_mobili_dopo_elim:
    print(f"ID: {operatore_mobile.id}, Nome: {operatore_mobile.nome}, Cognome: {operatore_mobile.cognome}")
