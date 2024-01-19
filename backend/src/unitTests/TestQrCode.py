import unittest
from datetime import datetime
from unittest.mock import  MagicMock

from backend.src.dataManagement.services import QrCodeService


class TestQrCode(unittest.TestCase):
    def setUp(self):
        self.qrcode_dao_mock = MagicMock()
    def testOttieniQrCodePerId(self):

            self.qrcode_dao_mock.__json__ = MagicMock(return_value={"id": 1, "isValido":0,"dataCreazione":datetime(2023, 1, 1).date()})

            self.qrcode_dao_mock.ottieni_qrCode_per_id.return_value = self.qrcode_dao_mock

            risultato = QrCodeService.ottieniQRCodePerId(1)

            self.assertEqual(risultato, self.qrcode_dao_mock.__json__.return_value)
    def testOttieniQrCodeNonPresente(self):

            self.qrcode_dao_mock.ottieni_qrCode_per_id.return_value = None

            risultato = QrCodeService.ottieniQRCodePerId(59)

            self.assertEqual(risultato, {"message": "QRCode non trovato"})

if __name__ == '__main__':
    unittest.main()