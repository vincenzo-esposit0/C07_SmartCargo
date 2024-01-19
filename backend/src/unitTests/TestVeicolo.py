import unittest
from unittest.mock import  MagicMock
from backend.src.dataManagement.services import VeicoloService

class TestVeicoloService(unittest.TestCase):
    def setUp(self):
        # Creo un mock per il VeicoloDAO; questo mock verrà usato a posto dell'istanza reale di 'VeicoloDAO' per simularne il comportamento
        self.veicolo_dao_mock = MagicMock()

        # Inizializzo il VeicoloService con il mock
        #self.veicolo_service = VeicoloService(self.veicolo_dao_mock)

    def testOttieniVeicoloPerId(self):
        # Configuro il mock per restituire un veicolo

        #Creo l'oggetto mock che siuli il comportamento
        veicolo_mock = MagicMock()
        # Configuro il comportamento del mock dicendogli che quando il metodo __json__ viene chiamato, dovrebbe restituire un determinato valore
        #veicolo_mock.__json__.return_value = {"id": 1, "targa": "AB123CD", "descrizione": "Auto blu", "modello": "Modello X"}
        veicolo_mock.__json__ = MagicMock(return_value={"id": 1, "targa": "AB123CD", "descrizione": "Auto blu", "modello": "Modello X"})

        # Configuro il mock del 'VeicoloDAO' in modo che quando viene chiamato il metodo, restituisca l'oggetto 'veicolo_mock', simulando il comportamento della classe 'VeicoloDAO' durante il test
        self.veicolo_dao_mock.ottieniVeicoloPerId.return_value = veicolo_mock

        # Chiama il metodo da testare
        risultato = VeicoloService.ottieniVeicoloPerId(1)

        # Verifica che il risultato sia quello atteso
        self.assertEqual(risultato, veicolo_mock.__json__.return_value)

if __name__ == '__main__':
    unittest.main()