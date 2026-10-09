"""This module defines the CreditCardTransaction class."""

from account.account_status import AccountStatus
from account.bank_account import BankAccount
from transaction.transaction import Transaction
from transaction.transaction_status import TransactionStatus


class CreditCardTransaction(Transaction):
    """Represents a credit card transaction against a bank account."""

    FEE_RATE = 0.02
    """The percentage of the amount charged as a fee (2%)."""

    def __init__(self,
                 transaction_id: str,
                 amount: float,
                 account: BankAccount,
                 authorization_code: str) -> None:
        """Initializes a new instance of the CreditCardTransaction class.

            Args:
                transaction_id (str): The unique identity of the transaction.
                amount (float): The amount of the transaction.
                account (BankAccount): The source account.
                authorization_code (str): The authorization code issued
                    by the credit card vendor.

            Raises:
                ValueError: Raised
                - the transaction_id is blank
                - the amount is less than or equal to zero
        """

        super().__init__(transaction_id, amount, account)

        self.__authorization_code = authorization_code

    @property
    def authorization_code(self) -> str:
        """Gets the authorization code for the transaction.

            Returns:
                str: The authorization code issued by the vendor.
        """
        return self.__authorization_code

    @property
    def fees(self) -> float:
        """Gets the fees to debit when the transaction is processed.

            Returns:
                float: The fees, 2% of the transaction amount.
        """
        return self.amount * CreditCardTransaction.FEE_RATE

    def process(self) -> None:
        """Processes the credit card transaction.

            The transaction fails when:
                - the source account is not active
                - the amount plus fees exceeds the account balance
                - the authorization code is a blank string

            When valid and pending, the funds are withdrawn and the
            status is set to processed.
        """
        total = self.amount + self.fees

        if self.account.status != AccountStatus.ACTIVE:
            self.status = TransactionStatus.FAILED

        if total > self.account.balance:
            self.status = TransactionStatus.FAILED

        if len(self.__authorization_code.strip()) == 0:
            self.status = TransactionStatus.FAILED

        if self.status == TransactionStatus.PENDING:
            self.account.withdraw(self.amount)
            self.account.withdraw(self.fees)
            self.status = TransactionStatus.PROCESSED

    def __str__(self) -> str:
        """Returns the credit card transaction string representation.

            Returns:
                str: The credit card transaction string representation.
        """
        return (f"{super().__str__()}\n"
                f"AUTH CODE: {self.__authorization_code}")