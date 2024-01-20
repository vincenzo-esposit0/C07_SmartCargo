import unittest
from datetime import datetime
from unittest.mock import  MagicMock
import sys
import os

# Aggiungi il percorso del progetto al percorso di Python
current_script_path = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_script_path, ".."))
sys.path.append(project_root)

try:
    # Prova ad importare con 'src.'
    from src.dataManagement.services import QrCodeService
except ImportError:
    # Se fallisce, prova senza 'src.'
    from dataManagement.services import QrCodeService


class TestQrCode(unittest.TestCase):
    def setUp(self):
        self.qrcode_dao_mock = MagicMock()

    def testOttieniQrCodePerId(self):
        self.qrcode_dao_mock.__json__ = MagicMock(return_value={"id": 1, "isValido": True, "dataCreazione": datetime(2023, 1, 1).date()})
        self.qrcode_dao_mock.ottieniQRCodePerId.return_value = self.qrcode_dao_mock
        risultato = QrCodeService.ottieniQRCodePerId(1)
        self.assertEqual(risultato, self.qrcode_dao_mock.__json__.return_value)


    def testOttieniQrCodeNonPresente(self):
        self.qrcode_dao_mock.ottieniQRCodePerId.return_value = {"message": "QrCode non trovato"}
        risultato = QrCodeService.ottieniQRCodePerId(59)
        self.assertEqual(risultato, self.qrcode_dao_mock.ottieniQRCodePerId.return_value)

    # Caso id non valido: nullo
    def testOttieniQrCodePerIdNullo(self):
        # Configuro il mock per restituire il messaggio di ID non valido
        self.qrcode_dao_mock.ottieniQRCodePerId.return_value = {"message": "Errore: ID QrCode non valido"}
        risultato = QrCodeService.ottieniQRCodePerId(None)
        self.assertEqual(risultato, self.qrcode_dao_mock.ottieniQRCodePerId.return_value)

    # Caso id non valido: id negativo
    def testOttieniQrCodePerIdNegativo(self):
        # Configuro il mock per restituire il messaggio di ID non valido
        self.qrcode_dao_mock.ottieniQRCodePerId.return_value = {"message": "Errore: ID QrCode non valido"}
        risultato = QrCodeService.ottieniQRCodePerId(-1)
        self.assertEqual(risultato, self.qrcode_dao_mock.ottieniQRCodePerId.return_value)

    # Caso id non valido: Eccezione
    def testOttieniQrCodeCasoEccezione(self):
        # Configuro il mock per sollevare un'eccezione, simulando un errore durante il recupero dei dati del veicolo
        self.qrcode_dao_mock.ottieniQRCodePerId.return_value = {"message": "Errore durante l'ottenimento del QrCode"}
        risultato = QrCodeService.ottieniQRCodePerId({})
        self.assertEqual(risultato, self.qrcode_dao_mock.ottieniQRCodePerId.return_value)


if __name__ == '__main__':
    unittest.main()