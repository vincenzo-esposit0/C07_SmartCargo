import unittest
from unittest.mock import MagicMock
from backend.src.dataManagement.services import OperatoreIngressoService

class TestOperatoreIngresso(unittest.TestCase):
    def setUp(self):
        self.operatore_ingresso_dao_mock = MagicMock()

    def testOttieniOperatoreIngressoPerId(self):

        operatore_ingresso_mock = MagicMock()

        operatore_ingresso_mock.__json__ = MagicMock(return_value={"codiceFiscale": "ABC123XYZ4567890",
                                                                   "cognome": "Ricci",
                                                                   "dataNascita": "1990-02-18",
                                                                   "email": "marco@email.com",
                                                                   "id": 1,
                                                                   "indirizzo": "Via Roma, 123",
                                                                   "nome": "Marco",
                                                                   "password": "pass12345"})


        self.operatore_ingresso_dao_mock.ottieniOperatoreingressoPerId.return_value = operatore_ingresso_mock


        risultato = OperatoreIngressoService.ottieniOperatoreIngressoPerId(3)

        # Verifica che il risultato sia quello atteso
        self.assertEqual(risultato, operatore_ingresso_mock.__json__.return_value)

if __name__ == '__main__':
    unittest.main()