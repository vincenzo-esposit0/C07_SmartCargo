import unittest
from datetime import datetime, date
from unittest.mock import patch, MagicMock
from backend.src.dataManagement.account import AccountAutotrasportatoreController
from backend.src.dataManagement.account.AccountAutotrasportatoreController import modificaAutotrasportatore
from backend.src.dataManagement.issue import IssueController
from backend.src.models.UtenteRegistrato import Autotrasportatore


class TestAccountAutotrasportatoreController(unittest.TestCase):

    def setUp(self):
            # Configurare oggetti o variabili comuni per tutti i test
            self.mock_autotrasportatore_dao = MagicMock()


    def test_modificaAutotrasportatore(self):
            # Creare un oggetto JSON di esempio per il test
            self.mock_autotrasportatore_dao.__json__ = MagicMock(return_value = {
                "id": 1,
                "nome": "NomeTest",
                "cognome": "CognomeTest",
                "dataNascita": "1990-01-01",
                "codiceFiscale": "RSSMRA85M01H501Z",
                "email": "test@example.com",
                "password": "testpassword",
                "indirizzo": "Via Test, 123",
                "azienda": "AziendaTest",
                "qrCode_id": 1
            })


            autotrasportatoremod = {
                    "id": 1,
                    "nome": "NomeTest",
                    "cognome": "CognomeTest",
                    "dataNascita": "1990-01-01",
                    "codiceFiscale": "RSSMRA85M01H501Z",
                    "email": "test@example.com",
                    "password": "testpassword",
                    "indirizzo": "Via Test, 123",
                    "azienda": "AziendaTest"
            }

            self.mock_autotrasportatore_dao.ottieni_autotrasportatore_per_id.return_value = self.mock_autotrasportatore_dao
            self.mock_autotrasportatore_dao.aggiorna_autotrasportatore.return_value = self.mock_autotrasportatore_dao


            # Chiamare la funzione da testare
            response = AccountAutotrasportatoreController.modificaAutotrasportatore(autotrasportatoremod)



            print("Risposta effettiva:", response)
            print("Oracolo:", self.mock_autotrasportatore_dao.__json__.return_value)
            # Verificare che la funzione restituisca il risultato atteso
            self.assertEqual(response, self.mock_autotrasportatore_dao.__json__.return_value)

        #@patch('backend.src.models.AutotrasportatoreDAO')
    """def test_modificaAutotrasportatore_exception(self):

            # Simula un'eccezione nel dao
            self.mock_autotrasportatore_dao.ottieni_autotrasportatore_per_id.side_effect = Exception("Errore simulato")

            # Chiamata al metodo di modifica con eccezione attesa
            result = AccountAutotrasportatoreController.modificaAutotrasportatore({})

            # Verifica che il risultato contenga il messaggio di errore
            expected_result = {"message": "Errore durante la modifica dell'account di un autotrasportatore"}
            self.assertEqual(result, expected_result)"""

    def test_modificaAutotrasportatore_not_found(self):

                # Simula un'eccezione nel dao
                self.mock_autotrasportatore_dao.ottieniAutotrasportatorePerId.return_value = None

                # Chiamata al metodo di modifica con eccezione attesa
                result = AccountAutotrasportatoreController.modificaAutotrasportatore({})

                # Verifica che il risultato contenga il messaggio di errore
                expected_result = {"message": "Errore durante la modifica dell'account di un autotrasportatore"}
                self.assertEqual(result, expected_result)

    def test_modificaAutotrasportatore_exception(self):

                # Simula un'eccezione nel dao
                self.mock_autotrasportatore_dao.ottieniAutotrasportatorePerId.side_effect = Exception("Errore simulato")

                # Chiamata al metodo di modifica con eccezione attesa
                result = AccountAutotrasportatoreController.modificaAutotrasportatore({})

                # Verifica che il risultato contenga il messaggio di errore
                expected_result = {"message": "Errore durante la modifica dell'account di un autotrasportatore"}
                self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main()


