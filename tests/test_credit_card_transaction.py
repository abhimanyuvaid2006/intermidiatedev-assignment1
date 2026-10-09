"""This module defines tests for the CreditCardTransaction class."""


import unittest
from account.account_status import AccountStatus
from account.bank_account import BankAccount
from transaction.credit_card_transaction import CreditCardTransaction
from transaction.transaction_status import TransactionStatus

__author__ = "abhimanyu"
__version__ = "1.0.0"


class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""

    def setUp(self) -> None:
        # Arrange
        self.account = BankAccount(123456, 500, "Sam", AccountStatus.ACTIVE)

    def test_transaction_id_is_blank_string(self) -> None:
        # Arrange/Act
        with self.assertRaises(ValueError) as context:
            transaction = CreditCardTransaction("",
                                                100,
                                                self.account,
                                                "c13d9c63")

        # Assert
        self.assertEqual("transaction_id cannot be blank",
                         str(context.exception))

    def test_amount_is_less_than_zero(self) -> None:
        # Arrange/Act
        with self.assertRaises(ValueError) as context:
            transaction = CreditCardTransaction("98765",
                                                -100,
                                                self.account,
                                                "c13d9c63")

        # Assert
        self.assertEqual("amount must be greater than zero",
                         str(context.exception))

    def test_amount_is_zero(self) -> None:
        # Arrange/Act
        with self.assertRaises(ValueError) as context:
            transaction = CreditCardTransaction("98765",
                                                0,
                                                self.account,
                                                "c13d9c63")

        # Assert
        self.assertEqual("amount must be greater than zero",
                         str(context.exception))

    def test_initialize_new_instance(self) -> None:
        # Arrange/Act
        transaction = CreditCardTransaction("98765",
                                            100,
                                            self.account,
                                            "c13d9c63")

        # Assert
        self.assertEqual("98765", transaction._Transaction__transaction_id)
        self.assertEqual(100, transaction._Transaction__amount)
        self.assertEqual(TransactionStatus.PENDING, transaction._Transaction__status)
        self.assertEqual(self.account, transaction._Transaction__account)
        self.assertEqual("c13d9c63", transaction._CreditCardTransaction__authorization_code)


class TestFeesProperty(unittest.TestCase):
    """Defines tests for the fees property."""

    def test_returns_percentage_of_amount(self) -> None:
        # Arrange
        account = BankAccount(123456, 500, "Sam", AccountStatus.ACTIVE)
        transaction = CreditCardTransaction("98765",
                                            100,
                                            account,
                                            "c13d9c63")

        # Act/Assert
        self.assertAlmostEqual(2.00, transaction.fees)


class TestProcess(unittest.TestCase):
    """Defines tests for the process method."""

    def setUp(self) -> None:
        # Arrange
        self.account = BankAccount(123456, 500, "Sam", AccountStatus.ACTIVE)

        self.transaction = CreditCardTransaction("98765",
                                                 100,
                                                 self.account,
                                                 "c13d9c63")

    def test_account_status_not_active(self) -> None:
        # Arrange
        self.account._BankAccount__status = AccountStatus.INACTIVE

        # Act
        self.transaction.process()

        # Assert
        self.assertEqual(TransactionStatus.FAILED, self.transaction.status)
        self.assertEqual(500, self.account.balance)

    def test_amount_and_fee_greater_than_balance(self) -> None:
        # Arrange
        self.account._BankAccount__balance = 101

        # Act
        self.transaction.process()

        # Assert
        self.assertEqual(TransactionStatus.FAILED, self.transaction.status)
        self.assertEqual(101, self.account.balance)

    def test_authorization_code_is_blank_string(self) -> None:
        # Arrange
        transaction = CreditCardTransaction("98765",
                                            100,
                                            self.account,
                                            "")

        # Act
        transaction.process()

        # Assert
        self.assertEqual(TransactionStatus.FAILED, transaction.status)
        self.assertEqual(500, self.account.balance)

    def test_transaction_is_processed(self) -> None:
        # Act
        self.transaction.process()

        # Assert
        self.assertEqual(TransactionStatus.PROCESSED, self.transaction.status)
        self.assertEqual(398, self.account.balance)


class TestStr(unittest.TestCase):
    """Defines tests for the __str__ method."""

    def setUp(self) -> None:
        # Arrange
        self.account = BankAccount(123456, 5000, "Sam", AccountStatus.ACTIVE)

        self.transaction = CreditCardTransaction("98765",
                                                 2983.35,
                                                 self.account,
                                                 "c13d9c63-d8c3-4876-a00c-81ab7c3ff1fc")

    def test_returns_string_representation(self) -> None:
        # Act
        actual = self.transaction.__str__()

        # Assert
        expected = ("ID: 98765\n"
                    "STATUS: PENDING\n"
                    "AMOUNT: $2,983.35\n"
                    "SOURCE ACCT: 123456\n"
                    "AUTH CODE: c13d9c63-d8c3-4876-a00c-81ab7c3ff1fc")
        self.assertEqual(expected, actual)
