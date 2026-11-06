"""The module defines tests for the BasePercentageFeeStrategy class."""

import unittest
from decimal import Decimal

from fee.base_percentage_fee_strategy import BasePercentageFeeStrategy

__author__ = "abhimanyu"
__version__ = "1.0.0"

class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""

    def setUp(self) -> None:
        """Runs before each test."""

        self.base_fee = Decimal('1.00')
        self.percentage = Decimal('0.007')

    def test_base_fee_below_range(self) -> None:
        # Arrange
        self.base_fee = Decimal('-1')

        # Act
        with self.assertRaises(ValueError) as context:
            BasePercentageFeeStrategy(self.base_fee, self.percentage)

        # Assert
        self.assertEqual("base_fee must be greater than or equal to "
                         "zero",
                         str(context.exception))

    def test_percentage_below_range(self) -> None:
        # Arrange
        self.percentage = Decimal('-0.01')

        # Act
        with self.assertRaises(ValueError) as context:
            BasePercentageFeeStrategy(self.base_fee, self.percentage)

        # Assert
        self.assertEqual("percentage must be a value between 0 and "
                         "1 (inclusive)",
                         str(context.exception))

    def test_percentage_above_range(self) -> None:
        # Arrange
        self.percentage = Decimal('1.01')

        # Act
        with self.assertRaises(ValueError) as context:
            BasePercentageFeeStrategy(self.base_fee, self.percentage)

        # Assert
        self.assertEqual("percentage must be a value between 0 and "
                         "1 (inclusive)",
                         str(context.exception))

    def test_base_fee_is_low_range(self) -> None:
        # Arrange
        self.base_fee = Decimal('0')

        # Act
        strategy = BasePercentageFeeStrategy(self.base_fee,
                                             self.percentage)

        # Assert
        self.assertEqual(self.base_fee,
                         strategy._BasePercentageFeeStrategy__base_fee)

    def test_percentage_is_low_range(self) -> None:
        # Arrange
        self.percentage = Decimal('0')

        # Act
        strategy = BasePercentageFeeStrategy(self.base_fee,
                                             self.percentage)

        # Assert
        self.assertEqual(self.percentage,
                         strategy._BasePercentageFeeStrategy__percentage)

    def test_percentage_is_high_range(self) -> None:
        # Arrange
        self.percentage = Decimal('1')

        # Act
        strategy = BasePercentageFeeStrategy(self.base_fee,
                                             self.percentage)

        # Assert
        self.assertEqual(self.percentage,
                         strategy._BasePercentageFeeStrategy__percentage)

    def test_initialize_new_instance(self) -> None:
        # Act
        strategy = BasePercentageFeeStrategy(self.base_fee,
                                             self.percentage)

        # Assert
        self.assertEqual(self.base_fee,
                         strategy._BasePercentageFeeStrategy__base_fee)
        self.assertEqual(self.percentage,
                         strategy._BasePercentageFeeStrategy__percentage)

class TestGetFee(unittest.TestCase):
    """Defines tests for the get_fee() method."""

    def setUp(self) -> None:
        """Runs before each test."""

        self.strategy = BasePercentageFeeStrategy(Decimal('1.00'),
                                                  Decimal('0.007'))

    def test_returns_base_fee(self) -> None:
        self.assertEqual(Decimal('1.00'),
                         self.strategy.get_fee(Decimal('100')))

    def test_returns_percentage_of_amount(self) -> None:
        self.assertEqual(Decimal('7.00'),
                         self.strategy.get_fee(Decimal('1000')))

    def test_returns_fee_rounded_to_two_decimal_places(self) -> None:
        self.assertEqual(Decimal('8.64'),
                         self.strategy.get_fee(Decimal('1234.56')))