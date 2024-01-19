import unittest
from unittest.mock import MagicMock

import sys
import os

# Aggiungi il percorso del progetto al percorso di Python
current_script_path = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_script_path, ".."))
sys.path.append(project_root)

try:
    # Prova ad importare con 'src.'
    from src.dataManagement.services import OperatoreSalaService
except ImportError:
    # Se fallisce, prova senza 'src.'
    from dataManagement.services import OperatoreSalaService


class TestOperatoreSala(unittest.TestCase):
    def setUp(self):
        self.operatore_sala_dao_mock = MagicMock()

    def testOttieniOperatoreSalaPerId(self):

        operatore_sala_mock = MagicMock()

        operatore_sala_mock.__json__ = MagicMock(return_value={"codiceFiscale": "RSSLCU90T10L345K", "cognome": "Rossini", "dataNascita": "1990-12-10", "email": "luca@email.com", "id": 3, "indirizzo": "Via Firenze, 789", "nome": "Luca", "password": "pass123abc"})

        # Configuro il mock del 'VeicoloDAO' in modo che quando viene chiamato il metodo, restituisca l'oggetto 'veicolo_mock', simulando il comportamento della classe 'VeicoloDAO' durante il test
        self.operatore_sala_dao_mock.ottieniOperatoreSalaPerId.return_value = operatore_sala_mock

        # Chiama il metodo da testare
        risultato = OperatoreSalaService.ottieniOperatoreSalaPerId(3)

        # Verifica che il risultato sia quello atteso
        self.assertEqual(risultato, operatore_sala_mock.__json__.return_value)

if __name__ == '__main__':
    unittest.main()