import unittest
from account.account_status import AccountStatus

class TestAccountStatus(unittest.TestCase):

    def test_account_status_values_initialized(self):
        expected = 1
        actual = AccountStatus.ACTIVE.value
        self.assertEqual(expected, actual)

        expected = 2
        actual = AccountStatus.INACTIVE.value
        self.assertEqual(expected, actual)

        expected = 3
        actual = AccountStatus.CLOSED.value
        self.assertEqual(expected, actual)

        expected = 4
        actual = AccountStatus.FROZEN.value
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()