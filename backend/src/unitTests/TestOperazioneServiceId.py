import unittest
from datetime import datetime
from unittest.mock import MagicMock
from backend.src.dataManagement.services import OperazioneService

class TestOttieniOperazionePerId(unittest.TestCase):
    def setUp(self):
        # Creo un mock per l'OperazioneDAO; questo mock verrà usato al posto dell'istanza reale di 'OperazioneDAO' per simularne il comportamento
        self.operazione_dao_mock = MagicMock()

    #Caso id valido e presente nel DB
    def testOttieniOperazionePresente(self):
        # Configuro il mock per restituire un'operazione valida nel DB

        # Configuro il comportamento del mock dicendogli che quando il metodo __json__ viene chiamato, dovrebbe restituire un determinato valore
        self.operazione_dao_mock.__json__ = MagicMock(return_value={
            "id": 1,
            "dataOperazione": datetime(2023, 1, 1).date(),
            "tipo": "Consegna",
            "descrizione": "Consegna merci elettroniche",
            "puntoDestinazione": "Magazzino Centrale",
            "stato": "In corso",
            "autotrasportatore_id": 1,
            "operatoreIngresso_id": 11,
            "operatoreMagazzino_id": 7,
            "percorso_id": 1,
            "veicolo_id": 1
        })

        #Chiama il metodo da testare
        risultato = OperazioneService.ottieniOperazionePerId(1)

        # Verifica che il risultato sia quello atteso
        self.assertEqual(risultato, self.operazione_dao_mock.__json__.return_value)


    #Caso id valido ma non presente nel DB
    def testOttieniOperazioneNonPresente(self):
        #Configuro il mock per restituire il messaggio di operazione non trovata nel DB
        self.operazione_dao_mock.ottieniOperazionePerId.return_value = {"message": "Operazione non trovata"}

        risultato = OperazioneService.ottieniOperazionePerId(30)

        self.assertEqual(risultato, self.operazione_dao_mock.ottieniOperazionePerId.return_value)


    #Caso id non valido: nullo
    def testOttieniOperazioneIdNullo(self):
        #Configuro il mock per restituire il messaggio di ID non valido
        self.operazione_dao_mock.ottieniOperazionePerId.return_value = {"message": "Errore: ID Operazione non valido"}

        risultato = OperazioneService.ottieniOperazionePerId(None)

        self.assertEqual(risultato, self.operazione_dao_mock.ottieniOperazionePerId.return_value)


    #Caso id non valido: id negativo
    def testOttieniOperazioneIdNegativo(self):
        #Configuro il mock per restituire il messaggio di ID non valido
        self.operazione_dao_mock.ottieniOperazionePerId.return_value = {"message": "Errore: ID Operazione non valido"}

        risultato = OperazioneService.ottieniOperazionePerId(-1)

        self.assertEqual(risultato, self.operazione_dao_mock.ottieniOperazionePerId.return_value)


    #Caso id non valido: eccezione
    def testOttieniOperazioneIdEccezione(self):
        #Configuro il mock per restituire il messaggio scaturito da un'eccezione
        self.operazione_dao_mock.ottieniOperazionePerId.return_value = {"message": "Errore durante l'ottenimento delle operazione"}

        risultato = OperazioneService.ottieniOperazionePerId({})

        self.assertEqual(risultato, self.operazione_dao_mock.ottieniOperazionePerId.return_value)


if __name__ == '__main__':
    unittest.main()
