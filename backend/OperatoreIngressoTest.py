from src.models.UtenteRegistrato import OperatoreIngresso
from src.models.OperatoreIngressoDAO import OperatoreIngressoDAO

# Creazione di un'istanza di OperatoreIngressoDAO
operatore_ingresso_dao = OperatoreIngressoDAO()

# Ottieni tutti gli operatori di ingresso
print("Tutti gli operatori di ingresso:")
tutti_operatori_ingresso = operatore_ingresso_dao.ottieni_tutti_operatori_ingresso()
for operatore_ingresso in tutti_operatori_ingresso:
    print(f"ID: {operatore_ingresso.id}, Nome: {operatore_ingresso.nome}, Cognome: {operatore_ingresso.cognome}")

# Ottieni l'operatore di ingresso con ID 1
print("\nOperatore di ingresso con ID 1:")
operatore_ingresso_id = 1
operatore_ingresso_1 = operatore_ingresso_dao.ottieni_operatore_ingresso_per_id(operatore_ingresso_id)
if operatore_ingresso_1:
    print(f"ID: {operatore_ingresso_1.id}, Nome: {operatore_ingresso_1.nome}, Cognome: {operatore_ingresso_1.cognome}")
else:
    print(f"Nessun operatore di ingresso trovato con ID {operatore_ingresso_id}")

# Inserisci il nuovo operatore di ingresso
nuovo_operatore_ingresso = OperatoreIngresso(nome='Nuovo', cognome='Operatore', dataNascita='1990-01-01',
                                             codiceFiscale='ABC12345', email='nuovo@operatore.it',
                                             password='password', indirizzo='Indirizzo')
operatore_ingresso_dao.aggiungi_operatore_ingresso(nuovo_operatore_ingresso)

# Ottieni tutti gli operatori di ingresso dopo l'inserimento
print("\nTutti gli operatori di ingresso dopo l'inserimento:")
tutti_operatori_ingresso_dopo = operatore_ingresso_dao.ottieni_tutti_operatori_ingresso()
for operatore_ingresso in tutti_operatori_ingresso_dopo:
    print(f"ID: {operatore_ingresso.id}, Nome: {operatore_ingresso.nome}, Cognome: {operatore_ingresso.cognome}")

# Elimina un operatore di ingresso (ad esempio, con ID 2)
operatore_ingresso_da_eliminare_id = 21
operatore_ingresso_dao.elimina_operatore_ingresso(operatore_ingresso_da_eliminare_id)

# Ottieni tutti gli operatori di ingresso dopo l'eliminazione
print("\nTutti gli operatori di ingresso dopo l'eliminazione:")
tutti_operatori_ingresso_dopo_elim = operatore_ingresso_dao.ottieni_tutti_operatori_ingresso()
for operatore_ingresso in tutti_operatori_ingresso_dopo_elim:
    print(f"ID: {operatore_ingresso.id}, Nome: {operatore_ingresso.nome}, Cognome: {operatore_ingresso.cognome}")
