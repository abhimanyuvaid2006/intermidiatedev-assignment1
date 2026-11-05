"""This module defines the FeeStrategy interface."""

from abc import ABC, abstractmethod
from decimal import Decimal

__author__ = "abhimanyu"
__version__ = "1.0.0"

class FeeStrategy(ABC):
    """Represents the common interface for all fee strategies."""

    @abstractmethod
    def get_fee(self, transaction_amount: Decimal) -> Decimal:
        """Gets the fees to be charged for completing a transaction.

        Args:
            transaction_amount (Decimal): The amount of the transaction.

        Returns:
            Decimal: The fees to be charged for the transaction.
        """
        pass