import unittest
from datetime import datetime
from unittest.mock import MagicMock
from backend.src.dataManagement.services import OperazioneService

class TestOperazioneService(unittest.TestCase):
    def setUp(self):
        # Creo un mock per l'OperazioneDAO; questo mock verrà usato al posto dell'istanza reale di 'OperazioneDAO' per simularne il comportamento
        self.operazione_dao_mock = MagicMock()

    def testOttieniOperazionePerId(self):
        # Configuro il mock per restituire un'operazione

        # Configuro il comportamento del mock dicendogli che quando il metodo __json__ viene chiamato, dovrebbe restituire un determinato valore
        self.operazione_dao_mock.__json__ = MagicMock(return_value={
            "id": 1,
            "dataOperazione": datetime(2023, 1, 1).date(),
            "tipo": "Consegna",
            "descrizione": "Consegna merci elettroniche",
            "puntoDestinazione": "Magazzino Centrale",
            "stato": "In corso / Issue aperta",
            "autotrasportatore_id": 1,
            "operatoreIngresso_id": 11,
            "operatoreMagazzino_id": 7,
            "percorso_id": 1,
            "veicolo_id": 1
        })

        # Configuro il mock del 'OperazioneDAO' in modo che quando viene chiamato il metodo, restituisca l'oggetto 'operazione_mock', simulando il comportamento della classe 'OperazioneDAO' durante il test
        self.operazione_dao_mock.ottieniOperazionePerId.return_value = self.operazione_dao_mock

        # Chiama il metodo da testare
        risultato = OperazioneService.ottieniOperazionePerId(1)

        # Verifica che il risultato sia quello atteso
        self.assertEqual(risultato, self.operazione_dao_mock.__json__.return_value)

    def testOttieniOperazioneNonPresente(self):
        #Configuro il mock per restituire None, silando che l'operazione non è stato trovato
        self.operazione_dao_mock.ottieniVeicoloPerId.return_value = None

        risultato = OperazioneService.ottieniOperazionePerId(23)

        self.assertEqual(risultato, {"message": "Operazione non trovata"})

if __name__ == '__main__':
    unittest.main()
