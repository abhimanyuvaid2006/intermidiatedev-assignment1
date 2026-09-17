import unittest
from account.bank_account import BankAccount
from account.account_status import AccountStatus

class TestBankAccount(unittest.TestCase):

    def test_init_account_id_less_than_zero_exception(self):
        with self.assertRaises(ValueError) as context:
            BankAccount(-1, 1000.00, "Pete Zahut", AccountStatus.ACTIVE)

        expected = "account_id must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_account_id_zero_exception(self):
        with self.assertRaises(ValueError) as context:
            BankAccount(0, 1000.00, "Pete Zahut", AccountStatus.ACTIVE)

        expected = "account_id must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_bank_account_initialized(self):
        account = BankAccount(20019, 6764.67, "Pete Zahut", AccountStatus.ACTIVE)

        expected = 20019
        actual = account._BankAccount__account_id
        self.assertEqual(expected, actual)

        expected = 6764.67
        actual = account._BankAccount__balance
        self.assertEqual(expected, actual)

        expected = "Pete Zahut"
        actual = account._BankAccount__owner
        self.assertEqual(expected, actual)

        expected = AccountStatus.ACTIVE
        actual = account._BankAccount__status
        self.assertEqual(expected, actual)

    def test_account_id_returns_current_state(self):
        account = BankAccount(20019, 6764.67, "Pete Zahut", AccountStatus.ACTIVE)

        actual = account.account_id

        expected = 20019
        self.assertEqual(expected, actual)

    def test_balance_returns_current_state(self):
        account = BankAccount(20019, 6764.67, "Pete Zahut", AccountStatus.ACTIVE)

        actual = account.balance

        expected = 6764.67
        self.assertEqual(expected, actual)

    def test_owner_returns_current_state(self):
        account = BankAccount(20019, 6764.67, "Pete Zahut", AccountStatus.ACTIVE)

        actual = account.owner

        expected = "Pete Zahut"
        self.assertEqual(expected, actual)

    def test_status_returns_current_state(self):
        account = BankAccount(20019, 6764.67, "Pete Zahut", AccountStatus.ACTIVE)

        actual = account.status

        expected = AccountStatus.ACTIVE
        self.assertEqual(expected, actual)

    def test_update_balance_positive_amount_increases_balance(self):
        account = BankAccount(20019, 1000.00, "Pete Zahut", AccountStatus.ACTIVE)

        account.update_balance(500.00)

        expected = 1500.00
        actual = account._BankAccount__balance
        self.assertEqual(expected, actual)

    def test_update_balance_negative_amount_decreases_balance(self):
        account = BankAccount(20019, 1000.00, "Pete Zahut", AccountStatus.ACTIVE)

        account.update_balance(-500.00)

        expected = 500.00
        actual = account._BankAccount__balance
        self.assertEqual(expected, actual)

    def test_deposit_amount_less_than_zero_exception(self):
        account = BankAccount(20019, 1000.00, "Pete Zahut", AccountStatus.ACTIVE)

        with self.assertRaises(ValueError) as context:
            account.deposit(-1.00)

        expected = "amount must be a value greater than or equal to zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_deposit_amount_increases_balance(self):
        account = BankAccount(20019, 1000.00, "Pete Zahut", AccountStatus.ACTIVE)

        account.deposit(250.00)

        expected = 1250.00
        actual = account._BankAccount__balance
        self.assertEqual(expected, actual)

    def test_withdraw_amount_less_than_zero_exception(self):
        account = BankAccount(20019, 1000.00, "Pete Zahut", AccountStatus.ACTIVE)

        with self.assertRaises(ValueError) as context:
            account.withdraw(-1.00)

        expected = "amount must be a value greater than or equal to zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_withdraw_amount_zero_balance_unchanged(self):
        account = BankAccount(20019, 1000.00, "Pete Zahut", AccountStatus.ACTIVE)

        account.withdraw(0.00)

        expected = 1000.00
        actual = account._BankAccount__balance
        self.assertEqual(expected, actual)

    def test_withdraw_amount_greater_than_balance_exception(self):
        account = BankAccount(20019, 1000.00, "Pete Zahut", AccountStatus.ACTIVE)

        with self.assertRaises(ValueError) as context:
            account.withdraw(1500.00)

        expected = "amount cannot exceed the account balance"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_withdraw_amount_decreases_balance(self):
        account = BankAccount(20019, 1000.00, "Pete Zahut", AccountStatus.ACTIVE)

        account.withdraw(250.00)

        expected = 750.00
        actual = account._BankAccount__balance
        self.assertEqual(expected, actual)

    def test_str_returns_string_representation(self):
        account = BankAccount(20019, 6764.67, "Pete Zahut", AccountStatus.ACTIVE)

        actual = str(account)

        expected = "Account Number: 20019 Balance: $6,764.67"
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main() 