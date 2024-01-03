from datetime import date

from src.models.QrCode import QrCode
from src.models.QrCodeDAO import QrCodeDAO
from src.models.UtenteRegistrato import Autotrasportatore
from src.models.AutotrasportatoreDAO import AutotrasportatoreDAO

# Creazione di un'istanza di AutotrasportatoreDAO
autotrasportatore_dao = AutotrasportatoreDAO()
qrCode_dao = QrCodeDAO()

# Ottieni tutti gli autotrasportatori
print("Tutti gli autotrasportatori:")
tutti_autotrasportatori = autotrasportatore_dao.ottieni_tutti_autotrasportatori()
for autotrasportatore in tutti_autotrasportatori:
    print(f"ID: {autotrasportatore.id}, Nome: {autotrasportatore.nome}, Cognome: {autotrasportatore.cognome}, QrCode: {autotrasportatore.qrCode_id}")

# Ottieni l'autotrasportatore con ID 1
print("\nAutotrasportatore con ID 1:")
autotrasportatore_id = 1
autotrasportatore_1 = autotrasportatore_dao.ottieni_autotrasportatore_per_id(autotrasportatore_id)
if autotrasportatore_1:
    print(f"ID: {autotrasportatore_1.id}, Nome: {autotrasportatore_1.nome}, Cognome: {autotrasportatore_1.cognome}, Azienda: {autotrasportatore_1.azienda}, QrCode: {autotrasportatore_1.qrCode_id}")
else:
    print(f"Nessun autotrasportatore trovato con ID {autotrasportatore_id}")

# Inserisci un nuovo autotrasportatore
# Prima creo un nuovo qrCode
nuovo_qrCode = QrCode(True, date.today())
nuovo_qrCode = qrCode_dao.aggiungi_qrCode(nuovo_qrCode)

# Crea un nuovo Autotrasportatore utilizzando l'ID del QrCode
nuovo_autotrasportatore = Autotrasportatore(
    nome='Nuovo', cognome='Autotrasportatore', dataNascita='1990-01-01',
    codiceFiscale='DEF67890', email='nuovo@autotrasportatore.it',
    password='password', indirizzo='Indirizzo', azienda='AziendaX', qrCode_id=nuovo_qrCode.id
)

# Aggiungi l'Autotrasportatore al database
autotrasportatore_dao.aggiungi_autotrasportatore(nuovo_autotrasportatore)

# Ottieni tutti gli autotrasportatori dopo l'inserimento
print("\nTutti gli autotrasportatori dopo l'inserimento:")
tutti_autotrasportatori_dopo = autotrasportatore_dao.ottieni_tutti_autotrasportatori()
for autotrasportatore in tutti_autotrasportatori_dopo:
    print(f"ID: {autotrasportatore.id}, Nome: {autotrasportatore.nome}, Cognome: {autotrasportatore.cognome}")
    print(f"Azienda: {autotrasportatore.azienda}, QrCode: {autotrasportatore.qrCode_id}")

# Elimina un autotrasportatore (ad esempio, con ID 2)
autotrasportatore_da_eliminare_id = 21
autotrasportatore_dao.elimina_autotrasportatore(autotrasportatore_da_eliminare_id)

# Ottieni tutti gli autotrasportatori dopo l'eliminazione
print("\nTutti gli autotrasportatori dopo l'eliminazione:")
tutti_autotrasportatori_dopo_elim = autotrasportatore_dao.ottieni_tutti_autotrasportatori()
for autotrasportatore in tutti_autotrasportatori_dopo_elim:
    print(f"ID: {autotrasportatore.id}, Nome: {autotrasportatore.nome}, Cognome: {autotrasportatore.cognome}")
    print(f"Azienda: {autotrasportatore.azienda}, QrCode: {autotrasportatore.qrCode_id}")
