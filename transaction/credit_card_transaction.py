"""This module defines the CreditCardTransaction class"""

from decimal import Decimal
from account.account_status import AccountStatus
from account.bank_account import BankAccount
from transaction.transaction import Transaction
from transaction.transaction_status import TransactionStatus

class CreditCardTransaction(Transaction):
    """Represents a credit card transaction"""

    def __init__(self,
                 transaction_id: str,
                 amount: Decimal,
                 account: BankAccount,
                 authorization_code: str) -> None:
        """Initializes a new instance of CreditCardTransaction

            Args:
                transaction_id (str): The unique identity of the transaction
                amount (Decimal): The amount of the transaction
                account (BankAccount): The source account
                authorization_code (str): The code issued by the vendor

            Raises:
                ValueError: Raised when
                    - the transaction_id is blank
                    - the amount is less than or equal to zero
        """
        super().__init__(transaction_id, amount, account)

        self.__authorization_code = authorization_code

    @property
    def authorization_code(self) -> str:
        """Gets the authorization code

            Returns:
                str: The code issued by the vendor
        """
        return self.__authorization_code

    def process(self) -> None:
        """Processes the credit card transaction

            Fails when:
                - the source account is not active
                - the amount plus fees exceeds the balance
                - the authorization code is blank

            Raises the processed event when successfully processed.
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
            self.on_processed.notify(self)

    def __str__(self) -> str:
        """Returns the credit card transaction string representation

            Returns:
                str: The credit card transaction string representation
        """
        return (f"{super().__str__()}\n"
                f"AUTH CODE: {self.__authorization_code}")