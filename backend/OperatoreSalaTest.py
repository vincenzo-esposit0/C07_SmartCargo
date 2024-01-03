from src.models.UtenteRegistrato import OperatoreSala
from src.models.OperatoreSalaDAO import OperatoreSalaDAO

# Creazione di un'istanza di OperatoreSalaDAO
operatore_sala_dao = OperatoreSalaDAO()

# Ottieni tutti gli operatori di sala
print("Tutti gli operatori di sala:")
tutti_operatori_sala = operatore_sala_dao.ottieni_tutti_operatori_sala()
for operatore_sala in tutti_operatori_sala:
    print(f"ID: {operatore_sala.id}, Nome: {operatore_sala.nome}, Cognome: {operatore_sala.cognome}")

# Ottieni l'operatore di sala con ID 1
print("\nOperatore di sala con ID 1:")
operatore_sala_id = 1
operatore_sala_1 = operatore_sala_dao.ottieni_operatore_sala_per_id(operatore_sala_id)
if operatore_sala_1:
    print(f"ID: {operatore_sala_1.id}, Nome: {operatore_sala_1.nome}, Cognome: {operatore_sala_1.cognome}")
else:
    print(f"Nessun operatore di sala trovato con ID {operatore_sala_id}")

# Inserisci il nuovo operatore di sala
nuovo_operatore_sala = OperatoreSala(nome='Nuovo', cognome='Operatore', dataNascita='1990-01-01',
                                     codiceFiscale='ABC12345', email='nuovo@operatore.it',
                                     password='password', indirizzo='Indirizzo')
operatore_sala_dao.aggiungi_operatore_sala(nuovo_operatore_sala)

# Ottieni tutti gli operatori di sala dopo l'inserimento
print("\nTutti gli operatori di sala dopo l'inserimento:")
tutti_operatori_sala_dopo = operatore_sala_dao.ottieni_tutti_operatori_sala()
for operatore_sala in tutti_operatori_sala_dopo:
    print(f"ID: {operatore_sala.id}, Nome: {operatore_sala.nome}, Cognome: {operatore_sala.cognome}")

# Elimina un operatore di sala (ad esempio, con ID 2)
operatore_sala_da_eliminare_id = 21
operatore_sala_dao.elimina_operatore_sala(operatore_sala_da_eliminare_id)

# Ottieni tutti gli operatori di sala dopo l'eliminazione
print("\nTutti gli operatori di sala dopo l'eliminazione:")
tutti_operatori_sala_dopo_elim = operatore_sala_dao.ottieni_tutti_operatori_sala()
for operatore_sala in tutti_operatori_sala_dopo_elim:
    print(f"ID: {operatore_sala.id}, Nome: {operatore_sala.nome}, Cognome: {operatore_sala.cognome}")
