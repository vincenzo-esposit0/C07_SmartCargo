import unittest
from unittest.mock import MagicMock

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")))

try:
    # Prova ad importare con 'src.'
    from src.dataManagement.services import OperatoreSalaService
except ImportError:
    # Se fallisce, prova senza 'src.'
    from dataManagement.services import OperatoreSalaService


#from backend.src.dataManagement.services import OperatoreSalaService

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
        self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value = {"message": "Operatore di Sala non trovato"}

        risultato = OperatoreSalaService.ottieniOperatoreSalaPerId(40)

        self.assertEqual(risultato, self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value)

    # Caso id non valido: nullo
    def testOttieniOperatoreSalaIdNullo(self):
        # Configuro il mock per restituire il messaggio di ID non valido
        self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value = {"message": "Errore: ID Operatore di Sala non valido"}
        risultato = OperatoreSalaService.ottieniOperatoreSalaPerId(None)

        self.assertEqual(risultato, self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value)

    # Caso id non valido: id negativo
    def testOttieniOperatoreSalaIdNegativo(self):
        # Configuro il mock per restituire il messaggio di ID non valido
        self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value = {"message": "Errore: ID Operatore di Sala non valido"}

        risultato = OperatoreSalaService.ottieniOperatoreSalaPerId(-2)

        self.assertEqual(risultato, self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value)

    # Caso id non valido: eccezione
    def testOttieniOperazioneIdEccezione(self):
        # Configuro il mock per restituire il messaggio scaturito da un'eccezione
        self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value = {"message": "Errore durante l'ottenimento dell'operatore di Sala"}

        risultato = OperatoreSalaService.ottieniOperatoreSalaPerId({})

        self.assertEqual(risultato, self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value)

if __name__ == '__main__':
    unittest.main()
