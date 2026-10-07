
from account.bank_account import BankAccount
from transaction.transaction_status import TransactionStatus


class Transaction():
    """Represents a bank account transaction."""

    def __init__(self, transaction_id: str, amount: float, account: BankAccount):
        """Initialize a transaction with a status of pending.

        Raises:
            ValueError: If transaction_id is blank or amount is <= 0.
        """
        if not transaction_id.strip():
            raise ValueError("transaction_id cannot be blank")
        if amount <= 0:
            raise ValueError("amount must be greater than zero")

        self.__transaction_id = transaction_id
        self.__amount = amount
        self.__status = TransactionStatus
        self.__account = account

    @property
    def transaction_id(self) -> str:
        return self.__transaction_id

    @property
    def amount(self) -> float:
        return self.__amount

    @property
    def status(self) -> TransactionStatus:
        return self.__status