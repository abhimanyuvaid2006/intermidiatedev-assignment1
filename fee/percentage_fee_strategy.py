"""This module defines the PercentageFeeStrategy class."""

__author__ = "Abhimanyu"
__version__ = "1.0.0"

from decimal import Decimal
from fee.fee_strategy import FeeStrategy


class PercentageFeeStrategy(FeeStrategy):
    """Represents a fee strategy where the fee is a percentage of the
    transaction amount.
    """

    def __init__(self, percentage: Decimal) -> None:
        """Initializes a new instance of the PercentageFeeStrategy class.

        Args:
            percentage (Decimal): The percentage of the transaction
                amount.

        Raises:
            ValueError: Raised when the percentage is not between 0 and
                1 (inclusive).
        """

        if (percentage < Decimal('0') or
           percentage > Decimal('1')):
            raise ValueError("percentage must be a value between 0 and "
                             "1 (inclusive)")

        self.__percentage = percentage

    def get_fee(self, transaction_amount: Decimal) -> Decimal:
        """Gets the fees to be charged for completing a transaction.

        Args:
            transaction_amount (Decimal): The amount of the transaction.

        Returns:
            Decimal: The percentage of the amount, rounded to two
                decimal places.
        """

        return round(transaction_amount * self.__percentage, 2)