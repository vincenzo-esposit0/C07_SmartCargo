from src.models.UtenteRegistrato import OperatoreMagazzino
from src.models.OperatoreMagazzinoDAO import OperatoreMagazzinoDAO

# Creazione di un'istanza di OperatoreMagazzinoDAO
operatore_magazzino_dao = OperatoreMagazzinoDAO()

# Ottieni tutti gli operatori di magazzino
print("Tutti gli operatori di magazzino:")
tutti_operatori_magazzino = operatore_magazzino_dao.ottieni_tutti_operatori_magazzino()
for operatore_magazzino in tutti_operatori_magazzino:
    print(f"ID: {operatore_magazzino.id}, Nome: {operatore_magazzino.nome}, Cognome: {operatore_magazzino.cognome}")

# Ottieni l'operatore di magazzino con ID 1
print("\nOperatore di magazzino con ID 1:")
operatore_magazzino_id = 1
operatore_magazzino_1 = operatore_magazzino_dao.ottieni_operatore_magazzino_per_id(operatore_magazzino_id)
if operatore_magazzino_1:
    print(f"ID: {operatore_magazzino_1.id}, Nome: {operatore_magazzino_1.nome}, Cognome: {operatore_magazzino_1.cognome}")
else:
    print(f"Nessun operatore di magazzino trovato con ID {operatore_magazzino_id}")

# Inserisci il nuovo operatore di magazzino
nuovo_operatore_magazzino = OperatoreMagazzino(nome='Nuovo', cognome='Operatore', dataNascita='1990-01-01',
                                               codiceFiscale='ABC12345', email='nuovo@operatore.it',
                                               password='password', indirizzo='Indirizzo')
operatore_magazzino_dao.aggiungi_operatore_magazzino(nuovo_operatore_magazzino)

# Ottieni tutti gli operatori di magazzino dopo l'inserimento
print("\nTutti gli operatori di magazzino dopo l'inserimento:")
tutti_operatori_magazzino_dopo = operatore_magazzino_dao.ottieni_tutti_operatori_magazzino()
for operatore_magazzino in tutti_operatori_magazzino_dopo:
    print(f"ID: {operatore_magazzino.id}, Nome: {operatore_magazzino.nome}, Cognome: {operatore_magazzino.cognome}")

# Elimina un operatore di magazzino (ad esempio, con ID 2)
operatore_magazzino_da_eliminare_id = 21
operatore_magazzino_dao.elimina_operatore_magazzino(operatore_magazzino_da_eliminare_id)

# Ottieni tutti gli operatori di magazzino dopo l'eliminazione
print("\nTutti gli operatori di magazzino dopo l'eliminazione:")
tutti_operatori_magazzino_dopo_elim = operatore_magazzino_dao.ottieni_tutti_operatori_magazzino()
for operatore_magazzino in tutti_operatori_magazzino_dopo_elim:
    print(f"ID: {operatore_magazzino.id}, Nome: {operatore_magazzino.nome}, Cognome: {operatore_magazzino.cognome}")
