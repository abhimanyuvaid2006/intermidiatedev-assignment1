"""This module defines the Transaction class."""

__author__ = "abhimanyu"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from decimal import Decimal
from account.bank_account import BankAccount
from events.event import Event
from fee.fee_strategy import FeeStrategy
from transaction.transaction_status import TransactionStatus

class Transaction(ABC):
    """Represents a bank account transaction."""

    def __init__(self,
                 transaction_id: str,
                 amount: Decimal,
                 account: BankAccount) -> None:
        """Initializes a new instance of the Transaction class.

        Args:
            transaction_id (str): The unique identity of the transaction.
            amount (Decimal): The amount of the transaction.
            account (BankAccount): The source account for the
                transaction.

        Raises:
            ValueError: Raised when the transaction_id is blank or the
                amount is less than or equal to zero.
        """

        if len(transaction_id.strip()) == 0:
            raise ValueError("transaction_id cannot be blank")

        if amount <= Decimal('0'):
            raise ValueError("amount must be greater than zero")

        self.__transaction_id = transaction_id
        self.__amount = amount
        self.__status = TransactionStatus.PENDING
        self.__account = account
        self.__fee_strategy = None
        self.__processed_event = Event()

    @property
    def transaction_id(self) -> str:
        """Gets the unique identity of the transaction.

        Returns:
            str: The transaction id.
        """
        return self.__transaction_id

    @property
    def amount(self) -> Decimal:
        """Gets the amount of the transaction.

        Returns:
            Decimal: The transaction amount.
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
    def fees(self) -> Decimal:
        """Gets the fees to debit from the account when the
        transaction is processed.

        Returns:
            Decimal: The fee from the fee strategy, or 0.0 when no
                fee strategy has been set.
        """
        if not self.__fee_strategy:
            fees = Decimal('0.0')
        else:
            fees = self.__fee_strategy.get_fee(self.__amount)

        return fees

    @property
    def on_processed(self) -> Event:
        """Gets the event raised when the transaction is processed.

        Returns:
            Event: The processed event.
        """
        return self.__processed_event

    def set_fee_strategy(self, strategy: FeeStrategy) -> None:
        """Sets the fee strategy used to calculate the fees.

        Args:
            strategy (FeeStrategy): The fee strategy to apply.
        """
        self.__fee_strategy = strategy

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