import unittest

from unittest.mock import MagicMock
from backend.src.dataManagement.account import AccountAutotrasportatoreController


class TestAccountAutotrasportatoreController(unittest.TestCase):

    def setUp(self):
             self.mock_autotrasportatore_dao = MagicMock()

    #Caso input corretto
    def test_modificaAutotrasportatore(self):

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


            # Chiamare la funzione da testare
            response = AccountAutotrasportatoreController.modificaAutotrasportatore(autotrasportatoremod)



            print("Risposta effettiva:", response)
            print("Oracolo:", self.mock_autotrasportatore_dao.__json__.return_value)
            # Verificare che la funzione restituisca il risultato atteso
            self.assertEqual(response, self.mock_autotrasportatore_dao.__json__.return_value)


    #Caso input vuoto
    def test_modificaAutotrasportatore_not_found(self):

                # Simula un'eccezione nel dao
                self.mock_autotrasportatore_dao.ottieniAutotrasportatorePerId.return_value = None

                # Chiamata al metodo di modifica con eccezione attesa
                result = AccountAutotrasportatoreController.modificaAutotrasportatore({})

                # Verifica che il risultato contenga il messaggio di errore
                expected_result = {"message": "Errore durante la modifica dell'account di un autotrasportatore"}
                self.assertEqual(result, expected_result)

    #campo input chiave vuota
    def test_modificaAutotrasportatore_valoreChiaveVuoto(self):
        self.mock_autotrasportatore_dao.__json__ = MagicMock(return_value = {
            "id": 1,
            "nome": "NomeTest",
            "cognome": "",
            "dataNascita": "1990-01-01",
            "codiceFiscale": "RSSMRA85M01H501Z",
            "email": "test@example.com",
            "password": "testpassword",
            "indirizzo": "Via Test, 123",
            "azienda": "AziendaTest",
            "qrCode_id": 1
        })

        result = AccountAutotrasportatoreController.modificaAutotrasportatore(self.mock_autotrasportatore_dao.__json__.return_value)

        # Verificare che la funzione restituisca il risultato atteso
        self.assertEqual(result, {"message": "Campo obbligatorio mancante o vuoto: cognome"})

    #Caso input chiave mancante
    def test_modificaAutotrasportatore_chiaveMancante(self):
        self.mock_autotrasportatore_dao.__json__ = MagicMock(return_value = {
            "id": 1,
            "nome": "NomeTest",
            "cognome": "CognomeTest",
            "dataNascita": "1990-01-01",
            "codiceFiscale": "RSSMRA85M01H501Z",
            "email": "test@example.com",
            "password": "testpassword",
            "indirizzo": "Via Test, 123",
            "qrCode_id": 1
        })

        result = AccountAutotrasportatoreController.modificaAutotrasportatore(self.mock_autotrasportatore_dao.__json__.return_value)

        # Verificare che la funzione restituisca il risultato atteso
        self.assertEqual(result, {"message": "Campo obbligatorio mancante o vuoto: azienda"})


    #Caso input non valido:eccezione
    def test_modificaAutotrasportatore_exception(self):

                # Chiamata al metodo di modifica con eccezione attesa
                result = AccountAutotrasportatoreController.modificaAutotrasportatore(1)

                expected_result = {"message": "Errore durante la modifica dell'account di un autotrasportatore"}
                self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()


