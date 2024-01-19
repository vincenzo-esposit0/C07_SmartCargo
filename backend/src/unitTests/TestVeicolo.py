import unittest
from unittest.mock import MagicMock
from backend.src.dataManagement.services import VeicoloService

class TestVeicoloService(unittest.TestCase):
    def setUp(self):
        # Creo un mock per il VeicoloDAO; questo mock verrà usato a posto dell'istanza reale di 'VeicoloDAO' per simularne il comportamento
        self.veicolo_dao_mock = MagicMock()

        # Inizializzo il VeicoloService con il mock
        #self.veicolo_service = VeicoloService(self.veicolo_dao_mock)

    # Verifico se la funzione restituisce correttamente i dettagli del veicolo rispetto al risultato atteso
    def testOttieniVeicoloPerId(self):
        # Configuro il mock per restituire un veicolo

        # Configuro il comportamento del mock dicendogli che quando il metodo __json__ viene chiamato, dovrebbe restituire un determinato valore
        #veicolo_mock.__json__.return_value = {"id": 1, "targa": "AB123CD", "descrizione": "Auto blu", "modello": "Modello X"}
        self.veicolo_dao_mock.__json__ = MagicMock(return_value={"id": 1, "targa": "AB123CD", "descrizione": "Auto blu", "modello": "Modello X"})

        # Configuro il mock del 'VeicoloDAO' in modo che quando viene chiamato il metodo, restituisca l'oggetto 'veicolo_mock', simulando il comportamento della classe 'VeicoloDAO' durante il test
        self.veicolo_dao_mock.ottieniVeicoloPerId.return_value = self.veicolo_dao_mock

        # Chiama il metodo da testare
        risultato = VeicoloService.ottieniVeicoloPerId(1)

        # Verifica che il risultato sia quello atteso
        self.assertEqual(risultato, self.veicolo_dao_mock.__json__.return_value)

    # Verifico se la funzione restituisce un messaggio corretto quando il veicolo non è presente nel DB
    def testOttieniVeicoloNonPresente(self):
        # Configuro il mock per restituire None, silando che il veicolo non è stato trovato
        self.veicolo_dao_mock.ottieniVeicoloPerId.return_value = {"message": "Veicolo non trovato"}

        risultato = VeicoloService.ottieniVeicoloPerId(23)

        self.assertEqual(risultato, self.veicolo_dao_mock.ottieniVeicoloPerId.return_value)

    # Verifico se la funzione gestisce correttamente le eccezioni e restituisce un risultato vuoto in caso di errore durante il recupero del veicolo

    # Caso id non valido: nullo
    def testOttieniOperazioneIdNullo(self):
        #Configuro il mock per restituire il messaggio di ID non valido
        self.veicolo_dao_mock.ottieniOperazionePerId.return_value = {"message": "Errore: ID Veicolo non valido"}

        risultato = VeicoloService.ottieniVeicoloPerId(None)

        self.assertEqual(risultato, self.veicolo_dao_mock.ottieniOperazionePerId.return_value)

    # Caso id non valido: id negativo
    def testOttieniOperazioneIdNegativo(self):
        #Configuro il mock per restituire il messaggio di ID non valido
        self.veicolo_dao_mock.ottieniOperazionePerId.return_value = {"message": "Errore: ID Veicolo non valido"}

        risultato = VeicoloService.ottieniVeicoloPerId(-1)

        self.assertEqual(risultato, self.veicolo_dao_mock.ottieniOperazionePerId.return_value)

    # Caso id non valido: Eccezione
    def testOttieniVeicoloCasoEccezione(self):
        # Configuro il mock per sollevare un'eccezione, simulando un errore durante il recupero dei dati del veicolo
        self.veicolo_dao_mock.ottieniVeicoloPerId.return_value = {"message": "Errore durante l'ottenimento del veicolo"}

        risultato = VeicoloService.ottieniVeicoloPerId({})

        self.assertEqual(risultato, self.veicolo_dao_mock.ottieniVeicoloPerId.return_value)


if __name__ == '__main__':
    unittest.main()