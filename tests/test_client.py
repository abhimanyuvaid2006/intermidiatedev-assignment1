import unittest
from email_validator import EmailNotValidError
from account.client import Client

class TestClient(unittest.TestCase):

    def test_init_client_id_less_than_zero_exception(self):
        with self.assertRaises(ValueError) as context:
            Client(-1, "Pete Zahut", "pzahut@yarrow-mullein.ca")

        expected = "client_id must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_client_id_zero_exception(self):
        with self.assertRaises(ValueError) as context:
            Client(0, "Pete Zahut", "pzahut@yarrow-mullein.ca")

        expected = "client_id must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_name_empty_string_exception(self):
        with self.assertRaises(ValueError) as context:
            Client(1010, "   ", "pzahut@yarrow-mullein.ca")

        expected = "name cannot be an empty string"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_email_invalid_exception(self):
        with self.assertRaises(EmailNotValidError):
            Client(1010, "Pete Zahut", "not-an-email")

    def test_init_client_initialized(self):
        client = Client(1010, "Pete Zahut", "pzahut@yarrow-mullein.ca")

        expected = 1010
        actual = client._Client__client_id
        self.assertEqual(expected, actual)

        expected = "Pete Zahut"
        actual = client._Client__name
        self.assertEqual(expected, actual)

        expected = "pzahut@yarrow-mullein.ca"
        actual = client._Client__email_address
        self.assertEqual(expected, actual)

    def test_client_id_returns_current_state(self):
        client = Client(1010, "Pete Zahut", "pzahut@yarrow-mullein.ca")

        actual = client.client_id

        expected = 1010
        self.assertEqual(expected, actual)

    def test_name_returns_current_state(self):
        client = Client(1010, "Pete Zahut", "pzahut@yarrow-mullein.ca")

        actual = client.name

        expected = "Pete Zahut"
        self.assertEqual(expected, actual)

    def test_email_address_returns_current_state(self):
        client = Client(1010, "Pete Zahut", "pzahut@yarrow-mullein.ca")

        actual = client.email_address

        expected = "pzahut@yarrow-mullein.ca"
        self.assertEqual(expected, actual)

    def test_email_address_set_invalid_exception(self):
        client = Client(1010, "Pete Zahut", "pzahut@yarrow-mullein.ca")

        with self.assertRaises(EmailNotValidError):
            client.email_address = "not-an-email"

    def test_email_address_set_valid_updates_state(self):
        client = Client(1010, "Pete Zahut", "pzahut@yarrow-mullein.ca")

        client.email_address = "new.address@yarrow-mullein.ca"

        expected = "new.address@yarrow-mullein.ca"
        actual = client._Client__email_address
        self.assertEqual(expected, actual)

    def test_str_returns_string_representation(self):
        client = Client(1010, "Pete Zahut", "pzahut@yarrow-mullein.ca")

        actual = str(client)

        expected = "Pete Zahut [1010] - pzahut@yarrow-mullein.ca"
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()