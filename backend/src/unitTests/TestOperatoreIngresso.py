import unittest
from unittest.mock import MagicMock
from backend.src.dataManagement.services import OperatoreIngressoService

class TestOperatoreIngressoId(unittest.TestCase):
    def setUp(self):
        self.operatore_ingresso_dao_mock = MagicMock()

    #Caso id valido e presente nel DB
    def testOttieniOperatoreIngressoPresente(self):

        operatore_ingresso_mock = MagicMock()

        operatore_ingresso_mock.__json__ = MagicMock(return_value={"codiceFiscale": "ABC123XYZ4567890",
                                                                   "cognome": "Ricci",
                                                                   "dataNascita": "1990-02-18",
                                                                   "email": "marco@email.com",
                                                                   "id": 1,
                                                                   "indirizzo": "Via Roma, 123",
                                                                   "nome": "Marco",
                                                                   "password": "pass12345"})


        #Chiama il metodo da testare
        risultato = OperatoreIngressoService.ottieniOperatoreIngressoPerId(1)

        # Verifica che il risultato sia quello atteso
        self.assertEqual(risultato, operatore_ingresso_mock.__json__.return_value)


    #Caso id valido ma non presente nel DB
    def testOttieniOperatoreIngressoNonPresente(self):
        #Configuro il mock per restituire il messaggio di operazione non trovata nel DB
        self.operatore_ingresso_dao_mock.ottieniOperatoreIngressoPerId.return_value = {"message": "Operatore Ingresso non trovato"}

        risultato = OperatoreIngressoService.ottieniOperatoreIngressoPerId(30)

        self.assertEqual(risultato, self.operatore_ingresso_dao_mock.ottieniOperatoreIngressoPerId.return_value)


    #Caso id non valido: nullo
    def testOttieniOttieniOperatoreIngressoIdNullo(self):
        #Configuro il mock per restituire il messaggio di ID non valido
        self.operatore_ingresso_dao_mock.ottieniOperatoreIngressoPerId.return_value = {"message": "Operatore Ingresso non trovato"}
        risultato = OperatoreIngressoService.ottieniOperatoreIngressoPerId(None)

        self.assertEqual(risultato, self.operatore_ingresso_dao_mock.ottieniOperatoreIngressoPerId.return_value)


    #Caso id non valido: id negativo
    def testOttieniOperatoreIngressoIdNegativo(self):
        #Configuro il mock per restituire il messaggio di ID non valido
        self.operatore_ingresso_dao_mock.ottieniOperatoreIngressoPerId.return_value = {"message": "Operatore Ingresso non trovato"}

        risultato = OperatoreIngressoService.ottieniOperatoreIngressoPerId(-1)

        self.assertEqual(risultato, self.operatore_ingresso_dao_mock.ottieniOperatoreIngressoPerId.return_value)


    #Caso id non valido: eccezione
    def testOttieniOperazioneIdEccezione(self):
        #Configuro il mock per restituire il messaggio scaturito da un'eccezione
        self.operatore_ingresso_dao_mock.ottieniOperatoreIngressoPerId.return_value = {"Errore durante l'ottenimento dell'operatore Ingresso:"}

        risultato = OperatoreIngressoService.ottieniOperatoreIngressoPerId({})  # o qualsiasi altro valore valido per l'id

        self.assertEqual(risultato, {})

if __name__ == '__main__':
    unittest.main()

