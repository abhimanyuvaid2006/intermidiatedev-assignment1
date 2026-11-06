"""The module defines tests for the PercentageFeeStrategy class."""

import unittest
from decimal import Decimal

from fee.percentage_fee_strategy import PercentageFeeStrategy

__author__ = "abhimanyu"
__version__ = "1.0.0"

class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""

    def setUp(self) -> None:
        """Runs before each test."""

        self.percentage = Decimal('0.02')

    def test_percentage_below_range(self) -> None:
        # Arrange
        self.percentage = Decimal('-0.01')

        # Act
        with self.assertRaises(ValueError) as context:
            PercentageFeeStrategy(self.percentage)

        # Assert
        self.assertEqual("percentage must be a value between 0 and "
                         "1 (inclusive)",
                         str(context.exception))

    def test_percentage_above_range(self) -> None:
        # Arrange
        self.percentage = Decimal('1.01')

        # Act
        with self.assertRaises(ValueError) as context:
            PercentageFeeStrategy(self.percentage)

        # Assert
        self.assertEqual("percentage must be a value between 0 and "
                         "1 (inclusive)",
                         str(context.exception))

    def test_percentage_is_low_range(self) -> None:
        # Arrange
        self.percentage = Decimal('0')

        # Act
        strategy = PercentageFeeStrategy(self.percentage)

        # Assert
        self.assertEqual(self.percentage,
                         strategy._PercentageFeeStrategy__percentage)

    def test_percentage_is_high_range(self) -> None:
        # Arrange
        self.percentage = Decimal('1')

        # Act
        strategy = PercentageFeeStrategy(self.percentage)

        # Assert
        self.assertEqual(self.percentage,
                         strategy._PercentageFeeStrategy__percentage)

    def test_initialize_new_instance(self) -> None:
        # Act
        strategy = PercentageFeeStrategy(self.percentage)

        # Assert
        self.assertEqual(self.percentage,
                         strategy._PercentageFeeStrategy__percentage)

class TestGetFee(unittest.TestCase):
    """Defines tests for the get_fee() method."""

    def setUp(self) -> None:
        """Runs before each test."""

        self.strategy = PercentageFeeStrategy(Decimal('0.02'))

    def test_returns_percentage_of_amount(self) -> None:
        self.assertEqual(Decimal('2.00'),
                         self.strategy.get_fee(Decimal('100')))

    def test_returns_fee_rounded_to_two_decimal_places(self) -> None:
        self.assertEqual(Decimal('2.47'),
                         self.strategy.get_fee(Decimal('123.45')))