"""This module defines tests for the CreditCardTransaction class."""



import unittest
from decimal import Decimal

from account.account_status import AccountStatus
from account.bank_account import BankAccount
from fee.percentage_fee_strategy import PercentageFeeStrategy
from transaction.credit_card_transaction import CreditCardTransaction
from transaction.transaction_status import TransactionStatus

__author__ = "abhimanyu"
__version__ = "1.0.0"


class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""

    def setUp(self) -> None:
        # Arrange
        self.account = BankAccount(123456, Decimal("500"), "Sam", AccountStatus.ACTIVE)

    def test_transaction_id_is_blank_string(self) -> None:
        # Arrange/Act
        with self.assertRaises(ValueError) as context:
            transaction = CreditCardTransaction("",
                                                Decimal("100"),
                                                self.account,
                                                "c13d9c63")

        # Assert
        self.assertEqual("transaction_id cannot be blank",
                         str(context.exception))

    def test_amount_is_less_than_zero(self) -> None:
        # Arrange/Act
        with self.assertRaises(ValueError) as context:
            transaction = CreditCardTransaction("98765",
                                                Decimal("-100"),
                                                self.account,
                                                "c13d9c63")

        # Assert
        self.assertEqual("amount must be greater than zero",
                         str(context.exception))

    def test_amount_is_zero(self) -> None:
        # Arrange/Act
        with self.assertRaises(ValueError) as context:
            transaction = CreditCardTransaction("98765",
                                                Decimal("0"),
                                                self.account,
                                                "c13d9c63")

        # Assert
        self.assertEqual("amount must be greater than zero",
                         str(context.exception))

    def test_initialize_new_instance(self) -> None:
        # Arrange/Act
        transaction = CreditCardTransaction("98765",
                                            Decimal("100"),
                                            self.account,
                                            "c13d9c63")

        # Assert
        self.assertEqual("98765", transaction._Transaction__transaction_id)
        self.assertEqual(Decimal("100"), transaction._Transaction__amount)
        self.assertEqual(TransactionStatus.PENDING, transaction._Transaction__status)
        self.assertEqual(self.account, transaction._Transaction__account)
        self.assertEqual("c13d9c63", transaction._CreditCardTransaction__authorization_code)


class TestProcess(unittest.TestCase):
    """Defines tests for the process method."""

    def setUp(self) -> None:
        # Arrange
        self.account = BankAccount(123456, Decimal("500"), "Sam", AccountStatus.ACTIVE)

        self.transaction = CreditCardTransaction("98765",
                                                 Decimal("100"),
                                                 self.account,
                                                 "c13d9c63")

    def test_account_status_not_active(self) -> None:
        # Arrange
        self.account._BankAccount__status = AccountStatus.INACTIVE

        # Act
        self.transaction.process()

        # Assert
        self.assertEqual(TransactionStatus.FAILED, self.transaction.status)
        self.assertEqual(Decimal("500"), self.account.balance)

    def test_amount_and_fee_greater_than_balance(self) -> None:
        # Arrange
        self.account._BankAccount__balance = Decimal("50")

        # Act
        self.transaction.process()

        # Assert
        self.assertEqual(TransactionStatus.FAILED, self.transaction.status)
        self.assertEqual(Decimal("50"), self.account.balance)

    def test_authorization_code_is_blank_string(self) -> None:
        # Arrange
        transaction = CreditCardTransaction("98765",
                                            Decimal("100"),
                                            self.account,
                                            "")

        # Act
        transaction.process()

        # Assert
        self.assertEqual(TransactionStatus.FAILED, transaction.status)
        self.assertEqual(Decimal("500"), self.account.balance)

    def test_transaction_is_processed(self) -> None:
        # Act
        self.transaction.process()

        # Assert
        self.assertEqual(TransactionStatus.PROCESSED, self.transaction.status)
        self.assertEqual(Decimal("400"), self.account.balance)

    def test_transaction_is_processed_with_fee_strategy(self) -> None:
        # Arrange
        self.transaction.set_fee_strategy(PercentageFeeStrategy(Decimal("0.02")))

        # Act
        self.transaction.process()

        # Assert
        self.assertEqual(TransactionStatus.PROCESSED, self.transaction.status)
        self.assertEqual(Decimal("398.00"), self.account.balance)


class TestStr(unittest.TestCase):
    """Defines tests for the __str__ method."""

    def setUp(self) -> None:
        # Arrange
        self.account = BankAccount(123456, Decimal("5000"), "Sam", AccountStatus.ACTIVE)

        self.transaction = CreditCardTransaction("98765",
                                                 Decimal("2983.35"),
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