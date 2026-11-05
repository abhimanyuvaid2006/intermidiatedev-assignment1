"""This module defines the BasePercentageFeeStrategy class."""

from decimal import Decimal
from fee.fee_strategy import FeeStrategy

__author__ = "Abhimanyu"
__version__ = "1.0.0"

class BasePercentageFeeStrategy(FeeStrategy):
    """Represents a fee strategy where the fee is a percentage of the
    transaction amount, or a base fee when the base fee is larger.
    """

    def __init__(self, base_fee: Decimal, percentage: Decimal) -> None:
        """Initializes a new instance of the BasePercentageFeeStrategy class.

        Args:
            base_fee (Decimal): The base fee to be charged.
            percentage (Decimal): The percentage of the transaction
                amount.

        Raises:
            ValueError: Raised when the base_fee is less than zero or
                the percentage is not between 0 and 1 (inclusive).
        """

        if base_fee < Decimal('0'):
            raise ValueError("base_fee must be greater than or equal to "
                             "zero")

        if (percentage < Decimal('0') or
           percentage > Decimal('1')):
            raise ValueError("percentage must be a value between 0 and "
                             "1 (inclusive)")

        self.__base_fee = base_fee
        self.__percentage = percentage

    def get_fee(self, transaction_amount: Decimal) -> Decimal:
        """Gets the fees to be charged for completing a transaction.

        Args:
            transaction_amount (Decimal): The amount of the transaction.

        Returns:
            Decimal: The percentage of the amount when greater than the
                base fee; otherwise the base fee. Rounded to two
                decimal places.
        """

        fee = round(transaction_amount * self.__percentage, 2)

        if fee < self.__base_fee:
            fee = self.__base_fee

        return round(fee, 2)