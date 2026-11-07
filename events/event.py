"""This module defines the Event class."""

from events.event_listener import EventListener

__author__ = "abhimanyu"
__version__ = "1.0.0"

class Event:
    """Represents an object's event."""

    def __init__(self) -> None:
        """Initializes a new instance of the Event class.

        The event is initialized with no listeners.
        """

        self.__listeners = []

    def add_listener(self, listener: EventListener) -> None:
        """Adds a listener to the list of listeners.

        Args:
            listener (EventListener): The listener to add.
        """
        self.__listeners.append(listener)

    def remove_listener(self, listener: EventListener) -> None:
        """Removes a listener from the list of listeners.

        If the listener is not in the list, nothing happens.

        Args:
            listener (EventListener): The listener to remove.
        """
        if listener in self.__listeners:
            self.__listeners.remove(listener)

    def notify(self, sender: object) -> None:
        """Raises the event by invoking each listener's action.

        If there are no listeners, no actions take place.

        Args:
            sender (object): The object that raised the event.
        """
        for listener in self.__listeners:
            listener.update(sender)