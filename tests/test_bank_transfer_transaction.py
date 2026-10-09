"""This module defines tests for the BankTransferTransaction class."""



import unittest
from account.account_status import AccountStatus
from account.bank_account import BankAccount
from transaction.bank_transfer_transaction import BankTransferTransaction
from transaction.transaction_status import TransactionStatus

__author__ = "abhimanyu"
__version__ = "1.0.0"


class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""

    def setUp(self) -> None:
        # Arrange
        self.account = BankAccount(123456, 500, "Sam", AccountStatus.ACTIVE)
        self.target_account = BankAccount(676767, 200, "Alex", AccountStatus.ACTIVE)

    def test_transaction_id_is_blank_string(self) -> None:
        # Arrange/Act
        with self.assertRaises(ValueError) as context:
            transaction = BankTransferTransaction("",
                                                  100,
                                                  self.account,
                                                  self.target_account)

        # Assert
        self.assertEqual("transaction_id cannot be blank",
                         str(context.exception))

    def test_amount_is_less_than_zero(self) -> None:
        # Arrange/Act
        with self.assertRaises(ValueError) as context:
            transaction = BankTransferTransaction("98765",
                                                  -100,
                                                  self.account,
                                                  self.target_account)

        # Assert
        self.assertEqual("amount must be greater than zero",
                         str(context.exception))

    def test_amount_is_zero(self) -> None:
        # Arrange/Act
        with self.assertRaises(ValueError) as context:
            transaction = BankTransferTransaction("98765",
                                                  0,
                                                  self.account,
                                                  self.target_account)

        # Assert
        self.assertEqual("amount must be greater than zero",
                         str(context.exception))

    def test_initialize_new_instance(self) -> None:
        # Arrange/Act
        transaction = BankTransferTransaction("98765",
                                              100,
                                              self.account,
                                              self.target_account)

        # Assert
        self.assertEqual("98765", transaction._Transaction__transaction_id)
        self.assertEqual(100, transaction._Transaction__amount)
        self.assertEqual(TransactionStatus.PENDING, transaction._Transaction__status)
        self.assertEqual(self.account, transaction._Transaction__account)
        self.assertEqual(self.target_account, transaction._BankTransferTransaction__target_account)


class TestFeesProperty(unittest.TestCase):
    """Defines tests for the fees property."""

    def setUp(self) -> None:
        # Arrange
        self.account = BankAccount(123456, 5000, "Sam", AccountStatus.ACTIVE)
        self.target_account = BankAccount(676767, 200, "Alex", AccountStatus.ACTIVE)

    def test_returns_base_fee(self) -> None:
        # Arrange
        transaction = BankTransferTransaction("98765",
                                              100,
                                              self.account,
                                              self.target_account)

        # Act/Assert
        self.assertEqual(1.00, transaction.fees)

    def test_returns_percentage_of_amount(self) -> None:
        # Arrange
        transaction = BankTransferTransaction("98765",
                                              1000,
                                              self.account,
                                              self.target_account)

        # Act/Assert
        self.assertAlmostEqual(7.00, transaction.fees)


class TestProcess(unittest.TestCase):
    """Defines tests for the process method."""

    def setUp(self) -> None:
        # Arrange
        self.account = BankAccount(123456, 500, "Sam", AccountStatus.ACTIVE)
        self.target_account = BankAccount(676767, 200, "Alex", AccountStatus.ACTIVE)

        self.transaction = BankTransferTransaction("98765",
                                                   100,
                                                   self.account,
                                                   self.target_account)

    def test_account_status_not_active(self) -> None:
        # Arrange
        self.account._BankAccount__status = AccountStatus.INACTIVE

        # Act
        self.transaction.process()

        # Assert
        self.assertEqual(TransactionStatus.FAILED, self.transaction.status)
        self.assertEqual(500, self.account.balance)
        self.assertEqual(200, self.target_account.balance)

    def test_target_account_status_not_active(self) -> None:
        # Arrange
        self.target_account._BankAccount__status = AccountStatus.INACTIVE

        # Act
        self.transaction.process()

        # Assert
        self.assertEqual(TransactionStatus.FAILED, self.transaction.status)
        self.assertEqual(500, self.account.balance)
        self.assertEqual(200, self.target_account.balance)

    def test_amount_and_fee_greater_than_balance(self) -> None:
        # Arrange
        self.account._BankAccount__balance = 100

        # Act
        self.transaction.process()

        # Assert
        self.assertEqual(TransactionStatus.FAILED, self.transaction.status)
        self.assertEqual(100, self.account.balance)
        self.assertEqual(200, self.target_account.balance)

    def test_transaction_is_processed(self) -> None:
        # Act
        self.transaction.process()

        # Assert
        self.assertEqual(TransactionStatus.PROCESSED, self.transaction.status)
        self.assertEqual(399, self.account.balance)
        self.assertEqual(300, self.target_account.balance)


class TestStr(unittest.TestCase):
    """Defines tests for the __str__ method."""

    def setUp(self) -> None:
        # Arrange
        self.account = BankAccount(123456, 5000, "Sam", AccountStatus.ACTIVE)
        self.target_account = BankAccount(676767, 200, "Alex", AccountStatus.ACTIVE)

        self.transaction = BankTransferTransaction("98765",
                                                   2983.35,
                                                   self.account,
                                                   self.target_account)

    def test_returns_string_representation(self) -> None:
        # Act
        actual = self.transaction.__str__()

        # Assert
        expected = ("ID: 98765\n"
                    "STATUS: PENDING\n"
                    "AMOUNT: $2,983.35\n"
                    "SOURCE ACCT: 123456 --> TARGET ACCT: 676767")
        self.assertEqual(expected, actual)