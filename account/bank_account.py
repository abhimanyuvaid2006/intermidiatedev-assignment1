from account.account_status import AccountStatus

class BankAccount():

    def __init__(
            self,
            account_id: int,
            balance: float,
            owner,
            status: AccountStatus): 
        """Represents an account at a financial institution.

        Raises:
            ValueError: If account_id is less than or equal to zero.
        """
        if account_id <= 0:
            raise ValueError("account_id must be a value greater than zero")

        self.__account_id = account_id
        self.__balance = balance
        self.__owner = owner
        self.__status = status

    @property
    def account_id(self) -> int:
        return self.__account_id

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @property
    def status(self) -> AccountStatus:
        return self.__status

    def update_balance(self, amount: float) -> None:
        self.__balance += amount

    def deposit(self, amount: float) -> None:
        """Updates the balance by the specified amount.

        Raises:
            ValueError: If amount is less than zero.
        """
        if amount < 0:
            raise ValueError("amount must be a value greater than or equal to zero")

        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """Updates the balance by subtracting the specified amount.

        Raises:
            ValueError: If amount is less than zero, or greater than
                the account balance.
        """
        if amount < 0:
            raise ValueError("amount must be a value greater than or equal to zero")

        if amount > self.__balance:
            raise ValueError("amount cannot exceed the account balance")

        self.update_balance(-amount)

        def __str__(self) -> str:
            return f"Account Number: {self.__account_id} Balance: ${self.__balance:,.2f}"

     