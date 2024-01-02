from datetime import date

from backend.src.models.QrCode import QrCode
from backend.src.models.QrCodeDAO import QrCodeDAO

# Creazione di un'istanza di QrCodeDAO
qrCode_dao = QrCodeDAO()

# Ottieni tutti i qrCode
print("Tutti i Qr Code:")
allQrCode = qrCode_dao.ottieni_tutti_qrCode()
for qrCode in allQrCode:
    print(f"ID: {qrCode.id}, isValido: {qrCode.isValido}, dataCreazione: {qrCode.dataCreazione}")

# Ottieni un QrCode con ID 3
print("\nQr Code con ID 3:")
qrCode_id = 3
qrCode = qrCode_dao.ottieni_qrCode_per_id(qrCode_id)
if qrCode:
    print(f"ID: {qrCode.id}, isValido: {qrCode.isValido}, dataCreazione: {qrCode.dataCreazione}")
else:
    print(f"Nessun Qr Code trovato con ID {qrCode_id}")

# Inserisci un nuovo Qr Code
nuovo_qrCode = QrCode(isValido=True, dataCreazione=date.today())
qrCode_dao.aggiungi_qrCode(nuovo_qrCode)

# Ottieni tutti i veicoli dopo l'inserimento
print("\nTutti i Qr Code dopo l'inserimento:")
tutti_qrCode_dopo = qrCode_dao.ottieni_tutti_qrCode()
for qrCode in tutti_qrCode_dopo:
    print(f"ID: {qrCode.id}, isValido: {qrCode.isValido}, dataCreazione: {qrCode.dataCreazione}")

# Elimina un Qr Code (ad esempio, con ID 2)
qrCode_da_eliminare_id = 22
qrCode_dao.elimina_qrCode(qrCode_da_eliminare_id)

# Ottieni tutti i Qr Code dopo l'eliminazione
print("\nTutti i Qr Code dopo l'eliminazione:")
tutti_QrCode_dopo_elim = qrCode_dao.ottieni_tutti_qrCode()
for qrCode in tutti_QrCode_dopo_elim:
    print(f"ID: {qrCode.id}, isValido: {qrCode.isValido}, dataCreazione: {qrCode.dataCreazione}")