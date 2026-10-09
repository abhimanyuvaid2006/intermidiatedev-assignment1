"""This module defines the Transaction class."""

__author__ = "Abhimanyu"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from account.bank_account import BankAccount
from transaction.transaction_status import TransactionStatus


class Transaction(ABC):
    """Represents a bank account transaction."""

    def __init__(self,
                 transaction_id: str,
                 amount: float,
                 account: BankAccount):
        """Initializes a new instance of the Transaction class.

        Args:
            transaction_id (str): The unique identity of the transaction.
            amount (float): The amount of the transaction.
            account (BankAccount): The source account for the
                transaction.

        Raises:
            ValueError: Raised when the transaction_id is blank or the
                amount is less than or equal to zero.
        """
        if len(transaction_id.strip()) == 0:
            raise ValueError("transaction_id cannot be blank")

        if amount <= 0:
            raise ValueError("amount must be greater than zero")

        self.__transaction_id = transaction_id
        self.__amount = amount
        self.__status = TransactionStatus.PENDING
        self.__account = account

    @property
    def transaction_id(self) -> str:
        """Gets the unique identity of the transaction.

        Returns:
            str: The transaction id.
        """
        return self.__transaction_id

    @property
    def amount(self) -> float:
        """Gets the amount of the transaction.

        Returns:
            float: The transaction amount.
        """
        return self.__amount

    @property
    def status(self) -> TransactionStatus:
        """Gets the status of the transaction.

        Returns:
            TransactionStatus: The status of the transaction.
        """
        return self.__status

    @status.setter
    def status(self, status: TransactionStatus) -> None:
        """Sets the status of the transaction.

        Args:
            status (TransactionStatus): The new status.
        """
        self.__status = status

    @property
    def account(self) -> BankAccount:
        """Gets the source account for the transaction.

        Returns:
            BankAccount: The source account.
        """
        return self.__account

    @property
    @abstractmethod
    def fees(self) -> float:
        """Gets the fees to debit from the account when the
        transaction is processed.

        Returns:
            float: The transaction fees.
        """
        pass

    @abstractmethod
    def process(self) -> None:
        """Processes the transaction."""
        pass

    def __str__(self) -> str:
        """Returns the "informal" or nicely printable string
                representation of the object.

        Returns:
            str: The "informal" or nicely printable string
                representation of the object.
        """
        return (f"ID: {self.__transaction_id}\n"
                f"STATUS: {self.__status.name}\n"
                f"AMOUNT: ${self.__amount:,.2f}\n"
                f"SOURCE ACCT: {self.__account.account_id}")