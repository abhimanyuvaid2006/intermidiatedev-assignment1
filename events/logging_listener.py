"""This module defines the LoggingListener class."""

from events.event_listener import EventListener
from transaction.transaction import Transaction

__author__ = "abhimanyu "
__version__ = "1.0.0"

class LoggingListener(EventListener):
    """Represents an event listener that is used for logging."""

    def update(self, sender: object) -> None:
        """Outputs a logging message to the console.

        The message is only output when the sender is a Transaction
        type.

        Args:
            sender (object): The object that raised the event.

        Raises:
            TypeError: Raised when the sender is not a Transaction type.
        """

        if isinstance(sender, Transaction):
            print("TRANSACTION PROCESSED")
            print("=" * 80)
            print(sender)
            print("-" * 80)
        else:
            raise TypeError("sender must be a Transaction type")