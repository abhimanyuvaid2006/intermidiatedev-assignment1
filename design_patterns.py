"""This module includes a program to demonstrate your understanding of
the Design Patterns used in this project.
"""

__author__ = "abhimanyu"
__version__ = "1.0.0"

from decimal import Decimal

from account.account_status import AccountStatus
from account.bank_account import BankAccount
from events.logging_listener import LoggingListener
from fee.base_percentage_fee_strategy import BasePercentageFeeStrategy
from fee.percentage_fee_strategy import PercentageFeeStrategy
from transaction.credit_card_transaction import CreditCardTransaction



def main() -> None:
    """The program's main entry point."""

    # 1. Create a transaction instance.
    account = BankAccount(777777777,
                          Decimal('5000'),
                          "Sam",
                          AccountStatus.ACTIVE)
    transaction = CreditCardTransaction("123456789",
                                        Decimal('1000'),
                                        account,
                                        "0bcbe492-350e-4bea-92bc-f8714db9bc59")

    # 2. Print the transaction fee
    print(transaction.fees)

    # 3. Create a new instance of a fee strategy, the transaction fee
    #    is determined by base or percentage, depending which is higher.
    #    The base fee is $1.26 and the percentage of the transaction 
    #    amount is .07%.
    base_percentage_strategy = BasePercentageFeeStrategy(Decimal('1.26'),
                                                         Decimal('0.0007'))

    # 4. Update the transaction instance such that it will use the fee
    #    strategy to calculate the fees.
    transaction.set_fee_strategy(base_percentage_strategy)

    # 5. Print the transaction fees. Formatting is not required.
    print(transaction.fees)

    # 6. Update the transaction instance such that the fee strategy will
    #    determine the fee based only on percentage of the transaction
    #    amount. The fee is .35% of the transaction amount.
    percentage_strategy = PercentageFeeStrategy(Decimal('0.0035'))
    transaction.set_fee_strategy(percentage_strategy)

    # 7. Print the transaction fees. Formatting is not required.
    print(transaction.fees)

    # 8. Create a logging listener instance.
    listener = LoggingListener()

    # 9. Using the listener, subscribe to the event.
    transaction.on_processed.add_listener(listener)

    # 10. Invoke the method to raise the event.
    transaction.process()

if __name__ == "__main__":
    main()