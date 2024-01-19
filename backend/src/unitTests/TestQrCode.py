import unittest
from unittest.mock import  MagicMock
from src.dataManagement.services import VeicoloService

class TestQrCode(unittest.TestCase):
    def setUp(self):
        self.qrcode_dao_mock = MagicMock()
    def testOttieniQrCodePerId(self):
       # Configuro il mock per restituire un'operazione

            # Configuro il comportamento del mock dicendogli che quando il metodo __json__ viene chiamato, dovrebbe restituire un determinato valore
            self.qrcode_dao_mock.__json__ = MagicMock(return_value={{"id": 1, "isValido":1,"dataCreazione":"2023-01-01"}})

            # Configuro il mock del 'OperazioneDAO' in modo che quando viene chiamato il metodo, restituisca l'oggetto 'operazione_mock', simulando il comportamento della classe 'OperazioneDAO' durante il test
            self.qrcode_dao_mock.ottieni_qrCode_per_id.return_value = self.qrcode_dao_mock

            # Chiama il metodo da testare
            risultato = OperazioneService.QrCodeService.ottieniQRCodePerId(1)

            # Verifica che il risultato sia quello atteso
            self.assertEqual(risultato, self.qrcode_dao_mock.__json__.return_value)

if __name__ == '__main__':
    unittest.main()