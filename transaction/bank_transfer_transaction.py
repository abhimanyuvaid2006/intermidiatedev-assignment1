"""This module defines the BankTransferTransaction class."""

__author__ = "Your Name"
__version__ = "1.0.0"

from account.account_status import AccountStatus
from account.bank_account import BankAccount
from transaction.transaction import Transaction
from transaction.transaction_status import TransactionStatus


class BankTransferTransaction(Transaction):
    """Represents a transfer of funds between two bank accounts."""

    BASE_FEE = 1.00
    """The minimum fee charged for a transfer."""

    FEE_RATE = 0.007
    """The percentage of the amount charged as a fee (0.7%)."""

    def __init__(self,
                 transaction_id: str,
                 amount: float,
                 account: BankAccount,
                 target_account: BankAccount) -> None:
        """Initializes a new instance of the BankTransferTransaction class.

            Args:
                transaction_id (str): The unique identity of the transaction.
                amount (float): The amount of the transaction.
                account (BankAccount): The source account.
                target_account (BankAccount): The account funds are
                    transferred to.

            Raises:
                ValueError: Raised
                - the transaction_id is blank
                - the amount is less than or equal to zero
        """

        super().__init__(transaction_id, amount, account)

        self.__target_account = target_account

    @property
    def target_account(self) -> BankAccount:
        """Gets the target account for the transaction.

            Returns:
                BankAccount: The account funds are transferred to.
        """
        return self.__target_account

    @property
    def fees(self) -> float:
        """Gets the fees to debit when the transaction is processed.

            Returns:
                float: The larger of the base fee or the percentage fee.
        """
        percentage_fee = self.amount * BankTransferTransaction.FEE_RATE

        if percentage_fee >= BankTransferTransaction.BASE_FEE:
            return percentage_fee
        else:
            return BankTransferTransaction.BASE_FEE

    def process(self) -> None:
        """Processes the bank transfer transaction.

            The transaction fails when:
                - the source account is not active
                - the target account is not active
                - the amount plus fees exceeds the source balance

            When valid and pending, the funds are transferred and the
            status is set to processed.
        """
        total = self.amount + self.fees

        if self.account.status != AccountStatus.ACTIVE:
            self.status = TransactionStatus.FAILED

        if self.__target_account.status != AccountStatus.ACTIVE:
            self.status = TransactionStatus.FAILED

        if total > self.account.balance:
            self.status = TransactionStatus.FAILED

        if self.status == TransactionStatus.PENDING:
            self.account.withdraw(self.amount)
            self.account.withdraw(self.fees)
            self.__target_account.deposit(self.amount)
            self.status = TransactionStatus.PROCESSED

    def __str__(self) -> str:
        """Returns the bank transfer transaction string representation.

            Returns:
                str: The bank transfer transaction string representation.
        """
        return (f"{super().__str__()} --> "
                f"TARGET ACCT: {self.__target_account.account_id}")