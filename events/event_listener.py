"""This module defines the EventListener interface."""

from abc import ABC, abstractmethod

__author__ = "abhimanyu"
__version__ = "1.0.0"

class EventListener(ABC):
    """Represents the common interface for all event listeners."""

    @abstractmethod
    def update(self, sender: object) -> None:
        """Defines an action that can respond to an event.

        Args:
            sender (object): The object that raised the event.
        """
        pass