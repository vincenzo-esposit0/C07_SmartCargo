from src.models.UtenteRegistrato import Autotrasportatore
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO

# Creazione di un'istanza di AutotrasportatoreDAO
autotrasportatore_dao = AutotrasportatoreDAO()

# Ottieni tutti gli autotrasportatori
print("Tutti gli autotrasportatori:")
tutti_autotrasportatori = autotrasportatore_dao.ottieni_tutti_autotrasportatori()
for autotrasportatore in tutti_autotrasportatori:
    print(f"ID: {autotrasportatore.id}, Nome: {autotrasportatore.nome}, Cognome: {autotrasportatore.cognome}")

# Ottieni l'autotrasportatore con ID 1
print("\nAutotrasportatore con ID 1:")
autotrasportatore_id = 1
autotrasportatore_1 = autotrasportatore_dao.ottieni_autotrasportatore_per_id(autotrasportatore_id)
if autotrasportatore_1:
    print(f"ID: {autotrasportatore_1.id}, Nome: {autotrasportatore_1.nome}, Cognome: {autotrasportatore_1.cognome}")
    print(f"Azienda: {autotrasportatore_1.azienda}")
else:
    print(f"Nessun autotrasportatore trovato con ID {autotrasportatore_id}")

# Inserisci un nuovo autotrasportatore
nuovo_autotrasportatore = Autotrasportatore(nome='Nuovo', cognome='Autotrasportatore', dataNascita='1990-01-01',
                                            codiceFiscale='DEF67890', email='nuovo@autotrasportatore.it',
                                            password='password', indirizzo='Indirizzo', azienda='AziendaX', qrCode_id=1)
autotrasportatore_dao.aggiungi_autotrasportatore(nuovo_autotrasportatore)

# Ottieni tutti gli autotrasportatori dopo l'inserimento
print("\nTutti gli autotrasportatori dopo l'inserimento:")
tutti_autotrasportatori_dopo = autotrasportatore_dao.ottieni_tutti_autotrasportatori()
for autotrasportatore in tutti_autotrasportatori_dopo:
    print(f"ID: {autotrasportatore.id}, Nome: {autotrasportatore.nome}, Cognome: {autotrasportatore.cognome}")
    print(f"Azienda: {autotrasportatore.azienda}")

# Elimina un autotrasportatore (ad esempio, con ID 2)
autotrasportatore_da_eliminare_id = 21
autotrasportatore_dao.elimina_autotrasportatore(autotrasportatore_da_eliminare_id)

# Ottieni tutti gli autotrasportatori dopo l'eliminazione
print("\nTutti gli autotrasportatori dopo l'eliminazione:")
tutti_autotrasportatori_dopo_elim = autotrasportatore_dao.ottieni_tutti_autotrasportatori()
for autotrasportatore in tutti_autotrasportatori_dopo_elim:
    print(f"ID: {autotrasportatore.id}, Nome: {autotrasportatore.nome}, Cognome: {autotrasportatore.cognome}")
    print(f"Azienda: {autotrasportatore.azienda}")
