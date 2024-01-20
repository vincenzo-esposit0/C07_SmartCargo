import unittest
from unittest.mock import MagicMock
from backend.src.dataManagement.services import OperatoreSalaService

class TestOperatoreSalaId(unittest.TestCase):
    def setUp(self):
        self.operatore_sala_dao_mock = MagicMock()

    # Caso id valido e presente nel DB
    def testOttieniOperatoreSalaPresente(self):
        operatore_sala_mock = MagicMock()

        operatore_sala_mock.__json__ = MagicMock(return_value={"codiceFiscale": "GHLALS93M15A001J",
                                                               "cognome": "Galli",
                                                               "dataNascita": "1993-06-15",
                                                               "email": "alessio@email.com",
                                                               "id": 1,
                                                               "indirizzo": "Via Roma, 123",
                                                               "nome": "Alessio",
                                                               "password": "password1"})

        # Chiama il metodo da testare
        risultato = OperatoreSalaService.ottieniOperatoreSalaPerId(1)

        # Verifica che il risultato sia quello atteso
        self.assertEqual(risultato, operatore_sala_mock.__json__.return_value)

    # Caso id valido ma non presente nel DB
    def testOttieniOperatoreSalaNonPresente(self):
        # Configuro il mock per restituire il messaggio di operazione non trovata nel DB
        self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value = {"message": "Operatore Sala non trovato"}

        risultato = OperatoreSalaService.ottieniOperatoreSalaPerId(40)

        self.assertEqual(risultato, self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value)

    # Caso id non valido: nullo
    def testOttieniOperatoreSalaIdNullo(self):
        # Configuro il mock per restituire il messaggio di ID non valido
        self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value = {"message": "Operatore Sala non trovato"}
        risultato = OperatoreSalaService.ottieniOperatoreSalaPerId(None)

        self.assertEqual(risultato, self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value)

    # Caso id non valido: id negativo
    def testOttieniOperatoreSalaIdNegativo(self):
        # Configuro il mock per restituire il messaggio di ID non valido
        self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value = {"message": "Operatore Sala non trovato"}

        risultato = OperatoreSalaService.ottieniOperatoreSalaPerId(-2)

        self.assertEqual(risultato, self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value)

    # Caso id non valido: eccezione
    def testOttieniOperazioneIdEccezione(self):
        # Configuro il mock per restituire il messaggio scaturito da un'eccezione
        self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value = {"Errore durante l'ottenimento dell'operatore Sala:"}

        risultato = OperatoreSalaService.ottieniOperatoreSalaPerId({})  # o qualsiasi altro valore valido per l'id

        self.assertEqual(risultato, {})

if __name__ == '__main__':
    unittest.main()
